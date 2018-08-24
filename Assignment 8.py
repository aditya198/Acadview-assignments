# Q.1- Create a circle class and initialize it with radius. Make two methods getArea and getCircumference inside this class.
class circle:
    def __init__(self,r):
        self.radius=r

    def getArea(self):
        return 3.14*self.radius*self.radius

    def getCircumference(self):
        return 2*3.14*self.radius

x = int(input("Enter value of radius: "))
ar = circle(x)
print("area of circle is ", ar.getArea())
print('circumference of circle is {}'.format(ar.getCircumference()))


# Q.2- Create a Student class and initialize it with name and roll number. Make methods to :
# 1. Display - It should display all informations of the student.
# 2. setAge - It should assign age to student 3. setMarks - It should assign marks to the student.


class Student:
    def __init__(self, name, rno):
        self.n = name
        self.r = rno

    def Display(self):
        print('Name: {}\nRoll No: {}'.format(self.n, self.r))

    def setAge(self, age):
        self.age = age
        print('Age: {} '.format(self.age))

    def setMarks(self, m):
        self.marks = m
        print('Marks: {} '.format(self.marks))


st1 = Student('Rishabh Sharma', 1610991707)
st1.Display()
st1.setAge(20)
st1.setMarks(75)


# Q.3- Create a Temprature class and create two methods:
# 1. convertFahrenheit - It will take celsius and will print it into Fahrenheit.
# 2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.
class Temprature:
    def __init__(self):
        print("Converting Temprature")

    def convertFahrenheit(self, c):
        self.c = c
        print('{}C ->{}f'.format(self.c, ((self.c * 9 / 5) + 32)))

    def convertCelsius(self, f):
        self.f = f
        print('{}F ->{}C'.format(self.f, ((self.f - 32) * 5 / 9)))


temp1 = Temprature()
temp1.convertFahrenheit(27)
temp1.convertCelsius(98);

# Q.4- Create a class MovieDetails and initialize it with artistname,Year of release and ratings .
# Make methods to
# 1. Display-Display the details.
# 2. Add- Add the movie details.

# Q.4- Create a class MovieDetails and initialize it with artistname,Year of release and ratings .
# Make methods to
# 1. Display-Display the details.
# 2. Add- Add the movie details.

class MovieDetails:
    def __init__(self, a, y, rr):
        self.a = a
        self.y = y
        self.rr = rr
        print("Create a class MovieDetails")

    def display(self):
        print('artist name {}\n year of release {}\n ratings {} star'.format(self.a, self.y, self.rr))

    def setaddmoviedetails(self, actorname):
        self.ac = actorname
        print('actorname added now using setter fun is {}'.format(self.ac))


t1 = MovieDetails('shahruk', 1998, 5)
t1.display()
t1.setaddmoviedetails('ranveersingh')

# Q.5- Create a class Animal as a base class and define method animal_attribute. Create another class Tiger which is inheriting Animal and access the base class method.

class Animal:
    def animal_attribute(self):
        print("base clas animal_attribute ")


class Tiger(Animal):
    def dis(self):
        print("derievd class called")


r = Tiger()
r.dis()
r.animal_attribute()


# qs 6
# ans is A B
#        A B

# Q.7- Create a class Shape.Initialize it with length and breadth Create the method Area.
# Create class rectangle and square which inherits shape and access the method Area.


class Shape:
    def __init__(self, ll, bb):
        self.l = ll
        self.b = bb

    def Area(self):
        '''area method created'''


class rectangle(Shape):

    def Area(self):
        print('area of rectangle is ', (self.l * self.b))


class square(Shape):

    def Area(self):
        print('area of square is ', (self.l * self.l))


r = rectangle(5, 6)
r.Area()
q = square(5, 6)
q.Area()

