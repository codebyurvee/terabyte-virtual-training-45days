#while loop 
# 1. print the table of 2,3,7,9 in normal and reverse order
#2. print the table of number entered by user
#3. print this table again in format 2x1=2 ...2x2=4..............2x10=20
def table():
  i = int(input("Enter a number for table: "))
  j = 0
  while j<= 10:
    a=j*i
    print(i,"x",j,"=",a)
    j+=
    
def table_reverse():
  i = int(input("Enter a number for table: "))
  j = 10
  while j >= 1:
    a=j*i
    print(i,"x",j,"=",a)
    j-=1
    
# sum of first 5 natural number
def sum():
  i = 0
  total = 0
  while i<=5:
      total+= i
      i+=1
  print(total)
sum()
  
# multiply of first 5 natural numbers
# factorial(5-> 5x4x3x2x1 => 120)
# factorial(5-> 5x4x3x2x1 => 120)
def multiply():
  i = 1
  total = 1
  while i<=5:
      total*= i
      i+=1
  print(total)
multiply()

# reverse number (452 -> 254)
def reverse():
  num = 452
  new_num = 0
  while num > 0:
    reminder = num%10
    new_num = (new_num*10)+reminder
    num = num//10
  print("reverse number",new_num)
    
  
# pallindrome number(121 <-> 121)
  def palli():
  
# fibonnacci series : 01123581321
# check if the given number is prime or not (2,3,5,7,11,13,17,19.....)
