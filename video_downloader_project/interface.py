from tkinter import *
from tkinter import messagebox



root=Tk()
frame_first_label = Frame()
frame_second_label = Frame()
frame_buttons = Frame()
frame_label_output = Frame()



input_box=Text(padx=15)
output_box=Text(padx=15, width=40)

#creating the upper two
label_output = Label(frame_second_label, text="download output", font=("Arial", 16), fg="black")
label_input = Label(frame_first_label, text="insert the urls of the songs to download" , font=("Arial", 16), fg="black")
#creating the label for dynamic info

label_conversion = Label(frame_label_output, text="convertion output", font=("Arial", 10), fg="black")


frame_first_label.grid(row=0, column=0)
frame_second_label.grid(row=0, column=1)

# button
try_download = Button(frame_buttons, text="start download", command="")
check_folder = Button(frame_buttons, text="check download folder", command="")


#gridding the butons
label_conversion.grid(row=0, column=0,  pady = 15, padx=6)
try_download.grid(row=0, column=1,  pady = 15, padx=6)
check_folder.grid(row=0, column=2,  pady = 15 , padx=6)


#gridding the two labels 
label_input .grid(row=0, column=0)
label_output .grid(row=0, column=1)
input_box.grid(row=1, column=0) 
output_box.grid(row=1, column=1)

frame_label_output.grid(row=2, column=0)
frame_buttons.grid(row=2, column=1, columnspan=2)









root.mainloop()




#get the text in the text areas 




#adding a function taht splits all the text on the "https" pattern