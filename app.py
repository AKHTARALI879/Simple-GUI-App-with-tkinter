import tkinter as tk
from turtle import title


def set_message():
    text = text_input.get()
    title_label.configure(text=text)


csa = tk.Tk()
csa.title("Python GUI Projects")
csa.minsize(width=300, height=300)

title_label = tk.Label(master=csa, text="Type any text and Click on Submit")
title_label.pack()

text_input = tk.Entry(master=csa)
text_input.pack()

btn = tk.Button(master=csa, text="Submit", command=set_message)
btn.pack()


csa.mainloop()
