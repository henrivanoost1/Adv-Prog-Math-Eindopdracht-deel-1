from tkinter import *
import os
import json

# Designing window for registration


def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")

    global name
    global username
    global mail
    global name_entry
    global username_entry
    global emailadres_entry

    # Set text variables
    name = StringVar()
    username = StringVar()
    mail = StringVar()

    # Set label for user's instruction
    Label(register_screen, text="Please enter details below").pack()
    Label(register_screen, text="").pack()

    # Set name label
    name_lable = Label(register_screen, text="Name *")
    name_lable.pack()

    # Set name entry
    # The Entry widget is a standard Tkinter widget used to enter or display a single line of text.

    name_entry = Entry(register_screen, textvariable=name)
    name_entry.pack()

    # Set username label
    username_lable = Label(register_screen, text="Username *")
    username_lable.pack()

    # Set username entry
    # The Entry widget is a standard Tkinter widget used to enter or display a single line of text.

    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()

    # Set emailadres label
    emailadres_lable = Label(register_screen, text="Emailadres *")
    emailadres_lable.pack()

    # S t emailadres entry
    emailadres_entry = Entry(register_screen, textvariable=mail)
    emailadres_entry.pack()

    Label(register_screen, text="").pack()

    # Set register button
    Button(register_screen, text="Register", width=10,
           height=1, command=register_user).pack()


# Designing window for login

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global mail_verify

    username_verify = StringVar()
    mail_verify = StringVar()

    global username_login_entry
    global mail_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Emailadres * ").pack()
    mail_login_entry = Entry(login_screen, textvariable=mail_verify)
    mail_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10,
           height=1, command=login_verify).pack()

# Implementing event on register button


def register_user():

    name_info = name.get()
    username_info = username.get()
    mail_info = mail.get()

    # function to add to JSON

    def write_json(data, filename='client\data.json'):
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    with open('client\data.json') as json_file:
        data = json.load(json_file)

        temp = data['user_info']

        # python object to be appended
        y = {"name": name_info,
             "username": username_info,
             "mail": mail_info
             }

        # appending data to emp_details
        temp.append(y)

    write_json(data)

    name_entry.delete(0, END)
    username_entry.delete(0, END)
    emailadres_entry.delete(0, END)

    Label(register_screen, text="Registration Success",
          fg="green", font=("calibri", 11)).pack()


# Implementing event on login button

def login_verify():
    username1 = username_verify.get()
    mail1 = mail_verify.get()
    username_login_entry.delete(0, END)
    mail_login_entry.delete(0, END)

    database = "client\data.json"
    data = json.loads(open(database).read())
    user_data = data['user_info']

    user_info = []
    for i in user_data:

        if username1 == i['username']:

            user_info.append(i['name'])
            user_info.append(i['username'])
            user_info.append(i['mail'])

        else:
            pass

    if username1 in user_info:
        if mail1 == user_info[2]:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()

    user_info.clear()

# Designing popup for login success


def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK",
           command=delete_login_success).pack()

# Designing popup for login invalid password


def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid combination ").pack()
    Button(password_not_recog_screen, text="OK",
           command=delete_password_not_recognised).pack()

# Designing popup for user not found


def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK",
           command=delete_user_not_found_screen).pack()

# Deleting popups


def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


# Designing Main(first) window

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", width="300",
          height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()

    main_screen.mainloop()


main_account_screen()
