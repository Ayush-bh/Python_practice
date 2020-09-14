import json              #std lib to wrok with json file format
from difflib import get_close_matches       #compairs with the closest value and return it.

data = json.load (open ("teaching/data.json"))


def translate(w):
    w = w.lower ()
    if w in data:
        return data[w]
    elif w.title () in data:  # if user entered "delhi" this will check for "Delhi" as well.(Noun)
        return data[w.title ()]
    elif w.upper () in data:  # in case user enters words like USA or NATO.(Acronyms)
        return data[w.upper ()]
    elif len (get_close_matches (w, data.keys ())) > 0:
        yn = input (
            "\ndo you mean %s instead? Enter Y if yes or N if no: \n" % get_close_matches (w, data.keys ())[0])
        if yn.lower () == "y":
            return data[get_close_matches (w, data.keys ())[0]]
        elif yn.lower () == "n":
            return "\nThe word doesn't exist. Please double check it.\n"
        else:
            return "\nWe didn't understand your entry.\n"
    else:
        return "\nThe word doesn't exist. Please double check it.\n"


def ip():
    word = input ("\nEnter word: \n")
    output = translate (word)
    if type (output) == list:
        for item in output:
            print (item)
    else:
        print (output)


while True:
    def menu():
        mn = input ("\nplease select \n1.search \n2.exit\nEnter number: ")
        if mn.lower () == "1":
            return ip ()
        elif mn.lower () == "2":
            return exit ()
        else:
            return "please check the number"


    print (menu ())
