from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random

num1=0
num2=0
product = 0

def generate_numbers():
    global num1, num2, product
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    product = num1 * num2
    messagebox.showinfo("Info", f"One of the numbers is: {num1}")

def check_guess():
    global product
    guess = entry.get()
    if guess == str(product):
        messagebox.showinfo("Win", "Congratulations! You win!")
        root.quit()
    else:
        messagebox.showinfo("Try Again", "Try again!")

root = Tk()
root.title("Guessing Game")

generate_numbers()

label = Label(root, text="Guess the product of two numbers:")
label.pack()

entry = Entry(root)
entry.pack()

button = Button(root, text="Submit", command=check_guess)
button.pack()

root.mainloop()