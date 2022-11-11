
# Futsal

A footabll match booking system built using Flask. HTML and Bootstrap is used for front end whereas Python and SSMS is used for backend development.


## This system is built for the purpose:
* Signup, Login and Logout securely
* Check if a slot is available for booking
* Fare enquiry
* Book the slot for match


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 


### Installing

To deploy this application follow these steps;
* clone/download this project from git hub
```
 git clone https://github.com/githubuserohith/futsal.git

```
* Extract the project and open it in an Editor forexample Vs code ,Pycharm or any editor of your choice.
* Create a python virtual environment using the following command
```
 virtualenv  venv 

``` 
* In windows, navigate to scripts in the venv folder where the virtual environment exists.
```
 cd venv\scripts

```
*  Activate the virtual environment using the following command ;
```
activate

```
* In linux, activate the virtual environment using ;
```
source bin/activate

```
* Execute the application by running a a given command

```
 python my_futsal.py

``` 

* After running that command the server will start running at http://127.0.0.1:5000/ which is the default URL.

* Copy paste the url http://127.0.0.1:5000/home in your browser.


## Database

* Microsoft SQL Server Management Studio 18

* Create a new database named "futsal"

* Run "futsal_script" file in SSMS for required tables and stored procedures to be created.

## Signup

Enter your valid email address and choose a password to create an account. Once successfully signed up, a sign in email will be sent to you.

![alt text](https://imgur.com/pmlMGiI.png)


## Login

Enter email address(Username) and password to login.

![alt text](https://imgur.com/qwsLJTI.png)


## Login with OTP

You can use this option if you wish to login without signing up.

Enter your email address and click on "send OTP". An OTP will be sent to your entered email address.

Enter that OTP and click on "Verify OTP" for verification.

You can use this OTP as your password to login next time.

![alt text](https://imgur.com/StEXMGe.png)


## Fare enquiry

Fare is divided into 4 categories for calculation-

(1) Weekday and morning - Rs 750/-

(2) Weekday and night - Rs 1000/-

(3) Weekend and morning - Rs 1200/-

(4) Weekend and night - Rs 1500/-


## Booking 

* Every slot is for an hour, so a day has 24 slots.

* For example, if a booking is made for 5:20 pm (or anytime between 5-6pm), the slot of 5-6pm remains unavailable for other users.

* You can check if a slot of your choise is available or not, before booking.

* Once the booking is confirmed, you'll receive a booking confirmation email with details.

![alt text](https://imgur.com/I4fQbbf.png)

![alt text](https://imgur.com/fDGjapE.png)

![alt text](https://imgur.com/VUNFCnj.png)

![alt text](https://imgur.com/ihpNMLg.png)






