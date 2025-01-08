from SQL.user_queries import user_exists, retrieve_password, SQL_to_user
from User.profile import Person
from gameplay_interface import interface
from create_user_interface import AccountCreationApp
import tkinter as tk
from tkinter import messagebox


class LoginApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login Interface")
        self.geometry("300x150")

        # Create a label and entry for username
        tk.Label(self, text="Username:").pack(pady=(20, 5))
        self.username_entry = tk.Entry(self)
        self.username_entry.pack(pady=(0, 10))

        # Create a label and entry for password
        tk.Label(self, text="Password:").pack(pady=(0, 5))
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack(pady=(0, 10))

        # Create a login button
        tk.Button(self, text="Login", command=self.login).pack(pady=10)
        create_new_user = AccountCreationApp
        tk.Button(self, text="Create New Account", command=create_new_user.mainloop()).pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        # Placeholder for authentication logic
        if not username or not password:
            messagebox.showwarning("Input Error", "Please enter both username and password.")
        else:
            if not user_exists(username):
                    messagebox.showinfo("Login", f"{username} not found")
            else:
                person = Person()
                retrieved_password = retrieve_password(username)
                if person.verify_password(password,retrieved_password):
                    user = Person()
                    SQL_to_user(user,username)
                else:
                    messagebox.showinfo("Login", f"Password is incorrect")


# Create and run the application
app = LoginApp()
app.mainloop()