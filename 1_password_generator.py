#in this project we will generate passwords and will keep them in binary file because it is not
#human readable
import random
import pickle

info={}
with open("game.p","br")as read_file:
    info=pickle.load(read_file)
    print(info)

string='abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?'
len_password=int(input("Enter total nos of letters in password: "))

password="".join(random.sample(string,len_password)) #the sample() of random takes 2 args: (string_of_pssible_letters, len_of_password)
#before using=> "".join, it was giving me a list of pass like["a","i","4","o"]  but join converted it into a list so we will get our password in str form
print(password)

answer=input("This is the highly secured password available. Would you like to keep this password? ")
if "yes" in answer:
    acc_name=input("Enter account name: ")
    info[acc_name]=password
    with open("game.p","bw")as file_write:
        pickle.dump(info,file_write,protocol=2)
        print("Password stored successfully")

else:
    print("OK")

#This was the file for generating passwords
#Now we will create a new file which will keep all the password