import tkinter as tk
import customtkinter as ctk
import sqlite3
from create_account_popup import open_create_account_popup
from login_popup import open_login_popup
from delete_record_popup import delete_record_popup
from update_popup import update_popup
from query_popup import query_popup

# Initialize the main application window
ctk.set_appearance_mode("dark")
root = ctk.CTk()
root.title("Video & Messaging")
root.geometry("700x700")

# Create database or connect to database
conn = sqlite3.connect("userinfo.db")
curs = conn.cursor()

# Create table if it doesn't exist
curs.execute('''
    CREATE TABLE IF NOT EXISTS userdetails (
        username TEXT PRIMARY KEY,
        password TEXT NOT NULL
    )
''')

# Buttons
create_account_button = ctk.CTkButton(master=root, text="Create Account", command=lambda: open_create_account_popup(root))
login_button = ctk.CTkButton(master=root, text="Login", command=lambda: open_login_popup(root))
update_button = ctk.CTkButton(master=root, text="Update a record", command=lambda: update_popup(root))
query_button = ctk.CTkButton(root, text="Show db contents", command=lambda: query_popup(root))
delete_button = ctk.CTkButton(root, text="Delete an account", command=lambda: delete_record_popup(root))

# Placing buttons on the screen
create_account_button.grid(row=0, column=0)
login_button.grid(row=1, column=0)
query_button.grid(row=2, column=0)
delete_button.grid(row=4, column=0)
update_button.grid(row=8, column=0)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

conn.commit()
conn.close()

root.mainloop()

