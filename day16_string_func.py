'''
#capitalize
str = "my name is Isha"

# case conversion string functions

print(str.capitalize())
#casefold
print(str.casefold())
#upper
print(str.upper())
#lower
print(str.lower())
#title
print(str.title())
#swapcase
print(str.swapcase())


#checking / testing string functions
x ="123456789"
#isnum
print(x.isalnum())
#check isalpha
print(str.isalpha())
#check isacii
print(str.isascii())
#check decimal
print(x.isdecimal())
#check digit
print(x.isdigit())
#check identifier
print(x.isidentifier())
#check lower
print(str.islower())
#check upper
print(str.isupper())
#check space
print(str.isspace())
#check isnumeric
print(x.isnumeric())
#check printable
print(str.isprintable())
#check title
print(str.istitle())


#Searching and finding string functions 7

h = "1. Keep moving forward—small steps today build big results today tomorrow."
#to find word index
print(h.find("today"))
#to find second word index
print(h.rfind("tomorrow"))
#to find index
print(h.index("today"))
#to find right side word's index
print(h.rindex("today"))
#to count the word
print(h.count("today"))
#to find it is start with return boolean
print(h.startswith("1"))
# to find it ends with return boolean
print(h.endswith("."))




    #splitting and joining functions 6
    #split
    a="hello jvd doos fjso everyoone"
    print(a.split(" ",8))

    #replit
    print(a.rsplit(",",8))

    #splitline
    print(a.splitlines())

    #join
    print(a.join("7"))

    #partition
    print(a.partition("7"))

    #rpartition
    print(a.rpartition("7"))

# Removing space / character 5
a= "     s      ijfm      "
print(a.strip()) #remove space from left & right
print(a.lstrip()) # remove left space
print(a.rstrip()) # remove right space

text = "luffy"
print(text.removeprefix("l")) # replace same starting part
print(text.removesuffix("y")) # replace same ending part
# replace with loop
text = "krishnaa"
for ch in text:
    text = text.replace(ch, "s",1)
print(text)

'''

#replacing and formatting string functions
print("hii".replace("hii","helooooo",3))
aaaa = "helloa"
print(aaaa.replace("a","h"))

name = "zoro"
print("luffy {}".format(na11me))



name = "syonnn"
clean = name.replace()

print(f"nanashi"
      f"+"
      f""
      f" {clean.title()}!")
# Welcome John Doe!
