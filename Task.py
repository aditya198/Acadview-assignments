#Q.1)Accept the gender in terms of male or female from user.
#If client enters wrong input instead of putting error it will display an appropriate message and exits.
sex = input("Enter sex: ")
if(sex.isalpha() and sex=='male' or sex=='m' or sex=='Male' or sex=='MALE'):
    print("Your gender is: ",sex)
elif(sex.isalpha() and sex=='female' or sex=='f' or sex=='Female' or sex=='FEMALE'):
    print("Your gender is: ",sex)
elif(sex.isnumeric()):
    print("Invalid input.")

#Q.2)Accept the name and prints the name with salutation according to gender like sir for male and mam for female
name = input("Enter name: ")
sex = input("Enter sex(m/f): ")
if(name.isalpha() and sex=='m' or sex=='f'):
    if(sex=='m'):
        print("Hello {} sir".format(sex))
    elif(sex=='f'):
        print("Hello {} mam".format(sex))
elif(name.isnumeric()):
    print("Invalid input.You have entered a int value in name instead of string.")
if(sex!='m' or sex!='f'):
    print("Invalid input.m is for male,f is for female.No other option.")

#Q.3)Ask their age and check the age criteria,if the age of man is greater than 20,it will print you are able to
#enroll for python fundamental course otherwise it will display an msg that you are below age criteria you cant
#enroll the course and exits(program does not throw any error here)
age = input("Enter age: ")
if(age.isnumeric()):
    b= int(age)
    if(b>20):
        print("You are able to enroll for python fundamental course.")
    elif(b<=20):
        print("You are not able to enroll for python fundamental course.")
elif(age.isalpha()):
    print("Invalid input.Enter in number.")

#Q.4)If age of women is greater than 19 she is available to enroll for core Java course
age = input("Enter age: ")
if(age.isnumeric()):
    b = int(age)
    if(b>19):
        print("Avaialble to enroll for core Java course.")
    elif(b<=19):
        print("Not available to enroll for core Java course.")
elif(age.isalpha()):
    print("Invalid input.You have to enter number.")

#Q.5)If user enters wrong value like in case of input of name he enters numeric value it will guide the user to enter
    #alphabetic value and some text incase of blank input
    #and in case of age he enters alphabetical value it will only accepts integers and will guide the user to do so
name = input("Enter name: ")
if(name.isalpha()):
    print("Name: ",name)
elif(name.isnumeric()):
    print("You have to enter string value.")
elif(name ==''):
    print("You have to enter something.")
age = input("Enter age: ")
if(age.isnumeric()):
    b = int(age)
    print("Age: ",b)
elif(age.isalpha()):
    print("You have to enter int value")
elif(age == ''):
    print("You have to enter something")

