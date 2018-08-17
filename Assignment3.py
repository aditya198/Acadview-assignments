#Q.1 Create a list with user defined inputs.
n = int(input("Enter the number of elements in the list: "))
a = []
for i in range(0,n):
    b = input("Enter the values in the list: ")
    a.append(b)
print(a)
#Q.2 Add ['google','apple',''facebook','microsoft','tesla'] to above created list
a.append('google')
a.append('apple')
a.append('facebook')
a.append('microsoft')
a.append('tesla')
print(a)
#Q.3 Count the number of time an object occurs in a list.
c = input("Enter the object that you want to count in the list: ")
print(a.count(c))
#Q.4 Create a list with numbers and sort it in ascending order.
list2 = [90,82,45,100,902,707,245]
list2.sort()
print(list2)
#Q.5 Merge two 1-d arrays A and B into single array C in ascending order.
A = [20,40,60]
B = [10,30,50]
C = A + B
C.sort()
print(C)
#Q.6 Implement a stack and queue using lists
stack = ['Rishabh','Rajat','Pritish']
print(stack)
stack.append('Rahul')
print(stack)
stack.append('Raghav')
print(stack)
print("Popping: ",stack.pop())#In stack we follow Last in First Out
print(stack)
queues = ['Rishabh','Rajat','Pritish']
queues.append('Rahul')
print(queues)
print("Popping: ",queues.pop(0))
print(queues)
#Optional question Count even and odd numbers in the list
lst = [24,15,21,34,89,75,38]
even = 0
odd = 0
for i in lst:
    if(i%2==0):
        even+=1
    else:
        odd+=1
print("Number of even elements are: ",even)
print("Number of odd elements are: ",odd)