from interface import *
from fetching_input_list import *
from clicking_command import *

#requires output 
def update_download_convert(string, filename):
    index = output_b.index(filename)
    output_b[index] = filename + string
    [output_box.insert("end", i + "\n") for i in output_b]

    
