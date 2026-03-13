import tkinter as tk
from tkinter import messagebox
from tkinter import Tcl

#documentation =  https://docs.python.org/3/library/tk.html


root=tk.Tk() #k() is the main class that creates the main window of the application, the root container.
#Components: It is based on "widgets" (visual elements) organized by geometry managers such as .pack(), .grid() o .place().

root.geometry("300x300") #it works to set the screen size

#////////////
label = tk.Label(root,text="hello world.",bg="cyan")  # always the first letter goes in capital letter : Lable, Tk , Button
#(1. First parameter: where it will live, in this case in the window, root. 2. Second parameter: the text of the label)
label.pack( fill=tk.X )  #we add the features inside the parenthesis    -fill argument in this code is filling the window along the x-axis
#also can be in the Y axis but we need to add an aditional property that is expand that works with booleans EX: fill = tk.X expand = True /(1) fot all the window BOTH

# the pack method use to display it EXAMPLE: side=tk.RIGHT/LEFT 
#///////////
def alert_0():
    messagebox.showinfo("view","Hi there!")

def greeting ():
    print("Greetings!")

button1 = tk.Button(root, text= "click here", padx= 10, pady= 5, command= greeting) #pdx size of the #to add a funtion command and add it without parenthesis  
button1.pack(expand = "True", anchor="center")

button2 = tk.Button(root, text= "click here", bg="gray",fg="white" ,command= alert_0)
button2.pack(expand = "True",anchor="center") #to apply the anchor need to add expand as True to allow move the position

#-------------------------------#

textbox = tk.Entry (root) # 1. First parameter: where it will live, in this case in the window, root. 2. Second parameter: the text of the label)
textbox.pack(expand = "True",anchor="center")

root.mainloop()