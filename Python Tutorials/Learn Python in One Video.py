import this


print("Hello World")

# # Hello Himanshu Chauhan how are you

# '''Om
# kya
# kar
# rha
# hai'''

sttr = "This is string"
age = 22
weight = 75.3

print(sttr)
print(age)
print(weight)

# # type of opreter

print(type(sttr))
print(type(age))
print(type(weight))

# # Number Strings Lists Tuple Dictionaries

# # Arithmetic Operations

print("The value of 3 + 5 = ", 3 + 5)
print("The value of 3 - 5 = ", 3 - 5)
print("The value of 3 * 5 = ", 3 * 5)
print("The value of 3 / 5 = ", 3 / 5)
print("The value of 3 ** 5 = ", 3 ** 5)
print("The value of 3 // 5 = ", 3 // 5)

print("This is Double Cot \"")

mls = '''This 
    is 
    Multiline
        string
        and
        this
        will
        keep
        going..............'''
print(mls)

print("%s to the right "%('This is a string'))

print('this is print statement 1', end=" ")
print('this is print statement 2')

This = ("This "*10)

print(type(This))
print(This)


# # lists

colleges = ['IIT', 'NIT', 'College of engineering']

print(colleges[0])
print(colleges[1])
print(colleges[2])

colleges[2] = "COE"
print(colleges[2])
print(colleges)

print(colleges[1:3])

list2 = ['table', 'chair', 'fan', 'clothes', 'Bottle']
print(list2)

list2.append('micophone')
print(list2)
list2.insert(2, 'Apple')
print(list2)
list2.remove('Apple')
print(list2)

print(list2 + ['pillow', 'tubelight', 'bed'])
print(list2)
print(type(list2))

print(len(list2))
print(max(list2))
print(min(list2))


# # Tuples


tup1 = (1, 2, 3)
# tup1[0] = 6 # TypeError: 'tuple' object does not support item assignment
print(tup1[0])
print(tup1[1])
print(tup1[2])
print(tup1)
print(type(tup1))

# # How to Change tuples into list

tup2 = (4, 5, 6)
list1 = list(tup2)
print(list1)
print(type(list1))
list1[1] = "10"
print(list1[1])
print(tup2[0])
print(tup2[1])
print(list1)
print(tup2)

print(len(tup2))
print(max(tup2))
print(min(tup2))

print("-------------------------------")
# # Dictionaries

names = {'Himanshu': 21,
         'umesh': 15,
         'abhishek': 23,
         'ankit': 18}

print(names['Himanshu'])
names['Himanshu'] = 55
print(names['Himanshu'])
print(names)
print(names.keys())
print(names.values())

print("-------------------------------")

# # if elseif else statements

print("Enter Your Marks :)")
# numbers = int(input())
# print(numbers)

# if(numbers>90):
#     grade = 'A'
# elif(numbers>80):
#     grade = 'B'
# elif(numbers>50):
#     grade = 'C'
# elif(numbers>30):
#     grade = 'D'
# else:
#     grade = 'Do not know'
# print("The grade is", grade)


#  # AND opreter
# print("Enter Your Marks :)")
# numbers = int(input())
# print(numbers)

# if(numbers>90 and numbers<100):
#     grade = 'A'
# elif(numbers>80 and numbers<100):
#     grade = 'B'
# else:
#     grade = 'Do not know'
# print("The grade is", grade)

# # OR operter
# print("Enter Your Marks :)")
# numbers = int(input())
# print(numbers)

# if(numbers>90 or numbers<100):
#     grade = 'A'
# elif(numbers>80 or numbers<100):
#     grade = 'B'
# else:
#     grade = 'Do not know'
# print("The grade is", grade)

if(0 and 1):
    print("Yes")
else:
    print("NO")

if(0 or 1):
    print("Yes")
else:
    print("NO")

print(type(0))
print(type(1))

# # loop

# for loop

print("How many times do yu want to execute")
# no = int(input())
# for i in range(0,no):
    # print(i)

list1 = ['item1, item2, item3']
for item in list1:
    print(item)

list2 = [[1,2,3], [4,5,6], [7,8,9]]
for item in list2:
    for i in item:
        print(i)

for item in list2:
    print(item)

print(type(item))


# while loops

# print("Enter the number: ")
# number = int(input())

# while(number > 4):
#     print("Number is greater than 4")
#     number = int(input())
#     if (number == 9):
#         break
#     elif (number == 8):
#         continue
# print("loop ended")


# Function -------------------------------

def average(num1, num2):
    return(num1 + num2)/2

print(average(2, 8))
print(type(average))

# Strings

string = "this is me"
print(string[0:2])
print(string[-2:])
print(string[:-2])
print(string.capitalize())
print(string.find("this"))
print(string.find("is"))
print(string.replace("is", "are"))

print(type(string))


# File IO

file1 = open("Himanshu.txt", "wb")
print(file1.mode)
print(file1.name)
file1.write(bytes("Write this to my file", "UTF-8"))
file1.close()

# file io - reading the content of a file

file1 = open('Himanshu.txt', 'r+')
text_to_read = file1.read()
print(text_to_read)


# OOPS Object oriented programming

class Employee:
    __name = None
    __id = 0
    __salary = 0

    def __init__(self, name, id, salary):
        self.__name = name
        self.__id = id
        self.__salary = salary


    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_salary(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

# himanshu = Employee()
# print(himanshu.__name)
# himanshu.set_name('himanshu')
# print(himanshu.get_name())

# himanshu.set_id('himanshuch8055')
# print(himanshu.get_id())

# himanshu.set_salary('20000000000')
# print(himanshu.get_salary())

harry = Employee('harry', 489, 70000000)
print(harry.get_name())
print(harry.get_id())
print(harry.get_salary())

my_list = []
my_list += "Python"
print(my_list)