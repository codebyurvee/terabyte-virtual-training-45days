# conditional statements
#Question 1:Check if a number is positive.
def positive():
  number = int(input("Enter a number: "))
  if number > 0 :
    print("your number is positive" , number)
    
#Question 2:Check if a number is even or odd.
def evenodd():
  num = int(input("enter a number: "))
  if num%2 ==0:
    print("it is even number")
  if num%2!=0:
    print("it is an odd number")

#Question 3:Check if a person is eligible to vote (age ≥ 18).
def vote():
  age = int(input("enter your age: "))
  if age >= 18:
    print("you are eligible for vote")
  if age<18: 
    print("you r not eligible for vote")

#Question 4:Find the greatest of two numbers.
def bignum():
  a = int(input("enter firstt number: "))
  b = int(input("enter second number: "))
  if a>b:
    print(a,"is greater than",b)
  if a<b:
    print(b,"is greater than",a)
  if a==b:
    print("both are same: ")

#Question 5:Check if a year is a leap year.
def yearcheck():
  year = int(input("enter year: "))
  if year%4==0:
    print("it is leap year")
  if year%4!=0:
    print("it is not leap year")

#Question 6:Check if a number is negative, positive, or zero.
def numcheck():
  num = int(input("enter a number: "))
  if num > 0:
    print("positive")
  if num <0:
    print("negative")
  if num == 0:
    print("zero")

  
