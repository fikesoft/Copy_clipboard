import pyperclip
import requests
import time
import os 

#This program will copy the link that you copied in your clipboard 
#Also will save it into a namefile.txt 

start = input("This app will copy the link that you copied in your clipboard. \n Press ENTER to start")

#Function that check if the url its valid
def its_valid(url):
    try:
        #Making some request 
        response = requests.head(url)
        #This returns  True if the request is 200 
        return response.status_code == 200
    except:
        return False 

#Function that check if the path exists 
def exist_path(name_file):
    #We join to obtain a correct path
    file_path = os.path.join("/Saved_photo", name_file)
    #Check if its exist
    if os.path.exists(file_path):
        return True
    #Else we create  a file with write 
    else:
        with open(file_path, "w") as mainfile:
            mainfile.close()
            return True


while True: 
    # Open a file in append  mode that allow me to save the last links 
    if exist_path("links.txt")==True:
        file=open("C:/Users/Sorin Chirtoaca/Desktop/copi/Saved_photo/links.txt", "a")
    url = pyperclip.paste()
    
    #A condition that allows check if its valid or no
    if its_valid(url)==True:
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

