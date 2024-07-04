import pandas as pd
from funcs import *
from tkinter import Tk, Label, Entry, Button, Listbox, END, messagebox, StringVar, Frame, Scrollbar, VERTICAL
from until import safe_command

entries = []

root = Tk()
root.title("Radius 생성기")
root.geometry("350x250")
root.configure(bg='#f0f0f0')

header_frame = Frame(root, bg='#4e4e4e', padx=10, pady=10)
header_frame.pack(fill='x')

Label(header_frame, text="이름과 나이 입력", fg='white', bg='#4e4e4e', font=("Helvetica", 14, "bold")).pack()

input_frame = Frame(root, bg='#f0f0f0', padx=10, pady=10)
input_frame.pack(fill='x')

Label(input_frame, text="이름", bg='#f0f0f0', font=("Helvetica", 10)).grid(row=0, column=0, padx=10, pady=5, sticky='w')
name_var = StringVar()
Entry(input_frame, textvariable=name_var, font=("Helvetica", 10), width=25).grid(row=0, column=1, padx=10, pady=5)

Label(input_frame, text="나이", bg='#f0f0f0', font=("Helvetica", 10)).grid(row=1, column=0, padx=10, pady=5, sticky='w')
age_var = StringVar()
Entry(input_frame, textvariable=age_var, font=("Helvetica", 10), width=25).grid(row=1, column=1, padx=10, pady=5)

Button(input_frame, text="생성", command=safe_command(add_entry,name_var, age_var, entries), bg='#4e4e4e', fg='white', font=("Helvetica", 10)).grid(row=2, columnspan=2, pady=10)
root.mainloop()
