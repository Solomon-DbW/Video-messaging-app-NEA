import customtkinter as ctk
import sqlite3

def delete_record_popup(root):
    popup = ctk.CTkToplevel(root)
    popup.title("Delete Account")
    popup.geometry("300x300")

    delete_box = ctk.CTkEntry(popup, width=100)
    delete_box.grid(row=5, column=0)

    delete_box_label = ctk.CTkLabel(popup, text="ID number")
    delete_box_label.grid(row=6, column=0)

    def delete_record():
        conn = sqlite3.connect("userinfo.db")
        curs = conn.cursor()

        curs.execute("DELETE from userdetails WHERE oid = ?", (delete_box.get(),))

        conn.commit()
        conn.close()

    delete_record_button = ctk.CTkButton(popup, text="Delete the record", command=delete_record)
    delete_record_button.grid(row=7, column=0)

