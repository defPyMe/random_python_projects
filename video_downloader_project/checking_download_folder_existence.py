import os
from interface import *
from all_variables_path import *







def check_if_folder():
    if not os.path.exists(os.path.join(desktop_path, download_folder)):
        os.makedirs(os.path.join(desktop_path, download_folder))
    else:
        #need to add the message box here
        messagebox.showinfo("Problem warning", "Download folder already exists")