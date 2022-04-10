from cProfile import label
from genericpath import isfile

import os
import tkinter
from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("Xampp Project Manager")
root.resizable("false","false")
root.configure(background="#333")
class App:
    def __init__(self, parent):
        super(App, self).__init__()
        self.parent = parent
        self.lbl_config = {
           "releif":RIDGE,
           "font": ("Verdana",12)
        } 
        self.entry_config = {
			"length": 15,
			"ipady": 10
		}

    def build_widgets(self):
       # gui
       print("")   
           
from os import pipe

target_dir = "../../../../../../xampp/htdocs/projects/"

root.mainloop()    