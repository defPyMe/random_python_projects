import re
import pandas as pd
import sqlite3
from tkinter import *

#creating the interface
root=Tk()
input_box=Text()
output_box=Text()
output_box.pack()
input_box.pack()

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





#ignore db they are all lists
def checking_list_inputs(word):
        start_inp = int(word[:1])
        chosen_list = dbs[start_inp]
        chosen_list_in_dict = {}
        for i in chosen_list:
                chosen_list_in_dict.update(i)
        for n in chosen_list_in_dict:
                txt = str(n)
                x = re.search(fr"{word}", txt)
                if x == None:pass
                elif x!=None:
                        #i can get the index of the dictionary key and go bak until the value is not
                        results.append(chosen_list_in_dict[n])
                        codes.append(n)
                        break

#tryng to call the function here to see if it works
j=Button(text="see variable", command=checking_for_input)
j.pack()
root.mainloop()
