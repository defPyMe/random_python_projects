from interface import *
#input_str = "https://www.youtube.com/watch?v=1kmkmNVuaXA&ab_channel=Enigmatichttps://www.youtube.com/watch?v=4PUHBL1vMNY&ab_channel=HALIDONMUSIC"
import all_variables_path


#returns a tuple (list, len_of_list)
def split_input(input_str):
    result=input_str.split("https")
    updated_result = ["https"+i for i in result if len(i)>5]
    link_list_len = len( updated_result)
    label_conversion.config(text="convertion output" + "/n" + "videos links detected :" + link_list_len)
    return updated_result,  link_list_len 