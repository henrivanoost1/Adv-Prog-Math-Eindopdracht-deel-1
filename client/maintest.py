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
    global register_screen
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
    Button(register_screen, text="Register",
           width=10, height=1, command=form).pack()


def form():
    global form_screen
    form_screen = Toplevel(register_screen)
    form_screen.title("Form")
    form_screen.geometry("300x250")

    Label(form_screen, text="Please choose a question").pack()
    Label(form_screen, text="").pack()

    Button(form_screen, text="Question 1",
           width=10, height=1, command=form1).pack()
    Label(form_screen, text="").pack()
    Button(form_screen, text="Question 2",
           width=10, height=1, command=form2).pack()
    Label(form_screen, text="").pack()
    Button(form_screen, text="Question 3",
           width=10, height=1, command=form3).pack()
    Label(form_screen, text="").pack()


def form1():

    # The Toplevel widget work pretty much like Frame,
    # but it is displayed in a separate, top-level window.
    # Such windows usually have title bars, borders, and other “window decorations”.
    # And in argument we have to pass global screen variable

    form1_screen = Toplevel(form_screen)
    form1_screen.title("form1")
    form1_screen.geometry("300x250")

    # Set text variables
    age = IntVar()
    gender = StringVar()
    # Set label for user's instruction
    Label(form1_screen, text="Please enter details below").pack()
    Label(form1_screen, text="").pack()

    # Set age label
    name_lable = Label(form1_screen, text="Age")
    name_lable.pack()

    # Set age entry
    # The Entry widget is a standard Tkinter widget used to enter or display a single line of text.

    name_entry = Entry(form1_screen, textvariable=age)
    name_entry.pack()
    Label(form1_screen, text="").pack()

    # Set gender label
    gender_lable = Label(form1_screen, text="Gender")
    gender_lable.pack()

    # Set gender entry
    # The Entry widget is a standard Tkinter widget used to enter or display a single line of text.

    gender_radio1 = Radiobutton(
        form1_screen, text="Male", variable=gender, value="male")
    gender_radio1.pack()

    gender_radio2 = Radiobutton(
        form1_screen, text="Female", variable=gender, value="female")
    gender_radio2.pack()

    gender_radio3 = Radiobutton(
        form1_screen, text="Other", variable=gender, value="other")
    gender_radio3.pack()

    Label(form1_screen, text="").pack()

    # Set register button
    Button(form1_screen, text="Search", width=10, height=1).pack()


def form2():

    # The Toplevel widget work pretty much like Frame,
    # but it is displayed in a separate, top-level window.
    # Such windows usually have title bars, borders, and other “window decorations”.
    # And in argument we have to pass global screen variable

    form2_screen = Toplevel(form_screen)
    form2_screen.title("form2")
    form2_screen.geometry("300x250")

    # Set text variables
    gender = StringVar()
    hart_disease = StringVar()
    # Set label for user's instruction
    Label(form2_screen, text="Please choose something to see the graph").pack()
    Label(form2_screen, text="").pack()

    # Set register button
    Button(form2_screen, text="Gender", width=10, height=1).pack()
    Label(form2_screen, text="").pack()
    Button(form2_screen, text="Hart Disease", width=10, height=1).pack()
    Label(form2_screen, text="").pack()


def form3():

    # The Toplevel widget work pretty much like Frame,
    # but it is displayed in a separate, top-level window.
    # Such windows usually have title bars, borders, and other “window decorations”.
    # And in argument we have to pass global screen variable

    form3_screen = Toplevel(form_screen)
    form3_screen.title("form3")
    form3_screen.geometry("300x250")

    # Set label for user's instruction
    Label(form3_screen, text="These are the statistics of age").pack()
    Label(form3_screen, text="").pack()


main_account_screen()  # call the main_account_screen() function
