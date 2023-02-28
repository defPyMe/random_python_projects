from interface_using import *
from all_variables_path_using import *


'''([<tkinter.Frame object .!frame>, <tkinter.Frame object .!frame2>, <tkinter.Frame object .!frame3>, 
<tkinter.Frame object .!frame4>, <tkinter.Text object .!text>, <tkinter.Text object .!text2>],



[<tkinter.Label object .!frame4.!label>])'''
















if __name__ == "__main__": 
    creating_interface = interface()
    print( creating_interface)
    desktop_and_folder = set_desktop()
    #adding the buttons with all required argumnets 
    # frame_buttons, input_box,label_conversion, desktop, folder, output_box
    all_args = [creating_interface[0][2],creating_interface[0][4],creating_interface[1][0], desktop_and_folder[0], desktop_and_folder[1], creating_interface[0][5] ]
    create_button(*all_args)
    initialize_interface()
    
    
    
    

