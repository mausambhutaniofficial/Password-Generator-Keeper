#Here frst it will take a master password from user to display all the passwrds so as to verify that this ia the same user accessing this file
#we have used pyperclip to copy the password rather than display on screen 
import pickle
import pyperclip

m_pass=input("Enter master password:    ")
if m_pass=='mausam':
    acc_name=input("Enter account name:  ")
    with open("game.p","br")as read_file:
        info=pickle.load(read_file)

    if acc_name in info:
        pyperclip.copy(info[acc_name])      
        print("password copied")
#AND BOOM you are done, the password is copied on clipboard now you can just paste it in any login site,
#using pyperclip increased its security so anyone cannot view the password on console screen
    else:
        print("Oooops, Account not found")
else:
    print("Oooops, Password doesn't match")