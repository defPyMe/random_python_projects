from interface import *

all_input = input_box.get("1.0", "end").strip().split()
#input_str = "https://www.youtube.com/watch?v=1kmkmNVuaXA&ab_channel=Enigmatichttps://www.youtube.com/watch?v=4PUHBL1vMNY&ab_channel=HALIDONMUSIC"
#returns a tuple (list, len_of_list)
def split_input(input_str):
    result=input_str.split("https")
    updated_result = ["https"+i for i in result if len(i)>5]
    link_list_len = len( updated_result)
    return updated_result,  link_list_len 