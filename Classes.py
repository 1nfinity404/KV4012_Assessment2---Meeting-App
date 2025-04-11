class User:
    name = ""
    student_id = None
    date_of_birth = None
    email_address = None
    username = None
    password = None

    def __init__(self, name, student_id, dob, email, username, password):
        self.name = name
        self.student_id = str(student_id)
        self.date_of_birth = dob
        self.email_address = email
        self.username = username
        self.password = password

    def __str__(self):
        return f"{self.name}#{self.student_id}#{self.date_of_birth}#{self.email_address}#{self.username}#{self.password}"