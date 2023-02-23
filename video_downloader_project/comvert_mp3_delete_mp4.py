from interface import * 
from pytube import YouTube
from moviepy.editor import *



def delete_useless_files():
    filtering =  [filename.path for filename in os.scandir(directory) if ".mp4" in filename.path]
    [os.remove(i) for i in filtering]
    
    
def search_and_convert():
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
