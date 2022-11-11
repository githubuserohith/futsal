from flask import Flask, render_template, redirect, request, flash, session
import my_form
import secrets
from flask_login import UserMixin
from datetime import datetime, date, time
import pytz
import pyodbc
from futsal_email import email_attachements_main, booking_confirmation, email_welcome
from flask_session import Session


def select_query(query):
    conn = pyodbc.connect(
        driver='{SQL Server Native Client 11.0}',
        server='(localdb)\MSSQLLocalDB',
        database='futsal',
        trusted_connection='YES'
    )
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result
    conn.close()


def insert_query(query):
    conn = pyodbc.connect(
        driver='{SQL Server Native Client 11.0}',
        server='(localdb)\MSSQLLocalDB',
        database='futsal',
        trusted_connection='YES'
    )
    cursor = conn.cursor()
    cursor.execute(query)
    cursor.commit()
    cursor.close()
    conn.commit()
    conn.close()


app = Flask(__name__)
token = secrets.token_hex(16)
app.config['SECRET_KEY'] = token

# SESSIONS
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    session.clear()
    form = my_form.Login()
    global username
    gender = request.form.get('gender')
    if request.method == 'POST':
        if request.form.get('submit_signup'):
            return redirect('/signup')
        elif request.form.get('submit_login'):
            username = request.form.get('username')
            password = request.form.get('password')
            query = f"select username from tbluser where username='{username}'"
            result_username = select_query(query)

            if result_username:
                query = f"select password from tbluser where username='{username}' and password='{password}'"
                result_password = select_query(query)

                if result_password:
                    session["username"] = username
                    flash(f'Logged in as {session["username"]}', category='success')
                    return redirect('/book')
                else:
                    flash('Incorrect password', category='error')

            else:
                flash('Username is incorrect or does not exist.', category='error')

        elif request.form.get('submit_login_otp'):
            return redirect('/login_otp')

    return render_template('login.html', form=form)


@app.route('/login_otp', methods=['GET', 'POST'])
def login_otp():
    form = my_form.Login_otp()
    global email_otp
    if request.method == 'POST' or request.method == 'GET':
        try:
            if request.form.get('send_otp'):
                email_add = request.form.get('email_add')

                try:
                    email_otp = int(email_attachements_main(email_add))
                    otp_str = str(email_otp)
                    flash("OTP sent to your email", category="success")
                    query = f"select username from tbluser where username='{email_add}'"
                    result = select_query(query)
                    if result:
                        query = f"update tbluser set password='{otp_str}' where username='{email_add}'"
                        insert_query(query)
                        flash("Your password has been updated with OTP.", category="success")
                    else:
                        query = f"exec sp_login '{email_add}', '{email_otp}' "
                        insert_query(query)

                except:
                    flash("Invalid email address. Try again.", category="error")

            elif request.form.get('verify_otp'):
                otp = int(request.form.get('otp'))
                if otp == email_otp:
                    flash("otp verified. Please login.", category='success')

                elif otp == 0000:
                    flash("please enter otp", category='error')
                else:
                    flash("Incorrect otp. Please try again.", category='error')

        except:
            flash("otp not sent. Please click the 'Send otp' button", category='error')
            return redirect('/login_otp')

    return render_template('login_otp.html', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = my_form.Signup()
    if request.form.get('submit_login1'):
        return redirect('/home')
    elif request.method == 'POST':
        if request.form.get('submit_signup1'):
            username1 = request.form.get('username1')
            password1 = request.form.get('password1')
            confirmpwd = request.form.get('confirmpwd')
            created_time = datetime.now()
            query = f"select username from tbluser where username='{username1}'"
            result = select_query(query)

            if not result:
                if password1 == confirmpwd:
                    try:
                        email_welcome(username1)
                        query = f"exec sp_login '{username1}', '{password1}' "
                        insert_query(query)
                        flash(f'Account created successfully for "{username1}". Please Login', category='success')
                    except:
                        flash("Invalid email address", category="error")
                else:
                    flash('Password and Confirm passwords do not match', category='error')
            else:
                flash('Username already exists. Please choose another.', category='error')

    return render_template('signup.html', form=form)


@app.route('/book', methods=['GET', 'POST'])
def book():
    form = my_form.Book()
    if session.get("username"):
        if request.method == 'POST':
            if request.form.get('submit_booking') or request.form.get('confirm_booking'):
                global slot_date_str, slot_time, price
                slot_date_str = request.form.get('slot_date')
                slot_date = datetime.strptime(slot_date_str, '%Y-%m-%d')
                slot_time = request.form.get('slot_time')
                slot_time = slot_time.split(':')[0]
                ampm = int(slot_time)
                today_date_str = str(datetime.now()).split(' ')[0]
                today_date = datetime.strptime(today_date_str, '%Y-%m-%d')
                if slot_date < today_date:
                    flash("Invalid date", category='error')
                    return redirect('/book')
                else:
                    query = f"select * from tblbooking where slot_date='{slot_date_str}' and slot_time='{slot_time}' and available='no' "
                    result = select_query(query)
                    if result:
                        flash("The chosen slot is not available. Please choose alternate slot.", category='error')
                        return redirect('/book')
                    else:
                        if slot_date.isoweekday() in range(1, 6):
                            if ampm < 13:
                                price = 750
                                flash(f"The chosen slot is available for Rs {price}. Book slot to confirm booking.")
                            else:
                                price = 1000
                                flash(f"The chosen slot is available for Rs {price}. Book slot to confirm booking.")

                        else:
                            if ampm < 12:
                                price = 1200
                                flash(f"The chosen slot is available for Rs {price}. Book slot to confirm booking.")

                            else:
                                price = 1500
                                flash(f"The chosen slot is available for Rs {price}. Book slot to confirm booking.")

            if request.form.get('confirm_booking'):
                query = f"insert into tblbooking values ('{session['username']}','{slot_date_str}','{slot_time}',{price},'no')"
                insert_query(query)
                flash(
                    f"Slot has been booked for {slot_date_str} : {slot_time}:00 hr. Please check your email ({session['username']}) for booking confirmation. ")
                booking_confirmation(session["username"], slot_date_str, slot_time)
                return redirect('/book')
    else:
        flash("Please login to continue!", category='error')
        return redirect('/login')

    return render_template('book.html', form=form)


# @app.route('/account', methods=['GET', 'POST'])
# def account():
#     form = my_form.Account()
#     return render_template('account.html', form=form)


@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out. Please login again.', category='success')
    return redirect('/login')


if __name__ == "__main__":
    app.run(debug=True)
