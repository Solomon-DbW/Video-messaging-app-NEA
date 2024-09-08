import customtkinter as ctk
import sqlite3

def query_popup(root):
    def query():
        conn = sqlite3.connect("userinfo.db")
        cursor = conn.cursor()

        cursor.execute("SELECT *, oid FROM userdetails")
        db_info = cursor.fetchall()

        print_user = ""

        for user in db_info:
            print_user += str(user[0]) + " -> " + str(user[1]) + "\t" + str(user[2]) + "\n"

        query_label.configure(text=print_user)  # Use 'configure' instead of 'config'

        conn.commit()
        conn.close()

    popup = ctk.CTkToplevel(root)
    popup.title("Database Contents")
    popup.geometry("400x400")

    query_label = ctk.CTkLabel(popup, text="")
    query_label.pack(pady=20)

    query_button = ctk.CTkButton(popup, text="Refresh", command=query)
    query_button.pack(pady=10)

    # Perform an initial query to display the data when the popup opens
    query()

