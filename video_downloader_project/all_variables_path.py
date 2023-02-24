import os
from interface import *

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
download_folder = "downloaded_videos"  
all_input = input_box.get("1.0", "end").strip().split()
