import pyperclip
import requests
import time
import os
from os.path import realpath

#This class will copy the link that you copied in your clipboard 
#Also will save it into a links.txt that it will create  

class Controled_method():
    
    def begin(self):
        input("This app will copy the link that you copied in your clipboard. \nPress ENTER to start")
        self.run()

    #A method that will check if it valid or not  
    def its_valid(self,url):
        
        try:
            #Making some request 
            response = requests.head(url)
            #This returns  True if the request give smth back  
            return response.status_code == 200
        
        except:
            return False 

    #Function that check if the path exists 
    def exist_path(self,name_file):
        
        #We join to obtain a correct path
        file_path = realpath(os.path.join("./Saved_photo", name_file))
        file_path = file_path.replace("\\", "/")
        
        #Check if its exist
        if os.path.exists(file_path):
            return True
        
        #Else we create  a file with write 
        else:
            with open(file_path, "w") as mainfile:
                mainfile.close()
                return True
            

    def run(self):
        while True: 
            
            # Open a file in append  mode that allow me to save the last links 
            if self.exist_path("links.txt")==True:
                file_path = "./Saved_photo/links.txt"
                file_path = file_path.replace("\\", "/")
                
                file=open(file_path, "a")
            
            url = pyperclip.paste()
            
            #A condition that allows check if its valid or no
            if self.its_valid(url)==True:
                file.write(url + '\n')
                print("Link saved to file!")
                file.close()
                
                #Condition that allow to continue or quit 
                x=input("Press any button to continue or q to exit")    
                if x=="q":
                    break
                else:
                    pass

            else:
                print("Invalid link or unable to access link \n Check it !")
                break
