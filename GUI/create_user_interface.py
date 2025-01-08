import tkinter as tk
from tkinter import messagebox
from SQL.user_queries import user_to_SQL
from User.profile import Person
from gameplay_interface import interface

special_characters = [
        '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+',
        '[', ']', '{', '}', ';', ':', "'", '"', ',', '.', '/', '<', '>', '?',
        '\\', '|', '`', '~'
    ]

digits = [str(i) for i in range(10)]

uppercase_letters = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

lowercase_letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]

letters = uppercase_letters + lowercase_letters

def valid_password(password:str):
    contains_letter = False
    contains_number = False
    contains_s_char = False
    if len(password) < 7:
        return -1
    if len(password) > 15:
        return -2
    for char in password:
        if char in letters:
            contains_letter = True
        if char in digits:
            contains_number = True
        if char in special_characters:
            contains_s_char = True
    if not contains_s_char or not contains_letter or not contains_number:
        return -3
    return 0
        


class AccountCreationApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Create Account")
        self.geometry("400x250")
        
        # Create the form for account creation
        self.create_account_form()

    def create_account_form(self):
        tk.Label(self, text="Username:").pack(pady=(20, 5))
        self.username_entry = tk.Entry(self)
        self.username_entry.pack(pady=(0, 10))

        tk.Label(self, text="Email:").pack(pady=(0, 5))
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(pady=(0, 10))

        tk.Label(self, text="Password:").pack(pady=(0, 5))
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack(pady=(0, 10))

        tk.Button(self, text="Create Account", command=self.create_account).pack(pady=20)

    def create_account(self):
        username = self.username_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        
        if not username or not password:
            messagebox.showwarning("Input Error", "Please fill out username and password")
            return
        if valid_password(password) == -1:
            messagebox.showwarning("Input Error", "password must be at least seven characters")
            return
        if valid_password(password) == -2:
            messagebox.showwarning("Input Error", "password must be at most fifteen characters")
            return
        if valid_password(password) == -3:
            messagebox.showwarning("Input Error", "password must contain a number, a letter, and a special character ")
            return
        
        user = Person()
        user.username = username
        user.password = user.password
        user.total_revenue = 0
        user.total_profit = 0
        if not email:
            user_to_SQL(user)
        else:
            user_to_SQL(user)
        # Here you would add logic to save the account information
        # For demonstration, we will just show the input values in a message box
        messagebox.showinfo("Account Created", f"Username: {username}\nEmail: {email}\nPassword: {password}")
        interface()

# Create and run the application