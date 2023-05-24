"""
Random Password Generator Script
Created by: Alok Patel
Intern at CodeClause
IDE- VS Code
"""



from tkinter import *
import string
from secrets import choice

class PasswordGenerator:
    def __init__(self):
        self.window = Tk()
        self.window.title("Password Generator")
        self.window.geometry("500x300")

        self.label_frame = LabelFrame(self.window, text="Enter Length of the Password")
        self.label_frame.pack(pady=30)

        self.length_entry_box = Entry(self.label_frame, width=10)
        self.length_entry_box.pack(padx=20, pady=20)

        self.err = Label(self.window)

        self.password_entry_box = Entry(self.window, width=50)
        self.password_entry_box.pack(pady=20)

        self.button_frame = Frame(self.window)
        self.button_frame.pack(pady=20)

        pass_gen_btn = Button(self.button_frame, text="Generate Password", command=self.generate_password)
        pass_gen_btn.grid(row=0, column=0, padx=10)

        # Footer
        self.footer_label = Label(self.window, text="Made by ❤️©️alokmotion")
        self.footer_label.pack(side=BOTTOM, pady=10)

    def generate_password(self):
        length = int(self.length_entry_box.get())
        password = ''

        characters = string.ascii_letters + string.digits + string.punctuation

        for _ in range(length):
            password += choice(characters)

        self.password_entry_box.delete(0, END)
        self.password_entry_box.insert(0, password)

    def run(self):
        self.window.mainloop()

password_generator = PasswordGenerator()
password_generator.run()

