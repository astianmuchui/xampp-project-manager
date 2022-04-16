from cgitb import text
from genericpath import isdir, isfile
from tkinter import *
from PIL import Image,ImageTk
from tkinter import font
import webbrowser
import os
class functions():
   def open_app(self):
      self.xmp_cli = "C:/xampp/xampp-control.exe"   
      webbrowser.open(self.xmp_cli)

   def open_server(self):
      webbrowser.open("http://localhost/phpmyadmin")
   def open_folder(self):
      webbrowser.open("C:/xampp/htdocs/projects") 
   def browse(self):
      webbrowser.open("http://localhost/projects/"+self.dir)
class App(functions):
	def __init__(self, parent):
		super(App, self).__init__()
		
		self.parent = parent
		

		# labels config dict
		self.lbl_config = {
			"relief": RIDGE,
			"font":   ("Verdana", 12)
		}

		# entry config dict
		self.entry_config = {
			"length": 15,
			"ipady": 10
		}
      
		self.create_widgets()
   
   
	def create_widgets(self):

         self.xmp_lbl = Label(self.parent, text="Welcome",font=("bold",16),foreground="#2fa5e8")
         
         self.xmp_lbl.place(x=40,y=50) 
         self.xmp_lbl.configure(background="white")

         # self.sr_val = StringVar()
         # self.xmp_sr = Entry(self.parent,textvariable=self.sr_val,border=0,width=50,background="#ccc")
         # self.xmp_sr.place(x=300,y=60,height=30)

         # self.xmp_sr_btn = Button(self.parent,text="Search",background="#2fa4e7",border=0,height=20)
         # self.xmp_sr_btn.place(x=605,y=60,height=30,width=50)

         # Create necessary links

         self.xmp_opn_btn = Button(self.parent,text="Open Xampp",command=self.open_app,background="orange",border=0,height=2,width=15)
         self.xmp_opn_btn.place(x=40,y=120)

         self.xmp_sql_server = Button(self.parent,text="Phpmyadmin",command=self.open_server,background="orange",border=0,height=2,width=15)
         self.xmp_sql_server.place(x=160,y=120)

         self.xmp_htdocs = Button(self.parent,text="Projects Folder",command=self.open_folder,background="orange",border=0,height=2,width=15)
         self.xmp_htdocs.place(x=280,y=120)

         self.xmpLbl = Label(self.parent,text="My projects",foreground="#2fa4e7",font=("bold",12))
         self.xmpLbl.place(x=120,y=180)
         self.xmpLbl.configure(background="white")
         #create cards for the projects 

         self.counter = 0
         self.init = 0
         self.path ="../../../../../../xampp/htdocs/projects/"
         self.dirs = os.listdir(self.path)
         for self.dir in self.dirs:
            
            self.init +=1    
            self.counter +=120
            Button(self.parent,text=self.dir,command=self.browse,height=5,width=15,background="#2fa4e7",border=0).place(x=self.counter,y=240)
            fr_dvd = self.dirs.count
      
            



if __name__ == '__main__':
	root = Tk()

	root.geometry("1000x500")

	root.resizable(False,False)

	root.configure(background="white")


	root.title("Xampp projects Manager")
	
	app = App(root)
	root.mainloop()
