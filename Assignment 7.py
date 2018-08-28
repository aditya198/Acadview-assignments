#Q.1)Create a user defined dictionary and get keys corresponding to the value using for loop.
n = int(input("Enter number of items you want to enter: "))
d ={}
for i in range(n):
    text = input("Enter key:value = ").split(":")
    d[text[0]] = text[1]
print(d)
key = input("Enter the key whose value you want to print: ")
for i in d:
    if(key==i):
        print(key,":",d[i])

#Q.2)Create a dictionary and store student names and
# create nested dictionary to store the subject wise marks of every student.
# Print the marks of a given student from that dictionary for every subject.
#Hint: Use nested dictionary to store subjects marks.
n = int(input("Enter the number of keys you want: "))
d = {}
for i in range(0,n):
    a = input("Enter student name: ")
    d[a] = {}
    b = int(input("Marks in Physics: "))
    d[a]['Physics'] = b
    c = int(input("Marks in Chemistry: "))
    d[a]['Chemistry'] = c
    e = int(input("Marks in Maths: "))
    d[a]['Maths'] = e
name = input("Enter name of the student whose result you want to find: ")
for i in d:
    if(name==i):
        print(i,d[i])