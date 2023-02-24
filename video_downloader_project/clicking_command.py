#most likely all imports here
from fetching_input_list import *
from interface import *
from download_mp4 import *


#tuple result has as first argument the list of ourls and as second its lenght
from checking_download_folder_existence import *






def click():
    tuple_result = split_input(all_input)
    conversion_list = tuple_result[0]
    #inserting the first lists now
    input_b = [input_box.insert("end", i + "\n") for i in conversion_list]
    output_b = [output_box.insert("end", i + "\n") for i in conversion_list]
    #checking if folder exists
    check_if_folder()
    #looping through the list of the files
    while len(conversion_list)>0:
        try:
            for link in conversion_list:
                Download(link)
                if  download_result:
                    conversion_list.remove(link)
                    update_download_convert("Downloaded", link)  
                else: next
    #modifying the second list to add downloaded and converted
            
    
                    
                
                
        except:
                messagebox.showinfo("Problem warning", "General error occurred")










