#  Variables Assignment & Operators

x = 10 
x = 23
y  = 0
z = ( x + y)/x + (78%3)

#  Primitive Types and String
name = "bobby"
age = 12 
height = 6.5
hasDate = False
comp = 7j

message = f"Hi my name is {name} I am {age} years old"

print(message)

intHeight = int(height)
strHeight = str(height)
floatHeight = float(height)
ageType = type(age)

#  Input Output

name  = input("Enter Name: ")
print(name)

#  Comparison
if 3 > 5:
    print("more")
else:
    print("less")


# elif === to else if
mark = input("Enter mark: ")
mark = int(mark)
if mark > 70 :
    print("A")
elif mark > 60:
    print("B")
elif mark > 50:
    print("C")
else:
    print("F")


i = 1
while i < 10:
    print(i)
    i += 1
else:
    print("This is run when the loop condition is no longer met")

# #iterating an iteraable such as a list
list = ["bob", "sally", "jhon"]
for j in list:
    print(j)

# #iterating between custom range an increment
for i in range(0,10,2):
    print(i)

# #basic function
def add(a, b):
    return a + b

def printPerson(name, age, height):
    print(name, age, height)

# #specifying arguments in any order if they are named
printPerson(age=12, name='bob', height=5)


def sayHello(fname, lname = 'Smith'):
    print('Hello' + fname + ' ' + lname)

sayHello('Jhon')

sayHello('Bill', 'Young')

#Python Syntax 2
#Lists
list = ['item1','item2','item3']
list2 = [12,33,45,58,23]

print(list)

print(list2[-1])

print(list2[2:4])

print(len(list2))

# #add items to list
list.append('item4')

print(list)

# #remove item from list
item4 = list.pop()

# print(list)

# #copies list
list3 =  list2.copy()

num = [1,2,3,4]
doubled= [n*2 for n in num]
print(doubled)

odd = [n for n in num if n%2 == 1]
print(odd)

num = [ 1, 2, 3, 4]
[first, second, *rest] = num
print(first)
print(second)
print(rest)

num2 = [5, 6]
num3 = num + num2
print(num3) 

num4 = num2.copy()

# #Tuples
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
print(thistuple[0])

# Sets
data = [ 20, 3, 20, 42, 2, 3, 10, 32, 2]

myset = {0, 1}

for num in data:
 myset.add(num)

print(myset)# {0, 1, 2, 3, 32, 42, 10, 20}
num_unique = len(myset)


# Dictionaries

mydict = {
    "name":"bob",
    "age": 34
}

print(mydict)

print(mydict["age"])

mydict['height'] = 7


# #prints the keys
for key in mydict:
    print(key)

# #prints the values

for key in mydict:
    print(mydict[key])

# #checking for a key

if 'weight' in mydict:
    print(mydict['weight'])
else:
    print('No weight property!')


# Classes

class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def sayHello(self):
        print("Hello ! I'm a person, my name is ", self.name)


class Student(Person):
    def __init__(self, stid, name, height, weight):
        super().__init__(name, height, weight)
        self.stid = stid

    def sayHello(self):
        print("Hello! I'm a student, my name is ", self.name)
    

bob = Person('Bob', 12, 175)

sally = Student(912234, 'Sally', 7, 133)

bob.sayHello()

sally.sayHello()

print(bob.name)

