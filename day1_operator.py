#i useed assignment /relational operators 
def arithemeticop():
    try:
        a = int(input("enter a number"))
        b = int(input("enter second number"))
        choice = input("Enter a option(addition:+,subtraction:-,division:/,multiplication:*,exponent:^,modulus:%,floor division://)")
    
        if choice == '+':
            print(a+b)
        elif choice == '-':
            print(a-b)
        elif choice == '*':
            print(a*b)
        elif choice == '/':
            print(a/b)
        elif choice == '//':
            print(a//b)
        elif choice == '%':
            print(a%b)
        elif choice == '^':
            print(a**b)     
    except ValueError:
        print("its an value error")
arithemeticop()
