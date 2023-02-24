from pytube import YouTube
from checking_download_folder_existence import desktop_path, download_folder
import os




def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(os.path.join(desktop_path, download_folder))
        download_result = True
    except:

        download_result = False
    #using download_result as a flag
    return download_result