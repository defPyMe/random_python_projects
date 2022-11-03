import PyPDF2
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from datetime import *
import os.path
import sys
import xlsxwriter

root=Tk()
root.geometry('400x300')
root.title('FILE PER SERGIO DA ANTONELLA')
#getting the desktop name 
desktop = os.path.expanduser("~/Desktop")
# the above is valid on Windows (after 7) but if you want it in os normalized form:
desktop = os.path.normpath(os.path.expanduser("~/Desktop"))


'''
see what happens with a multiple page file
see if it srtill works or not and where are the elemnets

'''

DATE=date.today()
'''
work on any computer--> add the variables for the desktop
does it work with more pages ? --> counting the pages
create the excel file
time on the columns
file already created if it is there
maybe the name changes if the file has a different name
'''
def read_the_file():
    global name_of_the_document
    try:
        
        #create file object variable
        #opening method will be rb
        pdffileobj=open('p.pdf','rb')
         
        #create reader variable that will read the pdffileobj
        pdfreader=PyPDF2.PdfFileReader(pdffileobj)
         
        #This will store the number of pages of this pdf file
        x=pdfreader.numPages
        print('number of pages ', x)
         
        #create a variable that will select the selected number of pages
        try:
            
            pageobj=pdfreader.getPage(x+1)
        except:
            pageobj=pdfreader.getPage(x-1)
             
        #(x+1) because python indentation starts with 0.
        #create text variable which will store all text datafrom pdf file
        text=pageobj.extractText()
        #splitting in items 
        list1=text.replace('ŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠŠ','')
        list2=list1.split('!02CC')
        list_for_title=list2[:1]
        print('list_for_title',list_for_title)
        name_of_the_document=(str(list_for_title))[351:381]
        
        list3=list2[1:]
        count=0
        List=''
        #creating the lists storing the element s
        list_for_code1=[]
        list_for_code2=[]
        list_for_code3=[]
        list_for_code4=[]
        list_for_code5=[]
        list_for_code6=[]
        list_for_code7=[]
        list_for_code8=[]
        list_for_code9=[]
        list_for_code10=[]
        list_for_code11=[]
        #creating the lists for the data
        for i in list3:
            count=count+1
            list_name=(List+str(count))
            list_name=[]
            list_name.append(i)
            list_name_str=str(list_name).split('!')
            #list_name_list=list(list_name_str)
            print(list_name_str)
            print('---------------->', list_name_str[7])
            list_for_code1.append((list_name_str[7])[:42])
            list_for_code2.append((list_name_str[13])[42:])
            #second slot
            list_for_code3.append(list_name_str[1])
            list_for_code4.append(list_name_str[7])
            list_for_code5.append(list_name_str[12])
            #third slot
            list_for_code6.append(list_name_str[2])
            list_for_code7.append(list_name_str[8])
            list_for_code8.append(list_name_str[13])
            #fourth slot
            list_for_code9.append((list_name_str[6])[13:43])
            list_for_code10.append((list_name_str[12])[12:23])

            


            
        #checking what i get   
        print('1',list_for_code1)
        print('2',list_for_code2)
        print('3',list_for_code3)
        print('4',list_for_code4)
        print('5',list_for_code5)
        print('6',list_for_code6)
        print('7',list_for_code7)
        print('8',list_for_code8)
        print('9',list_for_code9)
        print('10',list_for_code10)


        workbook=xlsxwriter.Workbook(desktop+name_of_the_document+'.xlsx')
        worksheet=workbook.add_worksheet()
        worksheet.write(0,0,'NR SPEDIZIONE')
        worksheet.write(0,1,'MITTENTE NR XAB')
        worksheet.write(0,2,'DESTINATARIO E CITTA')
        worksheet.write(0,3,'IMPORTI ANNOTAZIONI')
        worksheet.write(0,4,'DATA')
        #adding the date ina  second time
        worksheet.write(1,4, DATE)
        workbook.close()

        
        #save the extracted data from pdf to a txt file
        #we will use file handling here
        #dont forget to put r before you put the file path
        #go to the file location copy the path by right clicking on the file
        #click properties and copy the location path and paste it here.
        #put "\\your_txtfilename"
       
##      file1=open(r"C:\\Users\\STABOL_PC04\\Desktop\\1.txt","a")
##      file1.writelines(text)
    except Exception as e :
        messagebox.showinfo(message='An error has occurred ')
        print(e)
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)



read_the_file()
 

#wrap everythin in a try , except block
def find_file():
    #create the filedialog to import the file , just pdf starting from bt
    #D:\STABOL-VOLUME\Scanner\BT_pdffiles
    root.filename=filedialog.askopenfilename(initialdir='D:\\STABOL-VOLUME\\Scanner\\BT_pdffiles\\', title='RICERCA RITIRI PER SERGIO' , filetypes=[('PDF files','*.pdf')])
    


    
    
    if os.path.isfile(desktop+ 'p'+'.xlsx'):
         messagebox.showinfo(message=' Order already created')
    else:
        print('already created')
         

button1=Button(root, text='find file', command = find_file).pack()
    

   


root.mainloop()
