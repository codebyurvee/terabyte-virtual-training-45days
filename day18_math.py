This program will show the calculation of square root using the math module

importing the math module

import math

print(math.floor(math.sqrt( 9 )))

print(math.sqrt(9))

Euler's Number

math.e

# importing the required library

import math

#

# # # printing the value of Euler's number using the math module

print("The value of Euler's Number is: ", math.e)

Tau

The ratio of a circle's circumference to its radius is known as tau.

math.tau

# Importing the required library

import math



# Printing the value of tau using math module

print("The value of Tau is: ", math.tau)



Infinity

Infinity refers to anything limitless or never-ending in both directions of the actual number line. Numbers cannot adequately represent it. The math.inf returns positive infinity constant. We can use -math.inf to print negative infinity.

math.inf



# Importing the required library

import math



# Printing the value of positive infinity using the math module

print(math.inf)

#

# # # # Printing the value of negative infinity using the math module

print(-math.inf)

# Importing the required library

import math



# comparing the value of infinity

print(math.inf > 10e109)

print(-math.inf < -10e109)

Pi

Pi is known to everyone. It is mathematically represented as either the fraction 22/7 or the decimal number 3.14. math.pi gives the most accurate value of pi.

math.pi

# Importing the required library

import math



# # Printing the value of pi using the math module

print("The value of pi is ", math.pi)

# # Importing the required library

import math

#

# # # radius of the circle

r = 4



# # value of pi

pi_value = math.pi



# # circumference of the circle

print(2 * pi_value * r)

NaN

The math.nan gives us a floating-point nan (Not a Number) value. This amount is not a valid numeric value. Float("nan") and the nan constant are comparable.

Importing the required library

import math



# Printing the value of nan using the math module

print(math.nan)

Calculating the Ceiling and the Floor Value

# importing the math module

import math



x = 4.346



# # returning the ceiling value of 4.346

print("The ceiling value of 4.346 is : ", end="")

print(math.ceil(x))

#

# # # returning the floor value of 4.346

print("The floor value of 4.346 is : ", end="")

print(math.floor(x))

Calculating the Factorial of the Number

# importing the math module

import math



x = 6



# returning the factorial of 6

print("The factorial of 6 is : ", math.factorial(x))

# passing a non integral number

try:

print("The factorial of 6.5 in: ", math.factorial(6))

except:

print("Cannot calculate factorial of a non-integral number")

Calculating the Absolute Value

importing the math module

import math



x = -45



# returning x's absolute value.

print("The absolute value of -45 is: ", math.fabs(x))

Calculating the Exponential

importing the math module

import math



# # declaring some value

num1 = 4

num2 = -3

num3 = 0.00



# passing above values to the exp() function

print(f"The exponenetial value of {num1} is: ", math.exp(num1))

print(f"The exponenetial value of {num2} is: ", math.exp(num2))

print(f"The exponenetial value of {num3} is: ", math.exp(num3))

Calculating the Power of a Number

importing the math module

import math



x = 4

y = 5

# returning x to the power of y.

print(f"The value of {x} to the power of {y} is: ", math.pow(x, y))

Calculating Sine, Cosine, and Tangent

importing the math module

import math

#

angle = math.pi / 5

print(angle)



# returning the sine of pi/4

print("The sine of pi/4 is : ", math.sin(angle))



# # returning the cosine of pi/4

print("The cosine of pi/4 is : ", math.cos(angle))



# # returning the tangent of pi/4

print("The tangent of pi/4 is : ", math.tan(angle))

The dir( ) Function

Importing the math module

import math

# #

functions = dir(math)

print(functions)

import math



print(math.ceil(4.86))

how to practice this




import math

print(math.sqrt(4))
print(math.pow(2,4))
p= math.factorial(5)
print(p)
r = math.ceil(6.3)
print(r)
m = math.floor(4.5)
print(m)
k = math.fabs(-7)
print(k)
am = math.exp(9)
print(am)
sin = math.sin(14)
print(sin)
cos = math.cos(56)
print(cos)
tan = math.tan(4)
print(tan)
pi = math.pi(3.14)
print(pi)
e = math.e(3.483)
print(e)
