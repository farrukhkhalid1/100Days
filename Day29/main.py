from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip


def generate_password():
    word_list = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation + string.ascii_letters
    password = "".join(random.sample(word_list, 15))
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


def add_button():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(website) < 1 or len(username) < 1 or len(password) < 1:
        messagebox.showinfo(title="Oops", message="You left some fields empty.")
    else:
        confirmation = messagebox.askokcancel(title="Confirmation",
                                              message=f"Please confirm:\nWebsite: {website}\nUsername: {username}\nPassword: {password}")
        if confirmation:
            with open("password_file.txt", 'a') as f:
                f.write(f"{website} | {username} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


tk = Tk()
tk.title("Password Manager")
tk.minsize(width=500, height=400)
tk.config(padx=20, pady=20)

canvas = Canvas(width=200, height=190)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 96, image=image)
canvas.grid(column=1, row=0)

# Labels

website_label = Label(text="Website: ", font=("Arial", 15, "normal"))
website_label.grid(column=0, row=1)
username_label = Label(text="Email/Username: ", font=("Arial", 15, "normal"))
username_label.grid(column=0, row=2)
password_label = Label(text="Password: ", font=("Arial", 15, "normal"))
password_label.grid(column=0, row=3)

# Entries

website_entry = Entry(width=40)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
username_entry = Entry(width=40)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, "username@username.com")
password_entry = Entry(width=20)
password_entry.grid(column=1, row=3, sticky='w')

# Buttons

generate_button = Button(text="Generate Button", width=15, command=generate_password)
generate_button.grid(column=2, row=3, sticky='e')
add_button = Button(text="Add", width=40, command=add_button)
add_button.grid(column=1, row=4, columnspan=2, pady=5, sticky='we')

tk.mainloop()
