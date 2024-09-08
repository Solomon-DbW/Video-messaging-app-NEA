import customtkinter as ctk
import sqlite3

def open_login_popup(root):
    popup = ctk.CTkToplevel(root)
    popup.title("Login")
    popup.geometry("300x300")

    label = ctk.CTkLabel(popup, text="Enter username:")
    label.pack(pady=10)

    username_entry = ctk.CTkEntry(popup)
    username_entry.pack(pady=10)

    password_label = ctk.CTkLabel(popup, text="Enter password:")
    password_label.pack(pady=10)

    password_entry = ctk.CTkEntry(popup, show="*")
    password_entry.pack(pady=10)

    def login():
        username = username_entry.get()
        password = password_entry.get()

        conn = sqlite3.connect("userinfo.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM userdetails WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()

        if user:
            print("Logged in")
        else:
            print("Invalid credentials")

        conn.close()
        popup.destroy()

    login_button = ctk.CTkButton(popup, text="Login", command=login)
    login_button.pack(pady=10)

