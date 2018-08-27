#Q.1)Name and handle the exception occured in the following program:
# a=3
    # if a<4:
     #   a=a/(a-3)
      #   print(a)
a=3
if(a<4):
    try:
        a=a/(a-3)
    except ZeroDivisionError:
        print('It is a Zero Division error.')

#Q.2) Name and handle the exception occurred in the following program:
#l=[1,2,3]
#print(l[3])
l=[1,2,3]
try:
    print(l[3])
except IndexError:
    print("It is an Index Error.")

#Q.3)# What will be the output of the following program.
try:
    raise NameError("Hi there")
except NameError:
    print("An exception")
    raise
#Output: An exception
#Answer: It will print 'An exception' first then show error in raise NameError('Hi there')

#Q.4) What will be the output of the following code.
def AbyB(a, b):
    try:
        c = ((a + b) / (a - b))
    except ZeroDivisionError:
        print("a/b result in 0")
    else:
        print(c)
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)
#Output: 5.0
#        a/b result in 0
#Answer: a)For first function call it will print the value of c.
#        b)For second function call it will print exception error message as error is Zero Division Error
#             and denominator is 0 .

#Q.5)Write a program to show and handle following exceptions:
#       1. Import Error
#       2. Value Error
#       3. Index Error
#Import error:
#ImportError is raised when a module, or member of a module, cannot be imported.
try:
    print(sys.version)
except:
    print("Import Error")

#Value Error: If input is not a valid datatype then program shows Value error.
try:
    number = int(input("Enter only number."))
except ValueError:
    print("Err.. numbers only")
else:
    print(number)

#Index Error: It is raised whenever attempting to access an index that is outside the bounds of a list .
l=[1,2,3]
try:
    print(l[3])
except IndexError:
    print("It is an Index Error.")
