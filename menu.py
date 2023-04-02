#In this file  will be a cmd menu that allows
#To set up the method that you will use the program
from automatic_methd import Automatic_method
from controled_methd import Controled_method
from automatic_method_2 import Automatic_method_new_file
from dowland import Dowland

#The question that slected the method of use 
SELECTED_METHOD= '''
    ---------------------------------------
    What would you prefer?
    1) That the links are saved into a file 
    2) That every link is saved into a new file?
    0) Back 
    -----------------------------------------
    '''

#Main menu that wil show up the conditions 
MAIN='''
    ---------------------------------------
    1)Use the automatic checking of clipboard
    2)Use the controled method of copying
    3)Dowland photo with the file with links created
    0)Exit
    -----------------------------------------
    '''

def menu():
    return MAIN

#An bucle that will maintain the menu
while True:
    
    print(menu())
    
    x=input("What method would you use ?")

    #3 main condition that will interact with the menu
    
    if x=="1":
        
        #Interval of time  
        time_expected=int(input("What interval of time  would you prefer" \
        " for saving?"))

        while True:
            #Select the method 
            method_saving=input(SELECTED_METHOD)

            if method_saving == "1":
                auto=Automatic_method()
                auto.execute(time_expected)
            
            if method_saving =="2":
                Automatic=Automatic_method_new_file()
                Automatic.execute(time_expected)
            
            if method_saving =="0":
                break

    if x=="2":
        control=Controled_method()
        control.run()
    
    if x=="3":
        cl=Dowland()
        cl.run()
    
    if x=="0":
        break