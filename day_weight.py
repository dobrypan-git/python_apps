import tkinter as tk
from tkinter import simpledialog
import datetime

def get_user_weight():
    """
    Prompts the user to enter their weight in kilograms and returns it as a float.
    If the user cancels the input dialog, returns None.
    """
    user_input = simpledialog.askfloat("Weight Input", "Enter your weight in kg:")
    return user_input

def display_message(message):
    root = tk.Tk()
    root.title("Message")
    root.geometry("400x100")  # Set the size to 400x100 pixels
    label = tk.Label(root, text=message, font=("Times New Roman", 24))  # Increase the font size
    root.config(background="#ff0080")
    label.pack()
    root.mainloop()

weight = get_user_weight()

delta = datetime.date.today() - datetime.date(2024, 8, 26)
goal_weight = 80.65 - delta.days * 0.1

if weight is not None:
    if 68.15 < weight < goal_weight:
        display_message(f"Day {delta.days} - Your weight is {weight} kg.\n You're {round(goal_weight - weight,4)} kg lighter.")
    elif weight < 68.15:
        display_message(f"GOAL!!!\n CONGRATULATIONS!!!")
    else:
        display_message(f"Day {delta.days} - Your weight is {weight} kg.\n You need to lose {round(weight - goal_weight,4)} kg.")
else:
    display_message("No weight entered")

