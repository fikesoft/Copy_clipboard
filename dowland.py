import os
import requests 
import json

#This is the name of folder that will be iterated
NAME_OF_FOLDER1="Saved_photo"
NAME_OF_FOLDER2="Autosave_newfile"


#A string necesary for an input  
QUESTION="What file do you want to acces?"


class Dowland():
    
    #A method that returns the path of the file 
    def path(self,name):
        
        #Try Except block  
        try:
            #Listing the folder 
            f=os.listdir(name)
            #An display of files from 1 to num  of the files into the path 
            x=1
            for i in range(1, len(f)+1): 
                print("{}){}".format(x,f[i-1])) 
                x=x+1
            
            #Question what you want to select 
            inp1=int(input(QUESTION))  
            
            #Creating the path wiht the name of main folder and the  file
            pth="{}/{}".format(name, f[inp1-1])

            return pth        
        
        except:
            
            f=os.listdir("{}/{}".format(NAME_OF_FOLDER1,NAME_OF_FOLDER2))
            
            #An display of files from 1 to num  of the files into the path 
            x=1
            for i in range(1, len(f)+1): 
                print("{}){}".format(x,f[i-1])) 
                x=x+1
            
            #Question what you want to select 
            inp1=int(input(QUESTION))  
            
            #Creating the path wiht the name of main folder and the  file
            pth="{}/{}/{}".format(NAME_OF_FOLDER1 ,name, f[inp1-1])
            return pth
    
    #A method that checks that file extentions  
    def check(self,pth):
        #A condtions that checks if the last  4 digits are .txt 
        if pth [-4:] == ".txt":
            return True
        else:
            return False 

    def request(self,indice, url=""):
        
        response= requests.get(url=url) 
        path_dowland="./Dowlanded/img{}.png"
        path_dowland=path_dowland.replace("\\","/")
        
        print("--------{}".format(path_dowland))

        
        fichero= open(path_dowland.format(indice),"wb")
        fichero.write(response.content)
        fichero.close()


    #A method that will dowland      
    def dowland2(self,pth):
        #1 Opens that file that contains
        f_urls=open(pth,"r")
        
        #Returns a list with the 
        f_load= f_urls.readlines()
         
        f_urls.close()

        
        for i in range(len(f_load)):
            w=f_load[i]
            self.request(i, w)
            print("One image is saved ")
        

    

    
    def run(self):
        pth=self.path(NAME_OF_FOLDER1)

        if self.check(pth) == True:
            self.dowland2(pth)
        else:
            pth= self.path(NAME_OF_FOLDER2)
            self.dowland2(pth)

                   
#cl=Dowland()
#cl.run()
#cl.path(NAME_OF_FOLDER1)
#print(cl.check("Saved_photo/links.txt"))