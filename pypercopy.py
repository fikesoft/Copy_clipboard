import pyperclip
import requests
import time

start=input("This app will copy the link that you copied in your clipboard \n press ENTER ")

url= pyperclip.paste()

def its_valid(url):
    #This function will check if the link exist and can be instaled  
    
    #Request 
    answer = requests.head(url)
    
    #Making a condition because if the http status code is 200 
    #the request has been succed and returned data 
    if answer.status_code == 200:
        return True
    
    else: 
        return False  

if its_valid(url)==True:

# Open a file in write mode
    with open("C:/Users/Sorin Chirtoaca/Desktop/copi/save_photo/links.txt", 'w') as file:
        while True: 

        
            # Write clipboard contents to the file
            file.write(url + '\n')
            print("Link saved to file!")
            print("You have 10 seconds to find next link")
            # Here i will continue   making an timer 
            #After this i will improve the begin of my program 
            
            
    # Close the file
    file.close()
        
