from interface import * 
from pytube import YouTube
from moviepy.editor import *
from all_variables_path import *
from updating_the_boxes import *


#def delete_useless_files():
#    filtering =  [filename.path for filename in os.scandir(directory) if ".mp4" in filename.path]
#    [os.remove(i) for i in filtering]
    
    
def search_and_convert(directory):
    for filename in os.scandir(directory):
        if filename.is_file() and ".mp4" in filename:
            try:
                #print("filename", filename.path)
            #transforms the file 
                clip = VideoFileClip(filename.path)
            #writes the corrected file
                clip.audio.write_audiofile(os.path.join(desktop_path, download_folder) + filename.name[:-4] + ".mp3")
        #cleaning out mp4 file
                clip.close()
                #removing the file using filename -path should be there
                os.remove(filename)
                #need to rethink the lists here, with the index taken into consideration to change the mput boxes 
                update_download_convert("Converted", filename)
            except:
                messagebox("some error occurred while converting")
                next 
