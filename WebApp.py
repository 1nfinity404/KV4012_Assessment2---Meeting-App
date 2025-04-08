from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
from datetime import datetime
import re

import Classes as Class


def link(url, name):
    put_html(f"<div style='text-align:center;'><a href={url}>{name}</a></div>")


def validate_email(email: str) -> bool:
    # Regular expression for email address
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{3,}$'

    # Use re.match to check if the email matches the pattern
    if re.match(email_pattern, email):
        return True
    else:
        return False


def validate_name(name: str) -> bool:
    # Regular expression for validating a name
    name_pattern = r'^[a-zA-Z]+([ -]?[a-zA-Z]+)*$'

    # Use re.match to check if the name matches the pattern
    if re.match(name_pattern, name):
        return True
    else:
        return False


user = Class.User("name", 12345678, "00/00/0000", "name@email.com", "username", "password")


# Login user page
def user_login_page():
    clear()
    put_html("<h1 class='text-center'>Log In</h1>")

    link("?app=password_reset", "Forgot Password?")
    link("?app=register", "Register")

    user_login = input_group('', [
        input("Username", name="name", required=True),
        input("Password", name="password", required=True, type=PASSWORD)
    ])


# Password reset page
def password_reset_page():
    clear()
    put_html("<h1 class='text-center'>Password Reset</h1>")

    password_reset = input_group('', [
        input("New Password", name="new_password", required=True, type=PASSWORD),
        input("Confirm Password", name="confirm_password", required=True, type=PASSWORD)
    ])


# Register user page
def register_page():
    clear()
    global user
    put_html("<h1 class='text-center'>Register</h1>")

    user_register = input_group('', [
        input("Enter Name", name="name", required=True, type=TEXT),
        input("Student ID", name="student_id", required=True, type=NUMBER),
        input("Date of Birth", name="dob", required=True, type=DATE),
        input("Email address", name="email", required=True),
        input("Username", name="username", required=True),
        input("Password", name="password", required=True)
    ])

    if not validate_name(user_register["name"]):
        toast("Your name should not contain numbers!", 5)
        register_page()
    elif len(str(user_register["student_id"])) != 8:
        toast("Your student ID should have 8 numbers", 5)
        register_page()
    elif not validate_email(user_register["email"]):
        toast("Your email is incorrect!", 5)
        register_page()
    elif 5 > len(user_register["username"]) > 15:
        toast("Your username is too short or long!", 5)
        register_page()
    elif 5 > len(user_register["password"]) > 15:
        toast("Your password is too short or long!", 5)
        register_page()
    elif "#" in user_register["name"] or "#" in user_register["password"]:
        toast("Your username and password should not contain #!", 5)
        register_page()
    else:
        user = Class.User(user_register['name'], user_register["student_id"], user_register['dob'],
                          user_register['email'], user_register['username'], user_register['password'])
        with open("user_database.txt", "a") as file:
            file.write(f"{user},")


#
def tutor_meeting_page():
    clear()
    put_html("<h1 class='text-center'>Tutor Meetings</h1>")


#
def notifications_page():
    clear()
    put_html("<h1 class='text-center'>Notifications</h1>")


#
def tutors_page():
    clear()
    put_html("<h1 class='text-center'>Tutors</h1>")


#
def tutor_profile_page():
    clear()
    put_html("<a class='btn btn-primary' href='?app=tutors' role='button'>Back</a>")

    put_html("<h1 class='text-center'>Profile</h1>")


#
def create_meeting_page():
    clear()
    put_html("<h1 class ='text-center'>Create New Meeting</h1>")


# User Profile Page
def user_profile_page():
    clear()
    put_html("<h1 class ='text-center'>Profile</h1>")


if __name__ == '__main__':
    routes = {
        'login': user_login_page,
        'register': register_page,
        'password_reset': password_reset_page,
        'tutor_meeting': tutor_meeting_page,
        'notifications': notifications_page,
        'tutors': tutors_page,
        'tutor_profile': tutor_profile_page,
        'create_meeting': create_meeting_page,
        'user_profile': user_profile_page
    }
    start_server(routes, port=5000, debug=True)
