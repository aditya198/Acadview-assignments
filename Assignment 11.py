#Q.1- Write a python code to find a valid email address from a text.
#import re
email = input("Enter email: ")
match = re.match('[a-zA-Z0-9_.]*[@](gmail.com|yahoo.com|icloud.com|rediffmail.com|hotmail.com)',email)
if(match!=None):
    print("Valid  email")
    parts = re.split('@',email)
    print("User name is ",parts[0],"\nDomain name : ",parts[1])
else:
    print("Invalid Email")
#Q.2- Write a python program to find a valid Indian phone number from a text.(Valid Indian numbers will start with "+91-" and after that [6-9] followed by 9 digits.)
import re
phone = input("Enter a phone number: ")
#n = '+91-'+phn
match = re.match('^(\+91-)[6-9]\d{9}',phone)
if(match!=None):
    print("Valid phone number")
    num = re.split('-',phone)
    print("Number is " , num[1])
else:
    print("Invalid Phone number")
