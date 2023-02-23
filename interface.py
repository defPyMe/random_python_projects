from tkinter import *
from tkinter import messagebox



root=Tk()
frame_first_label = Frame()
frame_second_label = Frame()



input_box=Text(padx=15)
output_box=Text(padx=15, width=40)

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




#get the text in the text areas 
all_input = input_box.get("1.0", "end").strip().split()






#input_str = "https://www.youtube.com/watch?v=1kmkmNVuaXA&ab_channel=Enigmatichttps://www.youtube.com/watch?v=4PUHBL1vMNY&ab_channel=HALIDONMUSIC"
def split_input(input_str):
    result=input_str.split("https")
    updated_result = ["https"+i for i in result if len(i)>5]
    return updated_result


split_input(all_input)
#adding a function taht splits all the text on the "https" pattern