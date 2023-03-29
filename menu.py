#In this file  will be a cmd menu that allows
#To set up the method that you will use the program
from automatic_methd import Automatic_method
from controled_methd import Controled_method

def menu():
    ret= '''    
    ---------------------------------------
    1)Use the automatic checking of clipboard
    2)Use the controled method of copying  
    3)Dowland photo with the file with links created 
    0)Exit 
    -----------------------------------------
    '''
    return ret 

#An bucle that will maintain the menu 
while True:
    print(menu())
    x=input("What method would you use ?")
    if x=="1":
        auto=Automatic_method()
        auto.execute(15)
        pass
    if x=="2":
        pass
        
    if x=="3":
        pass
    if x=="0":
        break