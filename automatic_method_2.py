import pyperclip
import requests
import time
import os
from os.path import realpath
import datetime

#Constant directory to save new file 
FILE_PATH_CNST= ".\Saved_photo\Autosave_newfile\{}.txt"


class Automatic_method_new_file():
    #This class make auto the copying and saving url copied in one file  file 
    
    #This method checks if the url is valid
    def is_valid(self, url):
        try:
            response = requests.head(url)
            return response.status_code == 200
        except:
            return False 
    
    #This method make the file with name like date 
    def make_file(self):

        #Use module datetime to obtain date
        now = datetime.datetime.now()
        
        #Strftime is a command from datetime that allow convert to string  
        formatted_date = now.strftime("%d-%B-%H-%M-%S")
        
        #Making a path with the date 
        file_path = realpath(FILE_PATH_CNST.format(formatted_date))
        file_path = file_path.replace("\\", "/")

        
        #Creating the file with the path created 
        with open(file_path,"w") as file:
            file.close()
            #Return  directory of file 
            return file_path
           
    
    # This method execute and also join the other 2 methods
    def execute(self, times):
        #Use module pyperclip to obtain the copied from clipboard
        url = pyperclip.paste()
        
        while True:
            
            x=self.make_file()
            file = open(x, "a")
            url = pyperclip.paste()
            #Making a condition to check     
            
            #If its true then its saved corectly
            if self.is_valid(url):
                file.write(url + "\n")
                print("Link saved to file ^_^")
                file.close()
            
            #Else the file created will be deleted 
            else:
                print("Check the link or its unable to acess")
                file.close()
                os.remove(x)
            
            #The time that the program waits to start an infinite bucle 
            time.sleep(int(times))