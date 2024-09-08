import customtkinter as ctk
import sqlite3

def update_popup(root):
    id_popup = ctk.CTkToplevel(root)
    id_popup.title("Update a record")
    id_popup.geometry("300x300")

    id_box = ctk.CTkEntry(id_popup, width=100)
    id_box.grid(row=1, column=0)

    id_box_label = ctk.CTkLabel(id_popup, text="ID number")
    id_box_label.grid(row=0, column=0)

    def submit_id():
        record_id = id_box.get()

        try:
            record_id = int(record_id)
        except ValueError:
            print("Invalid ID")
            return

        conn = sqlite3.connect("userinfo.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM userdetails WHERE oid = ?", (record_id,))
        db_info = cursor.fetchall()

        popup = ctk.CTkToplevel(root)
        popup.title("Update a record")
        popup.geometry("300x300")

        username_entry = ctk.CTkEntry(popup)
        username_entry.grid(row=4, column=0)
        password_entry = ctk.CTkEntry(popup, show="*")
        password_entry.grid(row=6, column=0)

        if db_info:
            for record in db_info:
                username_entry.insert(0, record[0])
                password_entry.insert(0, record[1])
        else:
            print("No record found")

        def update():
            username = username_entry.get()
            password = password_entry.get()

            conn = sqlite3.connect("userinfo.db")
            cursor = conn.cursor()

            cursor.execute("UPDATE userdetails SET username = ?, password = ? WHERE oid = ?", (username, password, record_id))

            conn.commit()
            conn.close()
            popup.destroy()

        save_button = ctk.CTkButton(popup, text="Save changes", command=update)
        save_button.grid(row=7, column=0)

        conn.close()

    id_submit_button = ctk.CTkButton(id_popup, text="Submit ID", command=submit_id)
    id_submit_button.grid(row=2, column=0)

