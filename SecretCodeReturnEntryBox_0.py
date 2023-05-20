import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

def greet():
    root = tk.Tk()
    root.withdraw()
    name = simpledialog.askstring("Enter Name", "Please enter your name")

    if name == "Andrew":
        messagebox.showinfo("Special Code", "Special code: special code")
    else:
        messagebox.showinfo("Greeting", f"Hi {name}\nWelcome aboard")

greet()
