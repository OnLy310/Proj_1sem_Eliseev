from tkinter import *
from tkinter import ttk


def submit():
    print("Sign me up!")


root = Tk()
root.title("html5 forms demo")
root.geometry("370x600")
root.resizable(False, False)
root.configure(bg="red")


title_label = Label(root, text="html5 forms demo", font="Arial 24", fg="white", bg="red")
title_label.pack(fill='x', padx=10, pady=10)


form_frame = Frame(root, bg="brown")
form_frame.pack(fill='x', padx=20, pady=20)


# First Name
first_name_frame = Frame(form_frame, bg="brown")
first_name_frame.pack(fill='x', padx=10, pady=5)
first_name_label = Label(first_name_frame, text="First Name", font="Arial 12", fg="white", bg="brown")
first_name_label.pack(anchor='w')
first_name_entry = Entry(first_name_frame, font="Arial 12")
first_name_entry.pack(fill='x')


# Last Name
last_name_frame = Frame(form_frame, bg="brown")
last_name_frame.pack(fill='x', padx=10, pady=5)
last_name_label = Label(last_name_frame, text="Last Name", font="Arial 12", fg="white", bg="brown")
last_name_label.pack(anchor='w')
last_name_entry = Entry(last_name_frame, font="Arial 12")
last_name_entry.pack(fill='x')


# Email Address
email_frame = Frame(form_frame, bg="brown")
email_frame.pack(fill='x', padx=10, pady=5)
email_label = Label(email_frame, text="Email address", font="Arial 12", fg="white", bg="brown")
email_label.pack(anchor='w')
email_entry = Entry(email_frame, font="Arial 12")
email_entry.pack(fill='x')


# Date of Birthday
dob_frame = Frame(form_frame, bg="brown")
dob_frame.pack(anchor='w', padx=10, pady=5)
dob_label = Label(dob_frame, text="Date of birthday (we like to send presents!)", font="Arial 12", fg="white",
                  bg="brown")
dob_label.pack(anchor='w')
computers_spinbox = ttk.Spinbox(dob_frame, from_=0, to=100, font="Arial 12", width=15)
computers_spinbox.pack(anchor='w')


# Country
country_frame = Frame(form_frame, bg="brown")
country_frame.pack(fill='x', padx=10, pady=5)
country_label = Label(country_frame, text="Country", font="Arial 12", fg="white", bg="brown")
country_label.pack(anchor='w')
country_entry = Entry(country_frame, font="Arial 12")
country_entry.pack(fill='x')


# Number of Computers
computers_frame = Frame(form_frame, bg="brown")
computers_frame.pack(anchor='w', padx=10, pady=5)
computers_label = Label(computers_frame, text="How many computers do you have at home?", font="Arial 12", fg="white",
                        bg="brown")
computers_label.pack(anchor='w')
computers_spinbox = ttk.Spinbox(computers_frame, from_=0, to=100, font="Arial 12", width=15)
computers_spinbox.pack(anchor='w')


# Disclaimer label
foot_label = (Label(root, text="We love spam, and we'll share your email address with all our third-party friends.\n"
                               "Heck, we'll even sell it! If you're happy to receive annoying email on a regular"
                               "basis\n"
                               "please click submit...", bg="red", fg="white", wraplength=340, justify="left"))
foot_label.pack(anchor='w', padx=20, pady=0)


# Submit Button
submit_button = Button(root, text="Sign me up!", command=submit, font="Arial 12", bg="orange", fg="white")
submit_button.pack(pady=20)
submit_button.pack(anchor='e', padx=20)


root.mainloop()
