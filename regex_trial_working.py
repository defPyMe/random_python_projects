import re
import pandas as pd
import sqlite3
from tkinter import *
from tkinter import messagebox

#creating the interface
root=Tk()
input_box=Text()
output_box=Text()


root.geometry("200x200")
#initialize the list here

#choosing tje right db
#we can use a list of lists to process this and creeate lists dinamically 

def creating_all_the_dbs_lists():
        global zip_dict
        global dbs
        choice = [ "zero", "one",  "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        dbs = [[] for i in range(10)]
        count = -1
        for i in choice:
                # we index the values in the lists of lists to get what we need
                with sqlite3.connect("C:\\Users\\cavazzinil\\OneDrive - YOOX NET-A-PORTER GROUP\\Desktop\\ff\\hs_codes.db") as conn:
                        command = ("SELECT codes, description FROM " + i ) #LIKE 'i%'
                        result = conn.execute(command)
                        list_of_results = result.fetchall()
                        zip_dict = (dict(list_of_results))
                count = count + 1
                dbs[count].append(zip_dict)
                

creating_all_the_dbs_lists()


def checking_for_input():
        #resetting lists
        global results
        global codes 
        codes = []
        results = []
        #getting the inputs 
        h=input_box.get("1.0", "end").strip().split()
        no_dupl = list(dict.fromkeys(h))
        
        for i in no_dupl:
                checking_list_inputs(i)
        for i in range(len(results)):
                output_box.insert("end", codes[i] + "    " + results[i] + '\n')



def clean_the_input(input_word):
        separators = ["-",",", "/", ".", "*", "   "]
        #turning it to string
        new_word = "".join([i for i in input_word if i not in separators])
        return new_word


def checking_list_inputs(word):
        try:
                cleaned_word =  clean_the_input(word)
                if str.isdigit(cleaned_word[:1]):
                        start_inp = int(cleaned_word[:1])
                        chosen_list = dbs[start_inp]
                        chosen_list_in_dict = {}
                #could have here a mechanisn that checks if the word contains only numbers
                #if not i put it into the output window
                        for i in chosen_list:
                                chosen_list_in_dict.update(i)
                        for n in chosen_list_in_dict:
                                txt = str(n)
                                x = re.search(fr"{cleaned_word}", txt)
                                if x == None:pass
                                elif x!=None:
                        #i can get the index of the dictionary key and go bak until the value is not
                                        results.append(chosen_list_in_dict[n])
                                        codes.append(n)
                        
                                        break
                
                        
                        else:
                                results.append(" WARNING, NOT FOUND AS A VALID HS CODE")
                                codes.append(cleaned_word)
                else:
                        results.append(" WARNING, NOT A VLAID NUMERIC HS CODE")
                        codes.append(cleaned_word)

        except:
                messagebox.showinfo(message="an error has occurred, check if all the imputs are correct hs codes")

#tryng to call the function here to see if it works
j=Button(text="see variable", command=checking_for_input)
output_box.pack()
j.pack()
input_box.pack()

root.mainloop()