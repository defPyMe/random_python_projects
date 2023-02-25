from pytube import YouTube
from tkinter import * 
from tkinter import messagebox
import os
from moviepy.editor import *


def create_interface():
    try:
        
        






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

        
        def update_download_convert(string, filename, output_b, output_box):
            index = output_b.index(filename)
            output_b[index] = filename + string
            [output_box.insert("end", i + "\n") for i in output_b]
            
            #takes the desktop path and folder name 
        def click(desktop, folder):
            all_input = input_box.get("1.0", "end")
            result=all_input.split("https")
            updated_result = ["https"+i for i in result if len(i)>5]
            link_list_len = len( updated_result)
            label_conversion.config(text="convertion output" + "/n" + "videos links detected :" + link_list_len)
            if not os.path.exists(os.path.join(desktop, folder)):
                os.makedirs(os.path.join(desktop, folder))
            else:
        #need to add the message box here
                message= "download folder already exists"
                
        #maybe here i have all the info        

                #inserting the first lists now
            input_b = [input_box.insert("end", i + "\n") for i in updated_result]
            output_b = [output_box.insert("end", i + "\n") for i in updated_result]
                #checking if folder exists
            
            #looping through the list of the files
            
            try:
                for link in updated_result:
                    download_trial = Download(link)
                    if  download_trial:
                        updated_result.remove(link)
                        update_download_convert("Downloaded", link, output_b, output_box)  
                    else: next
    #i should have the list all converted now
            except:  messagebox.showerror("download error", "some error downloading " + link )
            
            
            while checking_if_mp4_left(os.path.join(desktop, folder)):
                for filename in os.scandir(os.path.join(desktop, folder)):
                    if filename.is_file() and ".mp4" in filename:
                        try:
                        #transforms the file 
                            clip = VideoFileClip(filename.path)
            #writes the corrected file
                            clip.audio.write_audiofile(os.path.join(desktop, folder) + filename.name[:-4] + ".mp3")
        #cleaning out mp4 file
                            clip.close()
                #removing the file using filename -path should be there
                            os.remove(filename)
                #need to rethink the lists here, with the index taken into consideration to change the mput boxes 
                            update_download_convert("Converted", filename)
                        except:
                            messagebox.showinfo("some error occurred while converting")
                            next 
    #using download_result as a flag
            
            
            
            
            
            
            
                return None
                            
                        
                        
               
    
        # button
        try_download = Button(frame_buttons, text="start download", command=click)
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


      





        root.resizable(False, False)
        root.mainloop()
        
        def checking_if_mp4_left(directory):
            #for file in direftory
            check = [i for i in directory if i.name[-4:]==".mp4"]
            if check != []:
                found_mp4 = True
            else:
                found_mp4 = False
            return found_mp4
        
        
        def Download(link, desktop, folder):
            youtubeObject = YouTube(link)
            youtubeObject = youtubeObject.streams.get_highest_resolution()
            try:
                youtubeObject.download(os.path.join(desktop, folder))
                download_result = True
            except:

                download_result = False
            #using download_result as a flag
            return download_result
        
       

    
    except Exception as e :
                messagebox.showinfo(message='An error has occurred ')
                print(e)
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)




#get the text in the text areas 




#adding a function taht splits all the text on the "https" pattern