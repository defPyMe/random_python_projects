import os




def set_desktop():
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    download_folder = "downloaded_videos"   
    return desktop_path, download_folder

