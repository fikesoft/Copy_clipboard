import pyperclip
import requests
import time

start = input("This app will copy the link that you copied in your clipboard. Press ENTER to start")

def its_valid(url):
    try:
        #Making some request 
        response = requests.head(url)
        #This returns  True if the request is 200 
        return response.status_code == 200
    except:
        print("Invalid url")
        return False 

# Open a file in write mode

while True: 
        # Open a file in write mode
    file=open("C:/Users/Sorin Chirtoaca/Desktop/copi/Saved_photo/links.txt", 'a')
    # Update the variable
    url = pyperclip.paste()
    if its_valid(url)==True:
        # Write clipboard contents to the file
        print(url)
        file.write(url + '\n')
        print("Link saved to file!")
        file.close()
        x=input("Press any button to continue or q to exit")
            
        if x=="q":
            break
        else:
            pass

    else:
        print("Invalid link or unable to access link.")
        break
