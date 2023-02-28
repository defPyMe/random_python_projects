from pytube import YouTube
from tkinter import * 
from tkinter import messagebox
import os
from moviepy.editor import *
from all_variables_path_using import click

root=Tk()

def interface():
    try:
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
           

            #gridding the butons
            label_conversion.grid(row=0, column=0,  pady = 15, padx=6)



            #gridding the two labels 
            label_input .grid(row=0, column=0)
            label_output .grid(row=0, column=1)
            input_box.grid(row=1, column=0) 
            output_box.grid(row=1, column=1)

            frame_label_output.grid(row=2, column=0)
            frame_buttons.grid(row=2, column=1, columnspan=2)
            
            all_widgets = root.winfo_children()
            all_widget_in_label_frame =  frame_label_output.winfo_children()
            

        
    except Exception as e :
                    
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    print(e, exc_type, fname, exc_tb.tb_lineno)
                    messagebox.showinfo(message=str(e)+ "/n" + str(exc_type)+ "/n" + str(fname)+ "/n" + str(exc_tb.tb_lineno)+ "/n")
                    
    #returning them both in a tuple  
    return all_widgets, all_widget_in_label_frame

def initialize_interface():
    root.resizable(False, False)
    root.mainloop()
    return None 
    
#needs to be returned the frame, needs to be returned above   
#need to be passed here as well
def create_button(frame_buttons, a, b, c, d, e):
    try_download = Button(frame_buttons, text="start download", command =lambda : click(a, b, c, d, e))#same arguments here as before
    check_folder = Button(frame_buttons, text="check download folder", command="")
    try_download.grid(row=0, column=1,  pady = 15, padx=6)
    check_folder.grid(row=0, column=2,  pady = 15 , padx=6)
    return None 
#get the text in the text areas 




#adding a function taht splits all the text on the "https" pattern