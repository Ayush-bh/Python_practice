This is a GUI application made with the help of "Tkinter".
It is a simple bookstore app. with which you can perform diffrent operations
like Add, update, delete, search books information.

It helped me to understand how tkinter and sqlite3 works.
also this is the first program during my practice where i have used the OOP concept
that is, creating class and objects.
-----------------------------------------------------------------------------------------
Working:

note: i have already given a "book.db" file with some sample data.
if you wish to make a new DB, the program will create one which i mentioned in the backend here(↓)
and initially it will be empty so you need to fill all the text box with some entry and 
press ADD button and then view all button,to see entry.

backend:
Initially it creats a Database named "book.db" if it is not present.(used sqlite3).
defined diffrent functions for diffrent operations. 
View all the entries in the DB.
Update a entry in the DB.
insert a entry in the DB.
delete a entry in the DB.
seaerch a entry in the DB.

frontend:
This is where the results will be reflected in a window which contains 
all the buttons to perform diffrents operations that we have 
defined in the backend.
this is done simply done by importing the class from the file where you have defined all the 
functions for the diffrents taks.(form backend(file) import Database(class))


____________________-------------------------------________________________________________
if you want to make a standalone file (.exe) that is for making it "exe" extenstion file.

route to the directry where you have saved the files, 
run the command "pyinstaller frontend.py" in the terminal of you IDE or cmdprompt
(as frontend.py here is the main file where we are performing all tasks) this will 
creat a file named "frontend.exe" and now you can execute it without calling 
it in a cmdprompt or terminal.
