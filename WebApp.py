from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
from datetime import datetime

put_html("<h1 class = text-center>Log In</h1>")

log_account = input_group('',[
    input("Enter your username: ", name="name", required=True),
    input("Enter your password: ", name="password", required=True, type=PASSWORD)
])