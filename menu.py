#In this file  will be a cmd menu that allows
#To set up the method that you will use the program
def menu():
    ret= '''    
    ---------------------------------------
    1)Use the automatic checking of clipboard
    2)Use the controled method of copying  
<<<<<<< HEAD
    3)Dowland photo with the file with links created 
=======
    3)Dowland photo with the link created 
>>>>>>> f4db8ca1d54a785c3fbf092057735433cc9a8e9f
    0)Exit 
    -----------------------------------------
    '''
    return ret 

#An bucle that will maintain the menu 
while True:
    print(menu())
    x=input("What method would you use ?")
    if x=="1":
        pass
    if x=="2":
        pass
    if x=="3":
        pass
    if x=="0":
        break