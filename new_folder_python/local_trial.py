from tkinter import *
from tkinter import messagebox
import sqlite3
from PIL import ImageTk, Image, ImageFont, ImageDraw
from tkinter import filedialog
import io

#grid(padx=20) adds 20 pixels to the left and right of the button.
# The padx=20 that is inside the constructor adds 20 pixels to the left and right of the text inside the button
#is a variable with the desktop needed ? or will it get the values ? i would say no 
# NEED TO ADD AN IMAGE ADD BUTTON IN THE ADD RECORD
root = Tk()
root.geometry("300x200")


def clean_the_input(input_string):
    global list_of_inputs
    separators = ["-",",", "/", ".", "*", "   "]
    for i in separators:
        new_string = input_string
        for n in new_string:
            if n==i:
                input_string  = input_string.replace(i, " ")
            else:
                next
    list_of_inputs = input_string.split()
    print(list_of_inputs)
    return list_of_inputs



def make_editable():
        text_box_query_modify["state"] = NORMAL
        text_box_edit_keyword["state"] = NORMAL

def save_changes():
        try:
        #need here to get the row and change it with two variables
                new_comment = str(text_box_query_modify.get("1.0", "end")).strip()
                new_keyword = str(text_box_edit_keyword.get("1.0", "end")).strip()
                with sqlite3.connect("path_to_db") as conn:
                        command = """   UPDATE comments_table
                                        SET     
                                                keyword = (?),
                                                comment = (?)
                                        WHERE
                                                id = (?) """
                        conn.execute(command, (new_keyword, new_comment, line_to_change))
                        conn.commit()
                messagebox.showinfo("value added", "value successfully added to DB")
        except :


                messagebox.showwarning("wrong insertion", "something went wrong, values not updated")

def convertToBinaryData(filename):
        with open(filename, 'rb') as file:
                blobData = file.read()
        return blobData



def see_picture():
        if picture_flag == "None":
                messagebox.showwarning("no image", "current record has no image")
        else: 
                #need to read the picture and display it
                new_window_picture_display = Toplevel()
                new_window_picture_display.geometry("350x405")
                new_window_picture_display.title(name_input)
                # getting the image from the DB 
                with sqlite3.connect("path_to_db") as conn:
                        command = "SELECT * FROM comments_table WHERE  id = (?)"
                        img = conn.execute(command, (line_to_change,))
                        #returns a tuple here
                        photo_tuple = img.fetchone()
                        photo = photo_tuple[3]
                fp = io.BytesIO(photo)
                image = Image.open(fp)
                # convert the image data to file object
                render = ImageTk.PhotoImage(image)
                #displaying it 
                # Create a Label Widget to display the text or Image
                label_picture = Label( new_window_picture_display, image = render)
                #needs to be recalled here as well
                label_picture.image = render # keep a reference!
                label_picture.pack()
      


def read_edit_comment(button_text):
        global text_box_edit_keyword, text_box_query_modify, line_to_change, picture_flag
        print("Button text =",list(button_text))
        new_window_read_edit = Toplevel()
        new_window_read_edit .geometry("350x405")
        new_window_read_edit.title(name_input)
        #should make the textbox editable by a button and add an image viewer
        #button see picture active only if the picture is present 
        label_space = Label(new_window_read_edit, text = "", height = 1)
        space_label_side_left = Label(new_window_read_edit,text = "", width = 1, height = 2,bg = "red")
        space_label_side_right = Label(new_window_read_edit,text = "", width = 3, height = 2,bg = "red")
        text_box_edit_keyword = Text( new_window_read_edit, height=1, width=17)
        button = Button( new_window_read_edit, text = "save", width = 10, command = save_changes)
        text_box_query_modify = Text( new_window_read_edit, height=15, width=40)
        button_edit = Button( new_window_read_edit, text= "edit", width = 5, command = make_editable)
        button_show_picture = Button(new_window_read_edit, text = "see picture", width = 10, command = see_picture)
        button_change_picture = Button(new_window_read_edit, text = "replace picture", command = insert_image)
        positions_m  = {label_space: (0,0),space_label_side_left: (1,0),text_box_edit_keyword:(2,1),
        button: (2,1,"e", 5,2 ),text_box_query_modify :(3,1,"", 10,2), space_label_side_right: (1,2),
        button_edit : (4,1, "n", 1, 2), button_change_picture : (4,1,"w", 1,1), button_show_picture : (4,1, "e", 3,1)  }
        gridding_widgets_in_dict(positions_m)

        #getting the value of the textb
        message =  str(button_text[2])
        message_keyword = str(button_text[1])
        line_to_change = int(button_text[0])
        picture_flag = str(button_text[3])


        text_box_query_modify.insert('end', message)
        text_box_edit_keyword.insert('end', message_keyword)


        text_box_query_modify["state"] = DISABLED
        text_box_edit_keyword["state"] = DISABLED

        if picture_flag == "None":
                button_show_picture["state"] = DISABLED



