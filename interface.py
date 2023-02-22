from tkinter import *
from tkinter import messagebox


root=Tk()
frame_first_label = Frame()
frame_second_label = Frame()



input_box=Text(padx=15)
output_box=Text(padx=15)

#creating the two labels 
label_input = Label(frame_first_label, text="insert the urls of the songs to download" , font=("Arial", 16), fg="black")
label_output = Label(frame_second_label, text="download output", font=("Arial", 16), fg="black")
frame_first_label.grid(row=0, column=0)
frame_second_label.grid(row=0, column=1)


#gridding the two labels 
label_input .grid(row=0, column=0)
label_output .grid(row=0, column=1)
input_box.grid(row=1, column=0) 
output_box.grid(row=1, column=1)
root.mainloop()