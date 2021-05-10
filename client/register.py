# https://pythonprogramming.net/python-3-tkinter-basics-tutorial/
from tkinter import *
from tkinter import messagebox
import os
import json


class Registerframe(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
        self.bmi = 0

    # Creation of init_window
    def init_window(self):
        # changing the title of our master widget
        self.master.title("Register")
        # self.master.geometry("400x300")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        Label(self, text="Name:").grid(row=0)
        Label(self, text="Username:").grid(row=1)
        Label(self, text="Mail:", pady=10).grid(row=2)

        self.entry_name = Entry(self, width=40)
        self.entry_username = Entry(
            self, width=40)
        self.entry_mail = Entry(self, width=40)
        self.entry_name.grid(row=0, column=1,)
        self.entry_username.grid(row=1, column=1,)
        self.entry_mail.grid(row=2, column=1,)

        self.buttonCalculate = Button(
            self, text="Register", command=self.login)
        self.buttonCalculate.grid(row=3, column=0, columnspan=1, pady=(
            0, 5), padx=(5, 5), )
        self.buttonReturn = Button(self, text="Return", command=lambda: self.master.switch_frame(
            "start", f"BMI: {self.bmi:.2f}"))
        self.buttonReturn.grid(row=3, column=1, columnspan=4, pady=(
            0, 5), padx=(5, 5), )

        Grid.rowconfigure(self, 2, weight=1)
        Grid.columnconfigure(self, 1, weight=1)

    def login(self):
        try:
            username1 = self.entry_username.get()
            mail1 = self.entry_mail.get()
            print(username1)
            print(mail1)
            # self.entry_username.delete(0, END)
            # self.entry_mail.delete(0, END)

            database = "data\data.json"
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

            print(user_info)

            if username1 in user_info:
                if mail1 == user_info[2]:
                    self.master.switch_frame("main")

                else:
                    messagebox.showerror("Fail", "Invalid combination")
            else:
                messagebox.showerror("Fail", "User not found")

        except:
            messagebox.showerror("Fail", "Something has gone wrong...")
