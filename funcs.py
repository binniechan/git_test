import pandas as pd
from tkinter import Tk, Label, Entry, Button, Listbox, END, messagebox, StringVar, Frame, Scrollbar, VERTICAL

def create_excel(data):
    df = pd.DataFrame(data)
    df.to_excel('output.xlsx', index=False)
    return '엑셀 파일이 성공적으로 생성되었습니다!'

def add_entry(name_var, age_var, entries):
    name = name_var.get()
    age = age_var.get()
    if not name or not age:
        messagebox.showerror("오류", "이름과 나이를 모두 입력하세요.")
        return
    try:
        age = int(age)
        entries.append({'Name': name, 'Age': age})
        message = create_excel(entries)
        messagebox.showinfo("radius 생성 완료", message)
    except ValueError:
        messagebox.showerror("오류", "나이는 숫자여야 합니다.")