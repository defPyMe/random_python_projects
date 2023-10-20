import pandas as pd 
import os
from icecream import ic
import sqlite3
# assign directory
directory = r'C:\Users\cavazzinil\Dropbox\new job materials\modify_presentation_luxory\project faulty\faulty_good_material\configuration_table_total'
 
# iterate over files in 
# that directory


#should write to the sqlitedb for each db


conn = sqlite3.connect(r"C:\Users\cavazzinil\Dropbox\new job materials\modify_presentation_luxory\project faulty\faulty_good_material\configuration_table_total\New folder\configuration_table.db")


for filename in os.scandir(directory):
    if filename.is_file():
        ic("processing df")
        df_empty = pd.DataFrame()
        df = pd.read_excel(filename.path)
        ic("shape of current df", df.shape)
        #ic("adding " + filename)
        df_empty = df_empty.append(df)
        #ic("appending    " + filename)
        ic("shape should be increased ", df_empty.shape)
        df_empty.to_sql('Historic_data', conn,if_exists='append', index=True)
        

ic("all df processed")
conn.close()
     
