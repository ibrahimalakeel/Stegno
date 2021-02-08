from stegano import lsb
import getpass
from termcolor import colored as c

print(c("""
------- Just run und get all links in the entered url :) -------
  _____ _           _     _     _ _           _           
 |  __ (_)         | |   | |   | (_)         | |          
 | |__) | _ __ __ _| |_  | |__ | |_ _ __   __| | ___ _ __ 
 |  ___/ | '__/ _` | __| | '_ \| | | '_ \ / _` |/ _ \ '__|
 | |   | | | | (_| | |_  | |_) | | | | | | (_| |  __/ |   
 |_|   |_|_|  \__,_|\__| |_.__/|_|_|_| |_|\__,_|\___|_|  s
                     ______                               
                    |______|                              
""","cyan"))

path_img = str(input("Enter your image path :"))
path_text = str(input("Enter your secret text :"))
username = getpass.getuser()

data = lsb.hide(path_img,path_text)
data.save("C:/Users/{0}/Desktop/picture_new.png".format(username))
print("picture saved in C:/Users/{0}/Desktop/picture_new.png".format(username))
