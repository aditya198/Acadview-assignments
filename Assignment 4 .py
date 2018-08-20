#Q.1) Reverse a list using list methods
n = int(input("Enter the total numbers in the list: "))
list = []
for i in range(0,n):
    a = int(input("Enter the elements: "))
    list.append(a)
print("List is: ",list)
print("Reverse of the list is: ",list[::-1])

#Q.2)Print all the uppercase letters from the string
str = input("Enter any string: ")
print("Uppercase etters of the string are: ")
for i in str:
    if(i>="A" and i<="Z"):
        print(i,end ="")

#Q.3- Split the user input on comma's and store the values in a list as integers.
n1 = input("Enter numbers using commas: ").split(",")
lst = []
for i in n1:
    b = int(i)
    lst.append(b)
print("List is: ",lst)
#Q.4)Check whether string is palindromic or not
str1 = input("Enter any string: ")
str2 = str1[::-1]
if(str1==str2):
    print("String is palindrome")
else:
    print("String is not palindrome")
#.5)Make a deepcopy of a list and write difference between shallow copy and deep copy
import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)

old_list[1][0] = 'BB'

print("Old list:", old_list)
print("New list:", new_list)
#Shallow Copy: A shallow copy creates a new object which stores the reference of the original elements.
              #So, a shallow copy doesn't create a copy of nested objects,
            #  instead it just copies the reference of nested objects.
#            This means, a copy process does not recurse or create copies of nested objects itself.
#Deep copy: A deep copy creates a new object and recursively adds the copies of nested objects present in the original elements.
           #The deep copy creates independent copy of original object and all its nested objects.
           #Both old list and new list are independent.