import os,getpass
import subprocess
import pyttsx3
def linux():
        
    os.system("color 01")
    print("\t\t\t Hi welcome to my TUI for some small tasks")
    os.system("color 07")

    print("\t\t\t-----------------------------------------")
    passwd = getpass.getpass("Enter ur password: ")
    apass = "abhay"
    if passwd != apass:
        print("authorization incorrect")
        pyttsx3.speak("authorization incorrect")
        exit()

    pyttsx3.speak("In which machine you want to use local/remote: ")    
    print("which machine you want to use local/remote: ",end="")
    location = input()
    print(location)
    if location == "remote":
        remoteIp = input("Enter ur Ip: ")
        user_name=input("Enter the username:")
    while True:
        os.system("color 04")
        print("\t\t .--,\t    .--,\n\t\t( (  \.---./  ) )\n\t\t '.__/o   o\__.'\n\t\t    {=  ^  =}\n\t\t     >  -  <\n      ___________.\"\"`-------`\"\".____________\n     /                                      \ \n     \ o   Press 1: to see date           o / \n     /     Press 2: to check Calendar       \ \n     \     Press 3: to conf Webserver       /   \n     /     Press 4: to create user          \ \n     \     Press 5: to install a package    / \n     /     Press 6: to check about server?  \ \n     \     Press 7: to exit \t\t    / \n     /______________________________________\ \n\t\t   ___)( )(___ \n \t\t  (((__) (__)))")
        os.system("color 02")
        pyttsx3.speak("Enter your choice")
        print("Enter your choice: " , end="")
        ch=input()
        print(ch)
        os.system("color 07")

        if location == "local":
            if int(ch) == 1:
                os.system("date")
            elif int(ch) == 2:
                os.system("cal")
            elif int(ch) == 3:
                os.system("sudo yum install httpd")
            elif int(ch) == 4:
                pyttsx3.speak("Please provide name of the user:")
                print("Please provide name of the user: ",end="")
                create_user = input()
                os.system("sudo useradd {0}".format(create_user))   ##this is called place holder  or interpolation
            elif int(ch) == 5:
                print("write a package name lets see if its available: ", end="")
                pack_name = input()
                os.system("sudo dnf install {0}".format(pack_name))
            elif int(ch) == 6:
                os.system("systemctl restart httpd")
            elif int(ch) == 7:
                exit()

                
            else:
                print("option not found")
            os.system(input("Press Enter to continue........"))
            os.system("cls")
        elif location == "remote":
            if int(ch) == 1:
                os.system("ssh {1}@{0} date".format(remoteIp,user_name))
            elif int(ch) == 2:
                os.system("ssh {1}@{0} cal".format(remoteIp,user_name))
            elif int(ch) == 3:
                os.system("ssh {1}@{0} sudo yum install httpd".format(remoteIp,user_name))
            elif int(ch) == 4:
                pyttsx3.speak("can you give me name for user:")
                print("can you give me name for user: ",end="")
                create_user = input()
                os.system("ssh {2}@{0} sudo useradd {1}".format(remoteIp,create_user,user_name))   ##this is called place holder  or interpolation
            elif int(ch) == 5:
                os.system("write a package name lets see if its available: ", end="")
                pack_name = input()
                os.system("ssh {2}@{0} sudo dnf install {1}".format(remoteIp,pack_name,user_name))
            elif int(ch) == 6:
                os.system("ssh {1}@{0}systemctl restart httpd".format(remoteIp,user_name))
            elif int(ch) == 7:
                exit()
            else:
                print("option not found")
            pyttsx3.speak("Press any key to continue")
            cl=input()
            os.system("cls")
                
        else:
            print("sorry wrong input")
            
