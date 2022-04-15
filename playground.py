from genericpath import isdir
import os
from os import pipe 
import webbrowser
target_dir = "../../../../../../xampp/htdocs/projects/"
dirs = os.listdir(target_dir)
for dir in dirs:
    webbrowser.open("http://localhost/projects/"+dir)