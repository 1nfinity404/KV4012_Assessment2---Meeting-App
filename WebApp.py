#name = "James Huang"
#student number = "24001207"

from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
#from datetime import datetime
import re
import Classes as Class
import NavBar as nav

navbar = """
<ul class="nav justify-content-center bg-primary fixed-top border border-black nav-fill">
    <li class="nav-item border border-black">
        <a class="nav-link" aria-current="page" href="?app=tutor_meeting">
           tutor
        </a>
    </li>
    <li class="nav-item border border-black">
        <a class="nav-link" href="?app=tutor_meeting">
           tutor
        </a>
    </li>
    <li class="nav-item border border-black">
        <a class="nav-link" href="?app=tutor_meeting">
          tutor
        </a>
    </li>
</ul>
"""

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

user = Class.User("name", 12345678, "00/00/0000", "something@email.com", "username", "password")
user_database_extract = []
user_extract = []
username_remind = ""

# Login user page
def user_login_page():
    clear()
    global user
    global username_remind

    put_html("<h1 class='text-center'>Log In</h1>")

    link("?app=password_reset", "Forgot Password?")
    link("?app=register", "Register")

    user_login = input_group('', [
        input("Username", name="username", required=True),
        input("Password", name="password", required=True, type=PASSWORD)
    ])

    username_remind = user_login["username"]

    if user.username == user_login["username"] and user.password == user_login["password"]:
        toast(f"Welcome, {user.username}", 5)
    elif user.username != user_login["username"] and user.password != user_login["password"]:
        with open("user_database.txt", "r") as file:
            user_database_extract = f"{file.readline()}"
            user_database_extract.removesuffix(",")
            user_database_extract.split(",")
            for user_info in user_database_extract:
                if f"{user_login["username"]}" in user_info and f"{user_login["password"]}" in user_info:
                    user_extract = user_info
                    user_extract.split("#")
                    user.name = user_extract[0]
                    user.student_id = user_extract[1]
                    user.date_of_birth = user_extract[2]
                    user.email_address = user_extract[3]
                    user.username = user_extract[4]
                    user.password = user_extract[5]
                    toast(f"Welcome, {user.username}", 5)
                    tutor_meeting_page()
            tutor_meeting_page()

# Password reset page
def password_reset_page():
    clear()
    global user
    global user_extract

    put_html("<h1 class='text-center'>Password Reset</h1>")

    password_reset = input_group('', [
        input("New Password", name="new_password", required=True, type=PASSWORD),
        input("Confirm Password", name="confirm_password", required=True, type=PASSWORD)
    ])
    if 5 > len(password_reset["new_password"]) > 15:
        toast("Your new password is too short or long!", 5)
        password_reset_page()
    elif password_reset["new_password"] == password_reset["confirm_password"]:
        with open("user_database.txt", "r") as file:
            user_database_extract = f"{file.readline()}"
            user_database_extract.removesuffix(",")
            user_database_extract.split(",")
            for user_info in user_database_extract:
                if username_remind in user_database_extract:
                    user_extract = user_info
                    user_extract.split("#")
                    user.name = user_extract[0]
                    user.student_id = user_extract[1]
                    user.date_of_birth = user_extract[2]
                    user.email_address = user_extract[3]
                    user.username = user_extract[4]
                    user.password = password_reset["new_password"]
                    user_database_extract.replace(f"{user_info}", f",{user},")
                    toast("Password Has Been Reset")
                    register_page()
    else:
        toast("Password Error", 5)

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
    #elif "#" in user_register["name"] or "#" in user_register["password"]:
        #toast("Your username and password should not contain #!", 5)
        #register_page()
    else:
        user = Class.User(user_register['name'], user_register["student_id"], user_register['dob'],
                          user_register['email'], user_register['username'], user_register['password'])
        with open("user_database.txt", "a") as file:
            file.write(f"{user},")
        toast("Account created!", 5)
        user_login_page()

# tutor meeting page
def tutor_meeting_page():
    clear()
    nav.navbar("?app=user_profile", "Profile", "?app=notifications", "Notifications", "?app=tutors", "Tutors")
    put_html("<h1 class='text-center'>Tutor Meetings</h1>")

    put_link("Add New Meeting","?app=create_meeting")


# notification page
def notifications_page():
    clear()
    nav.navbar("?app=user_profile", "Profile", "?app=tutor_meeting", "Meetings", "?app=tutors", "Tutors")
    put_html("<h1 class='text-center'>Notifications</h1>")

    notification_show = input_group('', [
        input("Notification 1", name="notification1", required=True),
        input("Notification 2", name="notification2", required=True),
        input("Notification 3", name="notification3", required=True),
        input("Notification 4", name="notification4", required=True),
    ])

