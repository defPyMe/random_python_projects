from pytube import YouTube
from moviepy.editor import *
#needed to get the files in the folder 
import os
 


# assign directory

 




def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(r"C:\Users\cavazzinil\OneDrive - YOOX NET-A-PORTER GROUP\Desktop\temp files\downloaded_files")
    except:
        print("An error has occurred")
    print("Download is completed successfully")


link_list = ["https://www.youtube.com/watch?v=G7KNmW9a75Y&ab_channel=MileyCyrusVEVO"]


for link in link_list:
    Download(link)
    


directory = r"C:\Users\cavazzinil\OneDrive - YOOX NET-A-PORTER GROUP\Desktop\temp files\downloaded_files"
# iterate over files in
# that directory
for filename in os.scandir(directory):
    if filename.is_file():
        print("filename", filename.path)
        clip = VideoFileClip(filename.path)
        clip.audio.write_audiofile(r"C:\Users\cavazzinil\OneDrive - YOOX NET-A-PORTER GROUP\Desktop\temp files\downloaded_files"+filename.name[:-4] + ".mp3")
        #cleaning out mp4 file






'''


# Load the MP4 file
clip = VideoFileClip("input.mp4")

# Convert the MP4 file to MP3 format

'''