import customtkinter as ctk
import sqlite3

def open_create_account_popup(root):
    popup = ctk.CTkToplevel(root)
    popup.title("Create Account")
    popup.geometry("300x300")

    label = ctk.CTkLabel(popup, text="Enter username:")
    label.pack(pady=10)

    username_entry = ctk.CTkEntry(popup)
    username_entry.pack(pady=10)

    password_label = ctk.CTkLabel(popup, text="Enter password:")
    password_label.pack(pady=10)

    password_entry = ctk.CTkEntry(popup, show="*")
    password_entry.pack(pady=10)

    def create_account():
        username = username_entry.get()
        password = password_entry.get()

        conn = sqlite3.connect("userinfo.db")
        cursor = conn.cursor()

        cursor.execute("INSERT INTO userdetails (username, password) VALUES (:username, :password)",
                       {"username": username, "password": password})

        conn.commit()
        conn.close()
        popup.destroy()

    create_account_button = ctk.CTkButton(popup, text="Create Account", command=create_account)
    create_account_button.pack(pady=10)

