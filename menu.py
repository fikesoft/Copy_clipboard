#In this file  will be a cmd menu that allows
#To set up the method that you will use the program
from automatic_methd import Automatic_method
from controled_methd import Controled_method
from automatic_method_2 import Automatic_method_new_file

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
        time_expected=int(input("What interval of time  would you prefer" \
        " for saving?"))

        method_saving=input("What would you prefer?\n1)That the links are " \
        "saved into a file\n2)That every link is saved into a new file?")

        if method_saving == "1":
            auto=Automatic_method()
            auto.execute(time_expected)
        else:
            Automatic=Automatic_method_new_file()
            Automatic.execute(time_expected)

    if x=="2":
        control=Controled_method()
        control.run()
    if x=="3":
        pass
    if x=="0":
        break