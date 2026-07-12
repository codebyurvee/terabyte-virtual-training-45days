# functions are the block of code to do a particular task
# creating function made code easy to read and debug(find error)
# it is good for memory utilization
# avoid code repeatition
# each function has unique name


# there are two type of function : pre-defined / user-defined
# syntax
# def is a keyword to create a function
#  function Define  here
# def doSomething():
#     print('function called')
#     print('function second line')
#
#
# print('before function call')
# # # # # # # # function called
# doSomething()
# doSomething()
# doSomething()
# print('after function call')
# doSomething()



# # First Type
# RNTN -> Returns Nothing Takes Nothing
# def add():
# # # # # local variable
#     a = int(input("Enter the First Number : "))
#     b = int(input("Enter the Second Number : "))
#     print(a+b)
# # # # # # #####function call
# add()
# add()

# Second Type
# RNTS -> Returns Nothing Takes Something
# def add(a,b):
#     sum=a+b
#     print(sum)
# #####
# p=int(input("Enter first number"))
# q=int(input("Enter second number"))
# add(p,q)
# add(100,2)
# add(200,150)

# Third Type
# RSTN
# def add():
    # x=int(input("Enter first number"))
    # y=int(input("Enter second number"))
#     # return the result from where it is called
#     sum=x+y
    # print(sum)
    # print(x+y)
    # return x+y
#     # this print statement is unreachable
#     print(x+y)
# # # #####
# add()
# res=add()
# print(res)
# print(add())
# print(res+5)
# add()
# #

# Fourth Type
# RSTS
# def add(a,b):

#     # return the result from where it is called
#     sum=a+b
    # print(sum)
    # print(x+y)
    # return sum
#     # this print statement is unreachable
#     print(x+y)
# # # #####
# res=add(100,50)
# print(res)
# print(add(200,100))
# print(res+5)
# add()

# # func -> receive only
# # func -> receive and return

# pow() -> pre-built function
# print(pow(6,3))
# # #

# print(9//2)
import math
print(math.floor(56.12))
print(math.ceil(56.12))
print(math.floor(math.sqrt(145)))
#1. Write a function to find the square of a number.
def square(a):
    print(a*a)

#2. Write a function to check whether a number is even or odd.
def numc(a):
    if a%2=0:
        print("even number")
    if a%2!=0:
        print("odd number")
#3. Write a function to return the sum of two numbers.
def sum(a,b):
    print(a+b)
    
#4. Write a function to find the factorial of a number.

#5. Write a function to find the maximum of three numbers.
def maxnm(a,b,c):
    if a>b and a>c:
        print(a)
    elif b>c and  b>a:
        print(b)
    else:
        print(c)
#6. Write a function to reverse a string.
def revs(a):
    print(a[::-1])
           
#7. Write a function that takes a list and returns the sum of all elements.
#8. Write a function to check whether a number is positive , Negative and zero.
