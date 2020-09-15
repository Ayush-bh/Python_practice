import time
from datetime import datetime as dt

host_temp = r"C:\Users\abhar\OneDrive\Desktop\Python projects\website_block\hosts"
host_path = r"C:\Windows\System32\drivers\etc"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com"]

while True:
    if dt (dt.now ().year, dt.now ().month, dt.now ().day, 8) < dt.now () < dt (dt.now ().year, dt.now ().month,
                                                                                dt.now ().day, 16):

        with open (host_temp, "r+") as file:
            content = file.read ()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write (redirect + " " + website + "\n")

        print ("work")  # delete after successful execution(check in terminal)


    else:
        with open (host_temp, "r+") as file:
            content = file.readlines ()
            file.seek (0)
            for line in content:
                if not any (website in line for website in website_list):
                    file.write (line)
            file.truncate ()

        print ("fun")  # delete after successful execution (check in terminal)

    time.sleep (5)
