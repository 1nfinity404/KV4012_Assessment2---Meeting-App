from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
from datetime import datetime

def link(url, name):
    put_html(f"<div style='text-align:center;'><a href={url}>{name}</a></div>")

def user_login_page():
    clear()
    put_html("<h1 class='text-center'>Log In</h1>")

    link("?app=password_reset", "Forgot Password?")
    link("?app=register", "Register")

    input_group('', [
        input("Username", name="name", required=True),
        input("Password", name="password", required=True, type=PASSWORD)
    ])


def password_reset_page():
    clear()
    put_html("<h1 class='text-center'>Password Reset</h1>")

    input_group('', [
        input("New Password", name="new_password", required=True, type=PASSWORD),
        input("Confirm Password", name="confirm_password", required=True, type=PASSWORD)
    ])

def register_page():
    clear()
    put_html("<h1 class='text-center'>Register</h1>")

    input_group('', [
        input("Enter Username", name="name", required=True),
        input("Student ID", name="student_id", required=True,),
        input("Date of Birth", name="date_of_birth", required=True,),
        input("Email address", name="email", required=True,)
    ])

def tutor_meeting_page():
    clear()
    put_html("<h1 class='text-center'>Tutor Meetings</h1>")

def notifications_page():
    clear()
    put_html("<h1 class='text-center'>Notifications</h1>")

def tutors_page():
    clear()
    put_html("<h1 class='text-center'>Tutors</h1>")

def tutor_profile_page():
    clear()
    put_html("<a class='btn btn-primary' href='?app=tutors' role='button'>Back</a>")

    put_html("<h1 class='text-center'>Profile</h1>")

def create_meeting_page():
    clear()
    put_html("<h1 class ='text-center'>Create New Meeting</h1>")

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