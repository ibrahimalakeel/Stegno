from stegano import lsb
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

rev_msg = str(input("Enter your image path to reveal the secret msg :"))
print()
print("Text has been revealed >> ", lsb.reveal(rev_msg))
