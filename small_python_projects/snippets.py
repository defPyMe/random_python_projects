from tkinter import *
import tkinter as tk

def delete():
    txt.delete('1.0', tk.END)

root = Tk()
txt = Text()
txt.insert("end", "wwwwwww")

b = Button(text="delete_textbox", command=delete)
txt.pack()
b.pack()


root.mainloop()