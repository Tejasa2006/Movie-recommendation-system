# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 08:44:07 2025

@author: Lokesh
"""

import tkinter as tk
from tkinter import messagebox
import sqlite3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Database setup
def initialize_db():
    connection = sqlite3.connect("Movie.db")
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS contact_us (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        email TEXT NOT NULL,
                        message TEXT NOT NULL
                      )''')
    connection.commit()
    connection.close()

# Save to database
def save_to_database(name, email, message):
    try:
        connection = sqlite3.connect("Movie.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO contact_us (name, email, message) VALUES (?, ?, ?)", (name, email, message))
        connection.commit()
        connection.close()
        return True
    except Exception as e:
        print("Database Error:", e)
        return False

# Send email to admin
def send_email_to_admin(name, email, message):
    try:
        sender_email = "choudharylokesh0009@gmail.com"  # Replace with your Gmail
        sender_password = "ofeo hawu cdfw iopr"  # Use Gmail App Password
        receiver_email = "choudharylokesh0009@gmail.com"

        subject = "New Contact Us Message"
        body = f"""
You have received a new message:

Name: {name}
Email: {email}

Message:
{message}
"""

        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        print("Email Error:", e)
        return False

# Handle send button
def send_message():
    name = name_entry.get()
    email = email_entry.get()
    message = message_entry.get("1.0", "end-1c")

    if not name or not email or not message.strip():
        messagebox.showerror("Validation Error", "All fields are required!")
    else:
        success = save_to_database(name, email, message)
        if success:
            email_sent = send_email_to_admin(name, email, message)
            if email_sent:
                messagebox.showinfo("Success", "Message sent and emailed successfully!")
            else:
                messagebox.showwarning("Saved", "Message saved, but email sending failed!")
            name_entry.delete(0, tk.END)
            email_entry.delete(0, tk.END)
            message_entry.delete("1.0", tk.END)
        else:
            messagebox.showerror("Error", "Failed to save message to database!")

# Initialize DB
initialize_db()

# Tkinter UI
root = tk.Tk()
root.title("Contact Us")
root.geometry("800x500")
root.config(bg="#202324")

# Left Panel
left_frame = tk.Frame(root, bg="#202324", width=300, height=500)
left_frame.pack(side="left", fill="y")

contact_title = tk.Label(left_frame, text="Contact Us", font=("Arial", 24, "bold"), fg="white", bg="#202324")
contact_title.pack(pady=20)

contact_desc = tk.Label(
    left_frame, 
    text="Reach out to us with your queries or feedback.", 
    font=("Arial", 10), fg="lightgray", bg="#202324", wraplength=250, justify="center"
)
contact_desc.pack(pady=10)

contact_info = [
    ("🏠 Address", "wakad, pune- 411033"),
    ("📞 Phone", "9691174877"),
    ("✉ Email", "choudharylokesh0009@gmail.com"),
]

for title, value in contact_info:
    tk.Label(left_frame, text=title, font=("Arial", 12, "bold"), fg="#00D1E0", bg="#202324").pack(pady=5)
    tk.Label(left_frame, text=value, font=("Arial", 10), fg="white", bg="#202324").pack(pady=2)

# Right Panel
right_frame = tk.Frame(root, bg="white", width=500, height=500)
right_frame.pack(side="right", fill="both", expand=True)

send_message_title = tk.Label(right_frame, text="Send Message", font=("Arial", 18, "bold"), bg="white", fg="#303030")
send_message_title.pack(pady=20)

entry_bg_color = "#F0F0F0"

name_label = tk.Label(right_frame, text="Full Name", font=("Arial", 12), bg="white", anchor="w")
name_label.pack(fill="x", padx=20)
name_entry = tk.Entry(right_frame, font=("Arial", 12), bg=entry_bg_color, fg="#303030", bd=1, relief="solid")
name_entry.pack(fill="x", padx=20, pady=5)

email_label = tk.Label(right_frame, text="Email", font=("Arial", 12), bg="white", anchor="w")
email_label.pack(fill="x", padx=20)
email_entry = tk.Entry(right_frame, font=("Arial", 12), bg=entry_bg_color, fg="#303030", bd=1, relief="solid")
email_entry.pack(fill="x", padx=20, pady=5)

message_label = tk.Label(right_frame, text="Type your Message...", font=("Arial", 12), bg="white", anchor="w")
message_label.pack(fill="x", padx=20)
message_entry = tk.Text(right_frame, font=("Arial", 12), bg=entry_bg_color, fg="#303030", bd=1, relief="solid", height=5)
message_entry.pack(fill="x", padx=20, pady=5)

send_button = tk.Button(
    right_frame, text="Send", font=("Arial", 12, "bold"), bg="#00D1E0", fg="white",
    activebackground="#00A8B0", bd=0, command=send_message
)
send_button.pack(pady=20, padx=20, ipadx=10, ipady=5, anchor="center")

root.mainloop()
