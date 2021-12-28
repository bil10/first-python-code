# code to identify the version of python

import sys
print("Python version")
print (sys.version)


# code to print the poem

print('Twinkle, twinkle. little star')
print('         How I wonder what you are!')
print('                 Up above the world so high,')
print('                 Like a diamond in the sky.')
print('Twinkle, twinkle, little star,')
print('        How I wonder what you are')

# code for current date and time

import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

# code for computing the area of circle

PI = 3.14
radius = float(input(' Please Enter the radius of a circle: '))
area = PI * radius * radius
print(" Area Of a Circle = %.2f" %area)

# code for first and last name

f = input ('Enter your first name')
l = input ('Enter your last name')

print(l,f)

# code for addtion of two inputs

a = int(input('Enter first number'))
b = int(input('Enter second number'))
c = a+b
print(c)








