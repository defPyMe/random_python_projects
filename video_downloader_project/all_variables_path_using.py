import os
from tkinter import messagebox
from pytube import YouTube
from moviepy.editor import *

def set_desktop():
            desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
            download_folder = "downloaded_videos"   
            full_path = os.path.join(desktop_path, download_folder)
            return desktop_path, download_folder
        


            
            #takes the desktop path and folder name 
# needs to set the indexing in the tuple 
def click():
            paths_folder_desktop = set_desktop()
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
                    download_trial = Download(link, desktop, folder)
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
        
def update_download_convert(string, filename, output_b, output_box):
            index = output_b.index(filename)
            output_b[index] = filename + string
            [output_box.insert("end", i + "\n") for i in output_b]