def query_db():
        global lis_of_results
        slaves = scrollable_frame.grid_slaves()
        for i in slaves:
                i.destroy()
        query_word = str(text_box_query.get("1.0", "end")).strip()
        query_word_cleaned = (clean_the_input(query_word))
        #should create the db if not existing here 
        #
        
        with sqlite3.connect("path_to_db") as conn:
                for i in query_word_cleaned:
                        command = ("SELECT * FROM comments_table WHERE keyword LIKE '" + i+ "%'")
                        result = conn.execute(command)
                        list_of_results = result.fetchall()
        print(list_of_results)
        if len(list_of_results)==0:
                messagebox.showwarning("query error", "query produced no results")
        else:
                count = 0
                for i in list_of_results: 
                        button_box = Button(scrollable_frame,
                        text=f"{i[0]} {i[1]}", width = 53, command=lambda j=i: read_edit_comment(j),
                        ).grid(row = count, column = 1)
                        count = count + 1


                
       # except:
        #        messagebox.showwarning("field error", "invalid search word, separate the word with spaces, commas (,) or a minus sign (-)") 

def insert_new_value():
        #isolating the value, loads the values 
        key_lookup = str(text_box_keyword.get("1.0", "end")).strip()
        comment = str(text_box_query_adding.get("1.0", "end")).strip()
        if comment != "" and key_lookup != "":
                with sqlite3.connect("path_to_db") as conn:
                        command = "INSERT INTO comments_table (keyword, comment) VALUES(?,?)"
                        conn.execute(command, (key_lookup, comment))
                        conn.commit()
        else:
                messagebox.showwarning("field error", "fill in all the required fileds")



def insert_image():
        root.filename=filedialog.askopenfilename(initialdir='', title='search images' , filetypes=(('png','*.png'),('jpeg', '*.jpg')))
        #returns a path
        img = root.filename
        #image needs to be converted to binary
        empPhoto = convertToBinaryData(img)
        
        with sqlite3.connect("path_to_db") as conn:
                        command = "UPDATE comments_table SET image = (?)  WHERE id = (?)"
                        conn.execute(command, (empPhoto,line_to_change))
                        conn.commit()
       


def add_records(**args):
        global text_box_keyword, text_box_query_adding
        new_window_add = Toplevel()
        new_window_add.geometry("350x404")
        new_window_add.title(name_input)
        #need to add a new label space here
        label_space = Label(new_window_add, text = "", height = 2)
        space_label_side_left = Label(new_window_add,text = "", width = 1, height = 2,bg = "red")
        space_label_side_right = Label(new_window_add,text = "", width = 3, height = 2,bg = "red")
        label = Label( new_window_add, text = "insert new values")
        text_box_keyword = Text( new_window_add, height=1, width=17)
        button = Button( new_window_add, text = "insert", width = 10, command = insert_new_value)
        text_box_query_adding = Text( new_window_add, height=15, width=40)
        button_insert_image = Button(new_window_add, text = "insert image", width = 10, command = insert_image)
        positions_m  = {label_space: (0,0),space_label_side_left: (1,0), label: (1,1),text_box_keyword:(2,1), button: (2,1,"e", 5,0 ),
        text_box_query_adding :(3,1,"", 10,0),space_label_side_right: (1,2), button_insert_image : (4,1, "e", 1,1) }
        gridding_widgets_in_dict(positions_m)
        #adding a messagebox now the record has been added 


def gridding_widgets_in_dict(dict_with_widgets):
    for i in dict_with_widgets:
        if len(dict_with_widgets[i]) <= 2:
                i.grid(row = dict_with_widgets[i][0],column = dict_with_widgets[i][1])
        else:
                i.grid(row = dict_with_widgets[i][0],column = dict_with_widgets[i][1], sticky = dict_with_widgets[i][2], pady = dict_with_widgets[i][3], padx = dict_with_widgets[i][4] )



def log_in_function():
    global result, name_input
    list_of_users = ["teresa"]
    name_input = str(text_box.get("1.0", "end")).strip()
    print(name_input)
    if name_input in list_of_users:
        result = messagebox.showinfo("log_info", "log in successful")
        build_second_screen(result, name_input, query_db)
    else:
        messagebox.showwarning("log_info", "wrong credentials")
    