# tutors' page
def tutors_page():
    clear()
    nav.navbar("?app=user_profile", "Profile", "?app=tutor_meeting", "Meetings", "?app=notifications", "Notifications")
    put_html("<h1 class='text-center'>Tutors</h1>")

    tutor_list_html = f"""
        <table class="table text-center text-primary">
            <thead>
                <tr>
                    <th scope="col">
                        <svg xmlns="http://www.w3.org/2000/svg" width="80" height="80" fill="currentColor"
                            class="bi bi-circle"
                            viewBox="0 0 16 16">
                            <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/>
                        </svg>
                    </th>
                    <th scope="col">
                        {put_link("Tutor 1", "?app=tutor_profile")}
                    </th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>
                        <svg xmlns="http://www.w3.org/2000/svg" width="80" height="80" fill="currentColor"
                            class="bi bi-circle"
                            viewBox="0 0 16 16">
                            <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/>
                        </svg>
                    </td>
                    <td>{put_link("Tutor 2", "?app=tutor_profile")}</td>
                </tr>
                <tr>
                    <td>
                        <svg xmlns="http://www.w3.org/2000/svg" width="80" height="80" fill="currentColor"
                            class="bi bi-circle"
                            viewBox="0 0 16 16">
                            <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/>
                        </svg>
                    </td>
                    <td>{put_link("Tutor 3", "?app=tutor_profile")}</td>
                </tr>
                <tr>
                    <td>
                        <svg xmlns="http://www.w3.org/2000/svg" width="80" height="80" fill="currentColor"
                            class="bi bi-circle"
                            viewBox="0 0 16 16">
                            <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/>
                        </svg>
                    </td>
                    <td>{put_link("Tutor 4", "?app=tutor_profile")}</td>
                </tr>
                <tr>
                    <td>
                        <svg xmlns="http://www.w3.org/2000/svg" width="80" height="80" fill="currentColor"
                            class="bi bi-circle"
                            viewBox="0 0 16 16">
                            <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/>
                        </svg>
                    </td>
                    <td>{put_link("Tutor 5", "?app=tutor_profile")}</td>
                </tr>
                <tr>
                    <td>
                        <svg xmlns="http://www.w3.org/2000/svg" width="80" height="80" fill="currentColor"
                            class="bi bi-circle"
                            viewBox="0 0 16 16">
                            <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/>
                        </svg>
                    </td>
                    <td>{put_link("Tutor 6", "?app=tutor_profile")}</td>
                </tr>
            <tbody>
        </table>
    """
    put_html(tutor_list_html)


# tutor profile page
def tutor_profile_page():
    clear()
    put_html("<a class='btn btn-primary' href='?app=tutors' role='button'>Back</a>")

    put_html("<h1 class='text-center'>Profile</h1>")

    tutor_profile = f"""
            <div class="jumbotron text-center bg-white py-3">
                <div class="container">
                    <svg xmlns="http://www.w3.org/2000/svg" width="80" height="80" fill="currentColor"
                        class="bi bi-circle"
                        viewBox="0 0 16 16">
                        <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/>
                    </svg>
                </div>
                <div class = "container">
                    Name
                    Office Location
                    Email
                    Drop-in hours
                </div>
            </div>
            """
    put_html(tutor_profile)

# page for creating meeting
def create_meeting_page():
    clear()
    put_html("<h1 class ='text-center'>Create New Meeting</h1>")
    meeting_create = input_group('', [
        input("Meeting Title", name="meeting_title", required=True),
        input("Tutor Name", name="tutor_name", required=True),
        input("Meeting Description", name="meeting_info", required=True)
        ])
    tutor_meeting_page()

# User Profile Page
def user_profile_page():
    clear()
    nav.navbar("?app=tutor_meeting", "Meetings", "?app=notifications", "Notifications", "?app=tutors", "Tutors")
    put_html("<h1 class ='text-center'>Profile</h1>")

    user_profile = f"""
    <div class="jumbotron text-center bg-white py-3">
        <div class="container">
            <svg xmlns="http://www.w3.org/2000/svg" width="80" height="80" fill="currentColor"
                class="bi bi-circle"
                viewBox="0 0 16 16">
                <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/>
            </svg>
        </div>
        <div class = "container">
            {user.name}
            {user.date_of_birth}
            {user.student_id}
            {user.email_address}
            Level
        </div>
    </div>
    """
    put_html(user_profile)

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
