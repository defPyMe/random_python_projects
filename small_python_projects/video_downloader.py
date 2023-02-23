from pytube import YouTube
from moviepy.editor import *
#needed to get the files in the folder 
import os 
#importing for the interface 
from tkinter import *
from tkinter import messagebox
#getting the desktop path 



root=Tk()
input_box=Text(padx=15)
output_box=Text(padx=15)





def check_if_folder():
    if not os.path.exists(os.path.join(desktop_path, download_folder)):
        os.makedirs(os.path.join(desktop_path, download_folder))
    else:
        pass



def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(r"C:\Users\cavazzinil\OneDrive - YOOX NET-A-PORTER GROUP\Desktop\temp files\downloaded_files")
    except:
        print("An error has occurred")
    print("Download is completed successfully")
    
    
#creating the path and name     
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
#creating the new directory name 
download_folder = "downloaded_videos"  



#getting the input 
link_list = [
]


for link in link_list:
    Download(link)
    


directory = r"C:\Users\cavazzinil\OneDrive - YOOX NET-A-PORTER GROUP\Desktop\temp files\downloaded_files"
# iterate over files in
# that directory
for filename in os.scandir(directory):
    if filename.is_file():
        try:
            print("filename", filename.path)
            #transforms the file 
            clip = VideoFileClip(filename.path)
            #writes the corrected file
            clip.audio.write_audiofile(r"C:\Users\cavazzinil\OneDrive - YOOX NET-A-PORTER GROUP\Desktop\temp files\downloaded_files\ " + filename.name[:-4] + ".mp3")
        #cleaning out mp4 file
            clip.close()
            output_box.insert("end", filename.name  + "downloaded correctly" + '\n')
        except:
            print("error occurred")
            output_box.insert("end", filename.name  + " not downloaded" + '\n')
            next 


filtering =  [filename.path for filename in os.scandir(directory) if ".mp4" in filename.path]
[os.remove(i) for i in filtering]






