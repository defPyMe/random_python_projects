import os
from tkinter import messagebox
from pytube import YouTube
from moviepy.editor import *
from tkinter import *
import tkinter as tk

def set_desktop():
            desktop_path = os.path.join(os.path.expanduser("~"), "Downloads")
            download_folder = "downloaded_videos"   
            full_path = os.path.join(desktop_path, download_folder)
            return desktop_path, download_folder, full_path
            
            #takes the desktop path and folder name 
# needs to set the indexing in the tuple 
# input_box,label_conversion, desktop, folder, output_box
def click(a, b, c, d, e):
            try:
                try:
                    full_path = (os.path.join(c, d))
                    all_input = a.get("1.0", "end")
                    result=all_input.split("https")
                    #adding som eminus two here as maybe this is getting in the way 
                    updated_result = ["https"+i[:-2] for i in result if len(i)>5]
                    link_list_len = len( updated_result)
                    b.config(text="convertion output" + "/n" + "videos links detected :" + str(link_list_len))
                    if not os.path.exists(full_path):
                        os.makedirs(full_path)
                        messagebox.showinfo("folder info", "download folder created")
                    
                    else:
                        try:
                            pass
                        except Exception as e:
                            exc_type, exc_obj, exc_tb = sys.exc_info()
                            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                            print(e, exc_type, fname, exc_tb.tb_lineno)
                            messagebox.showinfo(message=str(e)+ "   "+  "/n" + str(exc_type)+  "   "+ "/n" + str(fname)+"     "+ "/n" + str(exc_tb.tb_lineno)+ "/n")
            #need to 
                except:
                    messagebox.showinfo("folder info", "download folder created")

            #maybe here i have all the info        

                #cleaning the text boxes 
                a.delete('1.0', tk.END)
                e.delete('1.0', tk.END)
                #updating the text boxes with the values split as it is a list
                input_b = [a.insert("end", i + "\n") for i in updated_result]
                output_b = [i for i in updated_result]
                    
                # should be working up until now 
                print("output_b, updated_result --------------->", output_b, updated_result)
                
                
                
                
                
                
                
                #looping through the list of the files
                try:
                    for link in updated_result:
                        #need to fix this as we get no 
                        download_trial = Download(link[:-2],(full_path + "\\"))
                        
                        if  download_trial:
                            #pop seems to be working now, but should be added in the function
                            index_in_list = updated_result.index(link)
                            updated_result.pop(index_in_list)
                            update_download_convert("-- Downloaded", link, output_b, e)  
                        else: next
        #i should have the list all converted now
                except Exception as e:
                            exc_type, exc_obj, exc_tb = sys.exc_info()
                            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                            print(e, exc_type, fname, exc_tb.tb_lineno)
                            messagebox.showinfo(message=str(e) + str(exc_type)  + str(fname)+ str(exc_tb.tb_lineno))
                
                
                while checking_if_mp4_left((full_path + "\\")):
                    for filename in os.scandir((full_path + "\\")):
                        if filename.is_file() and ".mp4" in filename.name:
                            try:
                                print("filename", filename)
                                folder_to_iterate = os.listdir((full_path + "\\"))
                            #transforms the file 
                                clip = VideoFileClip(filename.path)
                #writes the corrected file
                                clip.audio.write_audiofile((full_path + "\\") + filename.name[:-4] + ".mp3")
            #cleaning out mp4 file
                                clip.close()
                                update_download_convert("--  Dwnloaded Converted", filename.name, folder_to_iterate,e)
                    #removing the file using filename -path should be there
                                os.remove(filename)
                    #need to rethink the lists here, with the index taken into consideration to change the mput boxes 
                                
                            except Exception as e:
                                exc_type, exc_obj, exc_tb = sys.exc_info()
                                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                                print(e, exc_type, fname, exc_tb.tb_lineno)
                                messagebox.showinfo(message=str(e) + str(exc_type)  + str(fname)+ str(exc_tb.tb_lineno))
                
                                next 
        #using download_result as a flag
                
                    
            except Exception as e :
                    
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    print(e, exc_type, fname, exc_tb.tb_lineno)
                    messagebox.showinfo(message=str(e)+ "/n" + str(exc_type)+ "/n" + str(fname)+ "/n" + str(exc_tb.tb_lineno)+ "/n")
                
                
                
                
                
                
                    return None

                           
#all functions i use above
def checking_if_mp4_left(directory):
            #for file in direftory
            check = [i for i in os.scandir(directory) if i.name[-4:]==".mp4"]
            if check != []:
                found_mp4 = True
            else:
                found_mp4 = False
            return found_mp4
        
        
def Download(link, path):
            youtubeObject = YouTube(link)
            youtubeObject = youtubeObject.streams.get_highest_resolution()
            try:
                youtubeObject.download(os.path.join(path))
                download_result = True
            except:

                download_result = False
            #using download_result as a flag
            return download_result
        
def update_download_convert(string, filename, list_from_output, output_box):
            #there is something wrong here, code needs some fixing
            #how can i have anything in the list if i popped it ? the variable has been modified 
            print("all variables in the arguments ", string, filename, list_from_output, output_box)
            index =list_from_output.index(filename)
            list_from_output[index] = str(filename) + string
            [output_box.insert("end", i + "\n") for i in list_from_output]
        