def build_first_screen(log_in):  
    global text_box
    label = Label(text = "", width=3, height=3)
    label1 = Label(text = "insert username")
    label_space = Label(text = "", width=1, height=1)
    label_space1 = Label(text = "", width=1, height=1)

    text_box = Text(height=1,width=10)
    button_log = Button(text = "log in", command = log_in_function)
    label.pack()
    label1.pack()
    label_space.pack()
    text_box.pack()
    label_space1.pack()
    button_log.pack()



def query_style_DB():
        #this is creating some issues here as i add the values 
        pass


        


def show_style_DB():
        new_window_style_DB = Toplevel()
        new_window_style_DB.geometry("400x404")
        new_window_style_DB.title(name_input)
        #need to add a text input for the styles 
        text_box_query_style = Text(new_window_style_DB, height=1, width=12, padx = 4, pady = 4)
        #using always the same text input for everything
        button_query_styles = Button(new_window_style_DB, text = "show styles", command = query_style_DB)
        
        label_left = Label(new_window_style_DB,text = "      ", bg = "red")
        label_right = Label(new_window_style_DB,text = "      ", bg = "blue")
        label_center = Label(new_window_style_DB, text = "", height = 3, width = 15, bg = "red")
        label_under_text_input = Label(new_window_style_DB, text = "", height = 3, width = 15, bg = "blue")
        
        container = Frame(new_window_style_DB, width = 10,  pady = 4)
        
        canvas = Canvas(container)
        scrollbar = Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollable_frame = Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
             lambda e: canvas.configure(
              scrollregion=canvas.bbox("all")
             )
            )

        
        # adding all to the interface 
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        

        def add_new_style():
                def go_back_to_query():
                        button_query_styles["text"] ="query styles"
                        button_query_styles["command"] = query_style_DB 
                        button_add["text"]= "add style"
                        text_box_query_comment_result.grid_remove()
                        positions = { text_box_query_style : (0,1),  button_query_styles : (0,1,"e",20,5),  label_right: (0,3), container : (1,1 ), button_add : (2,1,"e",12,5) }
                        container.grid_remove()
                        gridding_widgets_in_dict(positions)

                button_query_styles["text"] ="add style"
                button_query_styles["command"] = go_back_to_query 
                button_add["text"]= "query styles"
                label_left_style_DB = Label(new_window_style_DB, width = 2)
                text_box_query_comment_result = Text(new_window_style_DB, height=15, width=40, padx = 4, pady = 4)
                #should leave everything as it is here and grid just the new ones 
                positions = {label_left_style_DB : (0,0), text_box_query_style : (0,1),  button_query_styles : (0,1,"e",20,5),  label_right: (0,3), text_box_query_comment_result : (1,1), button_add : (2,1,"e",12,5) }
                container.grid_remove()
                gridding_widgets_in_dict(positions)

               
                
        button_add = Button(new_window_style_DB, text = "Add new Style", height = 1, width = 12, command = add_new_style)





        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")


        positions = { text_box_query_style : (0,1),  button_query_styles : (0,1,"e",20,5),  label_right: (0,3), container : (1,1), button_add : (2,1,"e",12,5)}
        gridding_widgets_in_dict(positions)
        








#query mode here as default, frame is there 
def build_second_screen(output, name, query, **args):
    if output == "ok":
        global text_box_query, scrollable_frame
        new_window = Toplevel()
        new_window.geometry("450x500")
        new_window.title(name)
        label = Label(new_window, text = "parola chiave")
        space_label_side_left = Label(new_window,text = "", width = 2, height = 2)
        space_label_side_right = Label(new_window,text = "", width = 2, height = 2)
        space_label_center = Label(new_window,text = "", width = 10, height = 2)
        text_box_query = Text(new_window, height=1, width=17)
        button = Button(new_window, text = "query", width = 10, command = query_db)
        button_add = Button(new_window, text = "add", width = 10, command = add_records)
        button_open_style_DB = Button(new_window, text = "see style DB", command = show_style_DB)
        # to specify the destination widget we need to use it in the widget creation otherwise we get an error
        container = Frame(new_window, width = 10, height = 10)
        
        canvas = Canvas(container)
        scrollbar = Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollable_frame = Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
             lambda e: canvas.configure(
              scrollregion=canvas.bbox("all")
             )
            )

        
        # adding all to the interface 
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
       
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        #first line i put all the values for the labels 
        positions = {space_label_side_left : (0,0), space_label_center : (0,1), space_label_side_right: (0,3), label : (1,1),
        text_box_query: (2,1), button : (2,1, "e", 20,0), container : (3,1), button_add : (4,1, "e",33,0), button_open_style_DB : (4,1, "w", 33, 80)}
        gridding_widgets_in_dict(positions)



        
build_first_screen(log_in_function)


root.mainloop()
