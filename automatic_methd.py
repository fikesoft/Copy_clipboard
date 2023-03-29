import pyperclip
import requests
import time
import os 

# This program will copy the link that you copied in your clipboard 
# Also will save it into a namefile.txt 

# Function that check if the url its valid
def is_valid(url):
    try:
        # Making some request 
        response = requests.head(url)
        # This returns True if the request is 200 
        return response.status_code == 200
    except:
        return False 

# Function that check if the path exists 
def exist_path(name_file):
    #We join to obtain a correct path
    file_path = os.path.join("C:/Users/Sorin Chirtoaca/Desktop/copi/Saved_photo" + name_file)
    #Check if its exist
    if os.path.exists(file_path):
        return True
    #Else we create  a file with write 
    else:
        with open(file_path, "w") as mainfile:
            mainfile.close()
            return True


# Open a file in append  mode that allow me to save the last links 
if exist_path("/links.txt")==True:
        file=open("C:/Users/Sorin Chirtoaca/Desktop/copi/Saved_photo/links.txt", "a")
url = pyperclip.paste()

while True: 
    url = pyperclip.paste()

    # A condition that allows check if it's valid or not
    if is_valid(url):
        file.write(url + '\n')
        print("Link saved to file!")
    else:
        print("Invalid link or unable to access link. Check it!")
        
    # Introduce a delay of 5 seconds between each link paste operation
    time.sleep(15)

    #####  Make a class with all of this  integrate  with menu 
