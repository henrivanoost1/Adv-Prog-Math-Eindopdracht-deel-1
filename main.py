from tkinter import *


def main_account_screen():
    global main_screen
    main_screen = Tk()   # create a GUI window
    main_screen.geometry("300x250")  # set the configuration of GUI window
    main_screen.title("Account Login")  # set the title of GUI window

    # create a Form label
    Label(text="Choose Login Or Register",  width="300",
          height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()

    # create Login Button
    Button(text="Login", height="2", width="30").pack()
    Label(text="").pack()

    # create a register button
    Button(text="Register", height="2", width="30", command=register).pack()

    main_screen.mainloop()  # start the GUI


def register():

    # The Toplevel widget work pretty much like Frame,
    # but it is displayed in a separate, top-level window.
    # Such windows usually have title bars, borders, and other “window decorations”.
    # And in argument we have to pass global screen variable

    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")

    # Set text variables
    name = StringVar()
    username = StringVar()
    mail = StringVar()

    # Set label for user's instruction
    Label(register_screen, text="Please enter details below").pack()
    Label(register_screen, text="").pack()

    # Set name label
    name_lable = Label(register_screen, text="Name")
    name_lable.pack()

    # Set name entry
    # The Entry widget is a standard Tkinter widget used to enter or display a single line of text.

    name_entry = Entry(register_screen, textvariable=name)
    name_entry.pack()

    # Set username label
    username_lable = Label(register_screen, text="Username")
    username_lable.pack()

    # Set username entry
    # The Entry widget is a standard Tkinter widget used to enter or display a single line of text.

    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()

    # Set emailadres label
    emailadres_lable = Label(register_screen, text="Emailadres")
    emailadres_lable.pack()

    # S t emailadres entry
    emailadres_entry = Entry(register_screen, textvariable=mail)
    emailadres_entry.pack()

    Label(register_screen, text="").pack()

    # Set register button
    Button(register_screen, text="Register", width=10, height=1).pack()


main_account_screen()  # call the main_account_screen() function



