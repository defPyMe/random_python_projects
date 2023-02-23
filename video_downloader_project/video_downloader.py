from pytube import YouTube
from moviepy.editor import *
#needed to get the files in the folder 
import os 
#importing for the interface 
from interface import *
#getting the desktop path 


#all useful paths 
directory = r"C:\Users\cavazzinil\OneDrive - YOOX NET-A-PORTER GROUP\Desktop\temp files\downloaded_files"
#creating the path and name     
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
#creating the new directory name 
download_folder = "downloaded_videos"  







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


def delete_useless_files():
    filtering =  [filename.path for filename in os.scandir(directory) if ".mp4" in filename.path]
    [os.remove(i) for i in filtering]





#getting the input 
all_input = input_box.get("1.0", "end").strip().split()


#input_str = "https://www.youtube.com/watch?v=1kmkmNVuaXA&ab_channel=Enigmatichttps://www.youtube.com/watch?v=4PUHBL1vMNY&ab_channel=HALIDONMUSIC"
def split_input(input_str):
    result=input_str.split("https")
    updated_result = ["https"+i for i in result if len(i)>5]
    for link in split_input(updated_result):
        Download(link)
    
    check_if_folder()
    return None



# iterate over files in
# that directory






