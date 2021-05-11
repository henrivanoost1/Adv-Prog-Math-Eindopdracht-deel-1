import logging
import socket
from queue import Queue
from threading import Thread
from tkinter import *
import json

from myserver import TaskServer


class ServerWindow(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
        self.init_messages_queue()
        self.init_server()

    # Creation of init_window

    def init_window(self):
        # changing the title of our master widget
        self.master.title("Server")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        Label(self, text="Log-berichten server:").grid(row=0)
        self.scrollbar = Scrollbar(self, orient=VERTICAL)
        self.lstnumbers = Listbox(self, yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.lstnumbers.yview)

        self.lstnumbers.grid(row=1, column=0, sticky=N + S + E + W)
        self.scrollbar.grid(row=1, column=1, sticky=N + S)

        self.btn_text = StringVar()
        self.btn_text.set("Start server")
        self.buttonServer = Button(
            self, textvariable=self.btn_text, command=self.start_stop_server)
        self.buttonServer.grid(row=3, column=0, columnspan=2, pady=(
            5, 5), padx=(5, 5), sticky=N + S + E + W)

        Label(self, text="Populaire zoekopdrachten:").grid(row=5)
        self.scrollbar1 = Scrollbar(self, orient=VERTICAL)
        self.lstpopular = Listbox(self, yscrollcommand=self.scrollbar1.set)
        self.scrollbar1.config(command=self.lstpopular.yview)

        self.lstpopular.grid(row=6, column=0, sticky=N + S + E + W)
        self.scrollbar1.grid(row=6, column=1, sticky=N + S)

        Label(self, text="Gegevens gebruikers:").grid(row=8)
        self.scrollbar2 = Scrollbar(self, orient=VERTICAL)
        self.lstdata = Listbox(self, yscrollcommand=self.scrollbar2.set)
        self.scrollbar2.config(command=self.lstdata.yview)

        self.lstdata.grid(row=9, column=0, sticky=N + S + E + W)
        self.scrollbar2.grid(row=9, column=1, sticky=N + S)

        Label(self, text="Online gebruikers:").grid(row=10)
        self.scrollbar3 = Scrollbar(self, orient=VERTICAL)
        self.lstonline = Listbox(self, yscrollcommand=self.scrollbar3.set)
        self.scrollbar3.config(command=self.lstonline.yview)

        self.lstonline.grid(row=11, column=0, sticky=N + S + E + W)
        self.scrollbar3.grid(row=11, column=1, sticky=N + S)
        # self.buttonMessage = Button(
        #     self, textvariable="Send Message", command=self.start_stop_server)
        # self.buttonServer.grid(row=3, column=0, columnspan=2, pady=(
        #     5, 5), padx=(5, 5), sticky=N + S + E + W)

        # Label(self, text="Zoekopdrachten per client:").grid(row=12)
        # self.scrollbar4 = Scrollbar(self, orient=VERTICAL)
        # self.lstsearch = Listbox(self, yscrollcommand=self.scrollbar4.set)
        # self.scrollbar4.config(command=self.lstsearch.yview)

        # self.lstsearch.grid(row=13, column=0)
        # self.scrollbar4.grid(row=13, column=1, sticky=N + S)

        # self.btn_text1 = StringVar()
        # self.btn_text.set("Start server")
        # self.buttonServer = Button(
        #     self, textvariable=self.btn_text, command=self.start_stop_server)
        # self.buttonServer.grid(row=3, column=0, columnspan=2, pady=(
        #     5, 5), padx=(5, 5), sticky=N + S + E + W)

        Grid.rowconfigure(self, 1, weight=1)
        Grid.columnconfigure(self, 0, weight=1)

    def init_server(self):
        # server - init
        self.server = TaskServer(
            socket.gethostname(), 9999, self.messages_queue)

    def afsluiten_server(self):
        if self.server != None:
            self.server.close_server_socket()
        # del (self.messages_queue)

    def print_messsages_from_queue(self):
        message = self.messages_queue.get()
        while message != "CLOSE_SERVER":
            if "SERVER STARTED" in message:
                self.lstnumbers.insert(END, message)
                self.get_data_users()
                self.messages_queue.task_done()
                message = self.messages_queue.get()

            elif "Got a connection from " in message:
                self.lstnumbers.insert(END, message)
                self.get_online_users()
                self.messages_queue.task_done()
                message = self.messages_queue.get()

            elif "Sending verification 1 back" in message:
                self.lstnumbers.insert(END, message)
                self.get_online_users()
                self.messages_queue.task_done()
                message = self.messages_queue.get()

            elif "log out succes" in message:
                self.lstnumbers.insert(END, message)
                self.get_online_users()
                self.messages_queue.task_done()
                message = self.messages_queue.get()

            else:
                self.lstnumbers.insert(END, message)
                self.messages_queue.task_done()
                message = self.messages_queue.get()

        print("queue stop")

    # def print_messsages_from_queue(self):
    #     message = self.messages_queue.get()
    #     counterParameter = 0
    #     counterGender = 0
    #     counterHeart = 0
    #     counterStatistics = 0
    #     # Parameter=""
    #     # Gender=""
    #     # Heart=""
    #     # Statistics=""
    #     while message != "CLOSE_SERVER":
    #         if "Got a connection from " in message:
    #             self.lstnumbers.insert(END, message)

    #         elif "CLH :> Most requested data: " in message:
    #             self.lstnumbers.insert(END, message)
    #             if "CLH :> Most requested data: parameter age" in message:
    #                 counterParameter = counterParameter+1
    #                 Parameter = ""
    #                 Parameter = f'Parameter age werd {str(counterParameter)} gevraagd'

    #             elif "CLH :> Most requested data: gender graph" in message:
    #                 counterGender = counterGender+1
    #                 Gender = ""
    #                 Gender = f'Grafiek Gender werd {str(counterGender)} gevraagd'

    #             elif "CLH :> Most requested data: heart disease graph" in message:
    #                 counterHeart = counterHeart+1
    #                 Heart = ""
    #                 Heart = f'Grafiek Hartaandoening werd {str(counterHeart)} gevraagd'

    #             elif "CLH :> Most requested data: statistics" in message:
    #                 counterStatistics = counterStatistics+1
    #                 Statistics = ""
    #                 Statistics = f'Statistische data werd {str(counterStatistics)} gevraagd'

    #             self.lstpopular.delete(0, END)
    #             self.lstpopular.insert(END, Parameter)
    #             self.lstpopular.insert(END, Gender)
    #             self.lstpopular.insert(END, Heart)
    #             self.lstpopular.insert(END, Statistics)
    #             # self.messages_queue.task_done()
    #             # message = self.messages_queue.get()

    #         else:
    #             self.lstnumbers.insert(END, message)

    #         self.messages_queue.task_done()
    #         message = self.messages_queue.get()
    #     print("queue stop")

    def init_messages_queue(self):
        self.messages_queue = Queue()
        t = Thread(target=self.print_messsages_from_queue)
        t.start()

    def get_users(self):
        with open('./data/data.json', 'r') as json_users:
            data = json_users.read()

        users = json.loads(data)

        return users

    def get_online_users(self):
        users = self.get_users()
        online_users = []

        for user in users['user_info']:
            if int(user['status']) == 1:
                online_users.append(user['name'])

            elif int(user['status']) != 1 and user['name'] in online_users:
                online_users.remove(user['name'])

        self.lstonline.insert(
            END, 'Online Users : ' + str(online_users))
        self.lstnumbers.insert(END, 'Online Users : ' + str(online_users))

    def get_data_users(self):
        users = self.get_users()
        clients = []
        # name_online_user

        for user in users['user_info']:
            clients.append(user['name'])

            name_user = user["name"]
            username_user = user["username"]
            mail_user = user["mail"]

            self.lstdata.insert(
                END, "Naam: " + str(name_user) + "     Username: " + username_user + "     Email: " + mail_user)

    def start_stop_server(self):
        if self.server.is_connected == True:
            self.server.close_server_socket()
            self.btn_text.set("Start server")
        else:
            self.server.init_server()
            self.server.start()  # thread!
            self.btn_text.set("Stop server")
