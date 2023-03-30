import pyperclip
import requests
import time
import os 
from os.path import realpath

class Automatic_method():
    #This class make auto the copying  
    
    #This method checks if the url is valid
    def is_valid(self, url):
        try:
            response = requests.head(url)
            return response.status_code == 200
        except:
            return False 
    
    #This method checks if the path exist if not create a file  
    def exist_path(self, name_file):
        file_path = realpath(os.path.join("./Saved_photo", name_file))
        file_path = file_path.replace("\\", "/")

        if os.path.exists(file_path):
            return True
        else:
            with open(file_path, "w") as mainfile:
                mainfile.close()
                return True
    
    # This method join the other 2 method
    def execute(self, times):
        if self.exist_path("links.txt"):
            file = open(realpath("./Saved_photo/links.txt"), "a")
        url = pyperclip.paste()
        while True:
            url = pyperclip.paste()
            if self.is_valid(url):
                file.write(url + "\n")
                print("Link saved to file!")
            else:
                print("Invalid link or unable to access link. Check it!")
            time.sleep(int(times))
        
        file.close()
