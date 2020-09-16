import time
from datetime import datetime as dt

host_temp = r"hostpath"  #replace hostpath insde with the temperory path of your host file
host_path = r"realpath"  #replace realpath inside with the host file(the location i mentioned in the read me file)
redirect = "add."        #replace add. inside with the redirect number(it is mentioned in the end of the hostfile ie 127.0.0.1 in mine).
website_list = ["www.facebook.com", "facebook.com"] #add more links of the websites that you want to block.

while True:
    if dt (dt.now ().year, dt.now ().month, dt.now ().day, 8) < dt.now () < dt (dt.now ().year, dt.now ().month,
                                                                                dt.now ().day, 16):

        with open (host_temp, "r+") as file:        #replace host_temp with host_path once the program runs successfully
            content = file.read ()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write (redirect + " " + website + "\n")

        print ("work")  # delete after successful execution(check in terminal)


    else:
        with open (host_temp, "r+") as file:        #replace host_temp with host_path once the program runs successfully
            content = file.readlines ()
            file.seek (0)
            for line in content:
                if not any (website in line for website in website_list):
                    file.write (line)
            file.truncate ()

        print ("fun")  # delete after successful execution (check in terminal)

    time.sleep (5)
