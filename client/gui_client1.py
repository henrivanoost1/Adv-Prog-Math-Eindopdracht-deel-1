import os
import json
import logging
import socket
from tkinter import *
from tkinter import messagebox


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
        self.makeConnnectionWithServer()

    # Creation of init_window

    def init_window(self):
        global main_screen
        main_screen = Toplevel(self.master)
        main_screen.geometry("300x250")
        main_screen.title("Account Login")
        Label(main_screen, text="Select Your Choice", width="300",
              height="2", font=("Calibri", 13)).pack()
        Label(main_screen, text="").pack()
        Button(main_screen, text="Login", height="2",
               width="30", command=self.login).pack()
        Label(main_screen, text="").pack()
        Button(main_screen, text="Register", height="2",
               width="30", command=self.register).pack()

        # main_screen.mainloop()

    def login(self):
        global login_screen
        login_screen = Toplevel(self.master)
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
        username_login_entry = Entry(
            login_screen, textvariable=username_verify)
        username_login_entry.pack()
        Label(login_screen, text="").pack()
        Label(login_screen, text="Emailadres * ").pack()
        mail_login_entry = Entry(login_screen, textvariable=mail_verify)
        mail_login_entry.pack()
        Label(login_screen, text="").pack()
        Button(login_screen, text="Login", width=10,
               height=1, command=self.login_verify).pack()

        # Implementing event on register button

    def register(self):
        global register_screen
        register_screen = Toplevel(self.master)
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
               height=1, command=self.register_user).pack()

    def form(self):
        global form_screen
        form_screen = Toplevel(self.master)
        form_screen.title("Form")
        form_screen.geometry("300x250")

        Label(form_screen, text="Please choose a question").pack()
        Label(form_screen, text="").pack()

        Button(form_screen, text="Question 1",
               width=10, height=1, command=self.form1).pack()
        Label(form_screen, text="").pack()
        Button(form_screen, text="Question 2",
               width=10, height=1).pack()
        Label(form_screen, text="").pack()
        Button(form_screen, text="Question 3",
               width=10, height=1).pack()
        Label(form_screen, text="").pack()

    def form1(self):

        # The Toplevel widget work pretty much like Frame,
        # but it is displayed in a separate, top-level window.
        # Such windows usually have title bars, borders, and other “window decorations”.
        # And in argument we have to pass global screen variable

        form1_screen = Toplevel(form_screen)
        form1_screen.title("form1")
        form1_screen.geometry("300x250")

        # Set text variables
        global ageParam
        ageParam = IntVar()
        gender = StringVar()
        # Set label for user's instruction
        Label(form1_screen, text="Please enter details below").pack()
        Label(form1_screen, text="").pack()

        # Set age label
        name_lable = Label(form1_screen, text="Age")
        name_lable.pack()

        # Set age entry
        # The Entry widget is a standard Tkinter widget used to enter or display a single line of text.

        name_entry = Entry(form1_screen, textvariable=ageParam)
        name_entry.pack()
        Label(form1_screen, text="").pack()

        # # Set gender label
        # gender_lable = Label(form1_screen, text="Gender")
        # gender_lable.pack()

        # # Set gender entry
        # # The Entry widget is a standard Tkinter widget used to enter or display a single line of text.

        # gender_radio1 = Radiobutton(
        #     form1_screen, text="Male", variable=gender, value="male")
        # gender_radio1.pack()

        # gender_radio2 = Radiobutton(
        #     form1_screen, text="Female", variable=gender, value="female")
        # gender_radio2.pack()

        # gender_radio3 = Radiobutton(
        #     form1_screen, text="Other", variable=gender, value="other")
        # gender_radio3.pack()

        # Label(form1_screen, text="").pack()

        # Set register button
        Button(form1_screen, text="Search", width=10,
               height=1, command=self.get_parameters).pack()

    def get_parameters(self):
        try:
            age1 = ageParam.get()
            msg = "Get parameters"

            self.my_writer_obj.write("Verifying\n")
            self.my_writer_obj.write(f"{msg}\n")
            logging.info(f"Sending message: {msg}")
            self.my_writer_obj.write("%s\n" % age1)
            logging.info(f"Sending age: {age1}")
            self.my_writer_obj.flush()
        except Exception as ex:
            logging.error(f"Foutmelding: {ex}")
            messagebox.showinfo("Getting parameters",
                                "Something has gone wrong...")

    def login_verify(self):

        try:
            username1 = username_verify.get()
            mail1 = mail_verify.get()
            msg = "Verify"

            self.my_writer_obj.write("Verifying\n")
            self.my_writer_obj.write(f"{msg}\n")
            logging.info(f"Sending message: {msg}")
            self.my_writer_obj.write("%s\n" % username1)
            logging.info(f"Sending username: {username1}")
            self.my_writer_obj.write("%s\n" % mail1)
            logging.info(f"Sending mail: {mail1}")
            self.my_writer_obj.flush()

            # waiting for answer
            answer = self.my_writer_obj.readline().rstrip('\n')
            logging.info(f"Answer server: {answer}")

            if answer == '1':
                self.login_sucess()
            elif answer == '2':
                self.password_not_recognised()
            elif answer == '3':
                self.user_not_found()

        except Exception as ex:
            logging.error(f"Foutmelding: {ex}")
            messagebox.showinfo("Verifying", "Something has gone wrong...")

    def register_user(self):

        name_info = name.get()
        username_info = username.get()
        mail_info = mail.get()
        status = 0
        msg = "Register"

        self.my_writer_obj.write("Registering\n")

        self.my_writer_obj.write(f"{msg}\n")
        logging.info(f"Sending Message: {msg}")
        self.my_writer_obj.write("%s\n" % name_info)
        logging.info(f"Sending name: {name_info}")
        self.my_writer_obj.write("%s\n" % username_info)
        logging.info(f"Sending username: {username_info}")
        self.my_writer_obj.write("%s\n" % mail_info)
        logging.info(f"Sending mail: {mail_info}")
        self.my_writer_obj.write("%s\n" % status)
        logging.info(f"Sending status: {status}")

        self.my_writer_obj.flush()
        # function to add to JSON

        name_entry.delete(0, END)
        username_entry.delete(0, END)
        emailadres_entry.delete(0, END)

        Label(register_screen, text="Registration Success",
              fg="green", font=("calibri", 11)).pack()
        register_screen.after(1000, register_screen.destroy)
        self.login()

    def login_sucess(self):
        # global login_success_screen
        # login_success_screen = Toplevel(login_screen)
        # login_success_screen.title("Success")
        # login_success_screen.geometry("150x100")
        # Label(login_success_screen, text="Login Success").pack()
        # Button(login_success_screen, text="OK",
        #        command=self.delete_login_success).pack()
        Label(login_screen, text="Login Success",
              fg="green", font=("calibri", 11)).pack()
        Label(login_screen, text="Please wait until this window closes",
              fg="black", font=("calibri", 11)).pack()
        login_screen.after(1000, login_screen.destroy)
        main_screen.after(1000, main_screen.destroy)
        self.form()

    # Designing popup for login invalid password

    def password_not_recognised(self):
        global password_not_recog_screen
        password_not_recog_screen = Toplevel(login_screen)
        password_not_recog_screen.title("Success")
        password_not_recog_screen.geometry("150x100")
        Label(password_not_recog_screen, text="Invalid combination ").pack()
        Button(password_not_recog_screen, text="OK",
               command=self.delete_password_not_recognised).pack()

    # Designing popup for user not found

    def user_not_found(self):
        global user_not_found_screen
        user_not_found_screen = Toplevel(login_screen)
        user_not_found_screen.title("Success")
        user_not_found_screen.geometry("150x100")
        Label(user_not_found_screen, text="User Not Found").pack()
        Button(user_not_found_screen, text="OK",
               command=self.delete_user_not_found_screen).pack()

    # Deleting popups

    def delete_login_success(self):
        # login_success_screen.destroy()
        pass

    def delete_password_not_recognised(self):
        password_not_recog_screen.destroy()

    def delete_user_not_found_screen(self):
        user_not_found_screen.destroy()

    def __del__(self):
        self.close_connection()

    def makeConnnectionWithServer(self):
        try:
            logging.info("Making connection with server...")
            # get local machine name
            host = socket.gethostname()
            port = 9999
            self.socket_to_server = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
            # connection to hostname on the port.
            self.socket_to_server.connect((host, port))
            self.my_writer_obj = self.socket_to_server.makefile(mode='rw')
            logging.info("Open connection with server succesfully")
        except Exception as ex:
            logging.error(f"Foutmelding: {ex}")

    def close_connection(self):
        try:
            logging.info("Close connection with server...")
            self.my_writer_obj.write("CLOSE\n")
            self.my_writer_obj.flush()
            self.socket_to_server.close()
        except Exception as ex:
            logging.error(f"Foutmelding: {ex}")
            messagebox.showinfo("Sommen", "Something has gone wrong...")


logging.basicConfig(level=logging.INFO)

root = Tk()
# root.geometry("400x300")
app = Window(root)
root.mainloop()
