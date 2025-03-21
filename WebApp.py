from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
from datetime import datetime

def log_in_page():
    put_html("<h1 class = text-center>Log In</h1>")

    log_account = input_group('', [
        input("Username", name="name", required=True),
        input("Password", name="password", required=True, type= PASSWORD)
    ], )

    put_html("<h2 class = text-center>For Password?</h2>")
    put_html("<h2 class = text-center>Register</h2>")

def password_reset_page():
    put_html("<h1 class = text-center>Password Reset</h1>")

def register_page():
    put_html("<h1 class = text-center>Register</h1>")


log_in_page()