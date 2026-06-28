# check if the given number is present in the list or not
def numcheck():
    li = [2,4,8,6,33,67,99]
    target = int(input("Enter the target number you wanna search: "))
    for i in li:
        if i==target:
            print("your target is present in the list")
        elif i != target: 
            print("your target isn't here")
    
# find the max and min value from the given list
def minmax():
    li = [3,5,7,23,98,21,9,1]
    print(min(li))
    print(max(li))

# find all the even and odd number from the given list and  print them in seperate List
def evenodd():
    li= [4,7,9,8,23,56,98,25,79,63]
    even =[]
    odd = []
    for i in li:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    print(even)
    print(odd)
        
            
# print all the duplicate element from the list
def dupli():
    li = []
# print the number of occurrences of every  element in the list

# print the the square of every item in the list
def square():
    li = [3,6,8,9,2]
    squa=[]
    for i in li:
        squa.append(i*i)
    print(squa)
square()
