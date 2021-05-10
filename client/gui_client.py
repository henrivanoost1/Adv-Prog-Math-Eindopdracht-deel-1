import logging
import socket
import pickle
from tkinter import *
from tkinter import messagebox
from login import Loginframe
from register import Registerframe
from main import Mainframe


class StartApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.switch_frame("start")
        self.makeConnnectionWithServer()

    # we switchen tss 3 frames: startframe <> bmiframe, startframe <> numbersframe

    def switch_frame(self, name_class, result=""):
        """Destroys current frame and replaces it with a new one."""
        if self._frame is not None:
            self._frame.destroy()

        if name_class == "start":
            new_frame = StartFrame(self, result)
        elif name_class == "login":
            new_frame = Loginframe(self)
        elif name_class == "register":
            new_frame = Registerframe(self)
        elif name_class == "main":
            new_frame = Mainframe(self)

        if new_frame is not None:
            self._frame = new_frame
            self._frame.pack()

    def __del__(self):
        self.close_connection()

    def makeConnnectionWithServer(self):
        try:
            logging.info("Making connection with server...")
            # get local machine name
            host = socket.gethostname()
            port = 9999
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # connection to hostname on the port.
            self.s.connect((host, port))

            self.in_out_server = self.s.makefile(mode='rwb')
            logging.info("Open connection with server succesfully")
        except Exception as ex:
            logging.error("Foutmelding: %s" % str(ex))
            messagebox.showinfo("Connection - foutmelding",
                                "Something has gone wrong...")

    def close_connection(self):
        try:
            logging.info("Close connection with server...")
            pickle.dump("CLOSE", self.in_out_server)
            self.in_out_server.flush()
            self.s.close()
        except Exception as ex:
            logging.error("Foutmelding:close connection with server failed")


class StartFrame(Frame):
    def __init__(self, master, result=""):
        Frame.__init__(self, master)
        self.master.title("Heartstroke Dataset")
        self.pack(fill=BOTH, expand=1)
        Label(self, text="This is the login page").pack(
            side="top", fill="x", pady=10)
        Button(self, text="Login",
               command=lambda: master.switch_frame("login")).pack()
        Button(self, text="Register",
               command=lambda: master.switch_frame("register")).pack()


logging.basicConfig(level=logging.INFO)

root = StartApp()
root.mainloop()
