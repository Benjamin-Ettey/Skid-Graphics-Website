# n=int(input("Enter any number: "))

# sum=0
# while (n>0):
#     d=n%10
#     sum=sum+d
#     n=n//10
# print(sum)

# from array import *
# name = array('i', [1,2,3,4,4,5,66])
# name1=array('i', [10,2,3,4,5,6,7])
# for x in name:
#     for a in x:
#         print(x)
#a=[1,2,3,4,4]
#a.reverse()
#print(a)
#b=a.copy()
#print(b)

#a=("Benjamin","Ettey","23","56")
#print(a[2])


#Ben [Ettey] is studious
#First_name=input("Enter your firstname: ")
#Second_name=input("Enter your surname: ")

#print(f'{First_name} {[Second_name]} {"is studious."}')


# command=""
# started=False
# while True:
#     command=input(">").lower()
#     if command=="start":
#         if started:                                     #so you have to use a boolean function to initiate these commands
#             print("Car start dey move longest oo")
#         else:
#             started=True
#             print("The car dey move.")
        
        
#     elif command=="stop":
#         if not started:
#             print("car stop longest oo")
#         else:
#             started=False
#             print("The car shun dey move.")
        
#     elif command=="help":
#         print("""
# Start: The Car is moving
# Stop: The Car has stopped
# Quit: You quit the game.""")
#     elif command=="quit":
#         print("gameover")
#         break

#coordinates system
# for x in range(4):
#     for y in range(3):
#         print(f'({x}, {y})')


# numbers=[5,2,5,2,2]

# for number in numbers:
#     for x in numbers:
#         print(f'{number*"x"} ')
#         break

# for x_count in numbers:
#     output=""
#     for count in range(x_count):
#         output+="x"
#     print(output)

# matrix=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# print(matrix[0][2])
# matrix.append()
# matrix.insert()

#removing duplicates in lists
# number=[2,3,4,5,4,4,3,2]
# unique=[]

# for num in number:
#     if num not in unique:
#         unique.append(num)

# print(unique)

#unpacking lists
# coordinates=(1,2,9)
# x,y,z = coordinates
# print(x,y,z)

#dictionary

# customer={
#     "name":"Ettey",
#     "age":"20",
#     "email":"etteyben@gmail.com"
# }

# print(customer.get("Name", "all typing must be in small letters."))

#assigning chaacters to their word form
# input("phone: ")
# output=""
# number={
#     "1":"one",
#     "2":"two",
#     "3":"three"
# }

# for i in number:
#     output+=number.get(i,"small letters.")
# print(output)


#dictionary emoji coverter
# message=input(">")
# words=message.split(' ')

# emoji_tab={
#     ":)":"😊",  
#     ":(":"😔"
#  }
# output=""
# for word in words:
#     output+=emoji_tab.get(word, word) +" "

# print(output)


# def greet_user(first_name, second_name):
#     print(f'Hi {first_name} {second_name}!')


# greet_user("Ben", "Ettey")


#exception to prevent program crashing
# try:
#     age=int(input("Enter your age: "))
#     print(age)
# except ValueError:
#     print("Type in a number")

# class Point:
#     def __init__(self,x,y):  #constructor
#         self.x=x
#         self.y=y
#     def move(self):
#         print("move")
#     def draw(self):
#         print("draw")
    

# point=Point(10,2)
# print(point.x)
# point.draw()
# point.x=10   #attributes


#classes explained
# class Person:
#     def __init__(self, name):
#         self.name=name
#     def talk(self):
#         print(f'Hi {self.name}')


# Jon=Person("Ben")
# Jon.talk()

#inheritance

# class Mammal:
#     def walk(self):
#         print("walk")

# class Cat(Mammal):
#     pass

# cat1=Cat()
# cat1.walk()

#modules
# makes code better by section them into new files and calling them in another function


#random, random selecting, random number generte
# import random

# for i in range(3):
#     print(random.randint(10, 20))
    
# import random

# members=['Ben', 'Ettey', 'Mary', 'Agnes']

# leader=random.choice(members)

# print(leader)



# import random
# roll=(1, 2, 3, 4, 5, 6)
 # choice=random.choice(roll)
 # print(choice)

# for i in roll:
#     for a in roll:
#         i=random.i(roll)
#         a=random.a(roll)
# print(f'{i}, {a}')

# import random
# class Dice:
#     def roll(self):
#         first=random.randint(1, 6)
#         second=random.randint(1, 6)
#         return first, second
    
# outcome=Dice()
# print(outcome.roll())

from pathlib import Path

path=Path("ecommence")

print(path.exists())