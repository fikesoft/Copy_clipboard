import pyperclip
import requests
import time
import os 
from os.path import realpath

class Automatic_method():
    #This class make auto the copying url and save
    #Saves the url into links.txt    
    
    #This method checks if the url is valid
    def is_valid(self, url):
        
        #Try except block that checks the response 
        try:
            #Makigna an request to head url 
            response = requests.head(url)
            return response.status_code == 200
        
        except:
            return False 
    
    #This method checks if the path exist if not create a file  
    def exist_path(self, name_file):
        
        #Making the path with the real path  
        file_path = realpath(os.path.join("./Saved_photo", name_file))
        
        #Replace 
        file_path = file_path.replace("\\", "/")

        if os.path.exists(file_path):
            return True
        else:
            with open(file_path, "w") as mainfile:
                mainfile.close()
                return True
    
    # This method  will run the other 2
    #Will paste with the module url
    #That you copied 
    def execute(self, times):
        
        #A condition that check with  the method existpath 
        #Also this open that file 
        if self.exist_path("links.txt"):
            file = open(realpath("./Saved_photo/links.txt"), "a")
        url = pyperclip.paste()
        
        #An infinite iteration that paste the lin
        while True:
            
            #Updating the functiion
            url = pyperclip.paste()
            
            #A condition 
            #If its valid than will paste into the file 
            if self.is_valid(url):
                file.write(url + "\n")
                print("Link saved to file!")
            else:
                print("Invalid link or unable to access link. Check it!")
            
            #Time that will wait  
            time.sleep(int(times))
        
        file.close()
