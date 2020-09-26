import json              #std lib to wrok with json file format
from difflib import get_close_matches       #compairs with the closest value and return it.

data = json.load (open ("teaching/data.json"))   #loading data
#-------------------------------------------------------------------------------------------------
#compairing the keys in the file and finding the match. 
#-------------------------------------------------------------------------------------------------
def translate(w):
    w = w.lower ()
    if w in data:
        return data[w]
    elif w.title () in data:  # if user entered "texas" this will check for "Texas" as well.
        return data[w.title ()]
    elif w.upper () in data:  # in case user enters words like USA or NATO
        return data[w.upper ()]
    elif len (get_close_matches (w, data.keys ())) > 0:
        yn = input ("\ndo you mean %s instead? Enter Y if yes or N if no: "
                    "\n" % get_close_matches (w, data.keys ())[0])
        if yn.lower () == "y":
            return data[get_close_matches (w, data.keys ())[0]]
        elif yn.lower () == "n":
            print("\nThe word doesn't exist. Please double check it.\n")
        else:
            print("\nWe didn't understand your entry.\n")
    else:
        print("\nThe word doesn't exist. Please double check it.\n")
#----------------------------------------------------------------------------------------------------------
#returning the value assigned to the key
#----------------------------------------------------------------------------------------------------------

def ip():
    word = input ("\nEnter word: \n")
    output = translate (word)
    if type (output) == list:
        for item in output:
            print (item)
    else:
        print (output)
#------------------------------------------------------------------------------------------------------------
#callng the main menu function 
#-----------------------------------------------------------------------------------------------------------
while True:
    def menu():
        mn = input ("\nplease select \n1.search \n2.exit\nEnter number: ")
        if mn == "1":
            return ip ()
        elif mn  == "2":
            return exit ()
        else:
            print("please check the number")

    menu ()
