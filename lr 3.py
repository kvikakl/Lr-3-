import tkinter as tk
from tkinter import messagebox
import random
import os
import threading
import winsound

def play_music():
    if os.path.exists("8bit.wav"):
        while True:
            try:
                winsound.PlaySound("8bit.wav", winsound.SND_FILENAME)
            except Exception:
                break

def animate_button():
    colors = ['#FFFFFF', '#E8F0FE', '#D2E3FC', '#FFFFFF']
    current_color = btn.cget("bg")
    try:
        next_index = colors.index(current_color) + 1
        if next_index >= len(colors):
            next_index = 0
        btn.config(bg=colors[next_index])
    except ValueError:
        btn.config(bg=colors[0])
    window.after(300, animate_button)

def generate_key():
    word = entry.get().upper().strip()
    if len(word) != 6 or not word.isalpha():
        messagebox.showerror("Ошибка", "Введите слово из 6 латинских букв!")
        return
    block1 = ''.join(random.sample(word, 3))
    temp_word = list(word)
    for char in block1:
        temp_word.remove(char)
    block3 = ''.join(random.sample(temp_word, 3))
    block2 = ''
    for char in word:
        num = ord(char) - ord('A') + 1
        block2 += str(num % 10)
    result_label.config(text=f"{block1}-{block2}-{block3}")

window = tk.Tk()
window.title("Лабораторная №3 (Вариант 7)")
window.geometry("500x450")
window.resizable(False, False)

threading.Thread(target=play_music, daemon=True).start()

try:
    bg_img = tk.PhotoImage(file='bg.png')
    bg_label = tk.Label(window, image=bg_img)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
except tk.TclError:
    window.configure(bg='#E8F0FE')

frame = tk.Frame(window, bg='#FFFFFF', bd=0, highlightthickness=0)
frame.place(relx=0.5, rely=0.5, anchor='center', width=400, height=350)

title_label = tk.Label(frame, text="KEYGEN", font=('Helvetica', 24, 'bold'), bg='#FFFFFF', fg='#1A73E8')
title_label.pack(pady=(30, 10))

entry_label = tk.Label(frame, text="Введите слово из 6 букв:", font=('Helvetica', 11), bg='#FFFFFF', fg='#5F6368')
entry_label.pack(pady=(0, 10))

entry = tk.Entry(frame, font=('Helvetica', 16), justify='center', bg='#F1F3F4', fg='#202124', insertbackground='#202124', relief='flat', bd=0)
entry.pack(pady=5, ipadx=10, ipady=8)

btn = tk.Button(frame, text="Сгенерировать", font=('Helvetica', 12, 'bold'), command=generate_key, bg='#FFFFFF', fg='#1A73E8', activebackground='#F1F3F4', activeforeground='#1A73E8', relief='solid', bd=1, cursor='hand2')
btn.pack(pady=20, ipadx=15, ipady=8)

result_label = tk.Label(frame, text="XXX-XXXXXX-XXX", font=('Courier', 22, 'bold'), bg='#FFFFFF', fg='#202124')
result_label.pack(pady=10)

animate_button()
window.mainloop()