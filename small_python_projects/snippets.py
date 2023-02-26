from tkinter import *
root = Tk()

def create_interface():
    button1 = Button(text="button text", command="") 
    label1 = Label(text="label text")
    button1.pack()
    label1.pack()
    d = root.winfo_children()
    return d



def initialize():
    root.mainloop()
