import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import string
import random

def generate_password():
    length = int(length_entry.get())
    use_letters = letters_var.get()
    use_numbers = numbers_var.get()
    use_symbols = symbols_var.get()

    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Error", "At least one character type must be selected.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

root = tk.Tk()
root.title("Password Generator")

main_frame = ttk.Frame(root, padding="50")
main_frame.grid(row=0, column=0)

length_label = ttk.Label(main_frame, text="Password Length:")
length_label.grid(row=0, column=0, sticky="w")

length_entry = ttk.Entry(main_frame)
length_entry.grid(row=0, column=1)

letters_var = tk.BooleanVar()
letters_checkbutton = ttk.Checkbutton(main_frame, text="Include Letters", variable=letters_var)
letters_checkbutton.grid(row=1, column=0, sticky="w")

numbers_var = tk.BooleanVar()
numbers_checkbutton = ttk.Checkbutton(main_frame, text="Include Numbers", variable=numbers_var)
numbers_checkbutton.grid(row=2, column=0, sticky="w")

symbols_var = tk.BooleanVar()
symbols_checkbutton = ttk.Checkbutton(main_frame, text="Include Symbols", variable=symbols_var)
symbols_checkbutton.grid(row=3, column=0, sticky="w")

generate_button = ttk.Button(main_frame, text="Generate Password", command=generate_password)
generate_button.grid(row=4, column=0, columnspan=2)

password_entry = ttk.Entry(main_frame, width=30)
password_entry.grid(row=5, column=0, columnspan=2)

root.mainloop()