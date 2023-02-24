#most likely all imports here
from fetching_input_list import *
from interface import *
from download_mp4 import *
all_input = input_box.get("1.0", "end").strip().split()
#tuple result has as first argument the list of ourls and as second its lenght
from checking_download_folder_existence import *






def click():
    tuple_result = split_input(all_input)
    conversion_list = tuple_result[0]
    #checking if folder exists
    check_if_folder()
    #looping through the list of the files
    while len(conversion_list)>0:
        try:
            for link in conversion_list:
                Download(link)
        except:
                messagebox.showinfo("Problem warning", "General error occurred")










