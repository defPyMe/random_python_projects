import os




def set_desktop():
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    download_folder = "downloaded_videos"   
    return desktop_path, download_folder
    
def check_if_folder(desktop, folder):
    if not os.path.exists(os.path.join(desktop, folder)):
        os.makedirs(os.path.join(desktop, folder))
    else:
        #need to add the message box here
        messagebox.showinfo("Problem warning", "Download folder already exists")

