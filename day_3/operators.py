age = 18
height = 1.65
z = 2 + 5j 

#prompt the user to enter base and height of a triangle and calculate the area of the triangle
base = int(input('Enter base:'))
height = int(input('Enter height:'))
area = 0.5 * base * height
print('The area of the triangle is ', area)

#Finding the perimeter of a triangle
side_a = int(input('Enter side a:'))
side_b = int(input('Enter side b:'))
side_c = int(input('Enter side c:'))
perimeter = side_a + side_b + side_c
print('The perimeter of the triangle is', perimeter)

#Finding the area and perimeter of a rectangle
length = int(input('Enter the length:'))
width = int(input('Enter the width:'))
area = length * width
perimeter = 2 * (length + width)
print('The area of a rectangle is', area)
print('The perimeter of a rectangle is', perimeter)

#finding the area and circumference of a circle
radius = int(input('Enter Radius:'))
area = 3.14 * radius * radius
circumference = 2 * 3.14 *radius
print('The area of a circle is ', area)
print('The circumference of a circle is ', circumference)

#Finding slope , x-intercept, y- intercept,
#Equation = y = 2x - 2
#using the general equation y = mx+c
m = 2
c = -2

slope = m
#At x-intercept,make y = 0
x_intercept = -c/m
#At y-intercept, make x = 0
y_intercept = c
print('The slope is', slope)
print('The x_intercept is', x_intercept )
print('The y_intercept is',y_intercept  )

#Find the Slope and Euclidean Distance
x1 = 2 
x2 = 6
y1 = 2
y2 = 10
slope = (y2-y1 / x2-x1)
Euclidean_distance =  ((x2-x1)**2 + (y2-y1)**2) **0.5
print('The Slope is', slope)
print('The Euclidean Distance is', Euclidean_distance )

#Compare the slope in task 8 and 9
m1 = 2
m2 = 7.6666666666

if(m1 > m2):
    print('The first slope(m1) is greater' )
elif(m1 < m2):
    print('The second slope(m2) is greater ')
else:
    print('They are equal.')


#Prompts the user to calculate the value of y, Try to use different x values and figure out at what x values y is going to be 0
#The equation of y is (y = x^2 + 6x + 9)
#Using the values -5,-4,-3,-2,-1,0 for x.
x = -5
y = x**2 + 6*x + 9
print('x=', x, 'y=',y)
#When x is -4
x = -4
y = x**2 + 6*x + 9
print('x=', x, 'y=',y)
# when x is -3
x = -3
y = x**2 + 6*x + 9
print('x=', x, 'y=',y)
#when x is -2
x = -2
y = x**2 + 6*x + 9
print('x=', x, 'y=',y)
# when x is -1
x = -1
y = x**2 + 6*x + 9
print('x=', x, 'y=',y)
# when x is 0
x = 0
y = x**2 + 6*x + 9
print('x=', x, 'y=',y)

#Prompts the user to Find the length of 'python' and 'dragon' and make a falsy comparison state.
print(len('python'))
print(len('dragon'))
if (len('python') == len('dragon')):
    print('False!')
else:
    print('True!')

#prompts the user to  Use *and* operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python' and 'on' in 'dragon')

print('jargon' in 'I hope this course is not full of jargon')

#prompts the user to check if there is no 'on' in both dragon and python
print('on' not in 'python' and 'on' not in 'dragon')

#prompts the user to find the length of the text python and convert the value to float and convert it to string
print(len('python'))
print(float(len('python')))
print(str(float(len('python'))))

#Prompts the user to check if  a number is even or not
x = 10
if (x%2 == 0 ):
    print('Even Number')
else:
    print('Odd Number')

#Prompts the user to  Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print(7//3 == int(2.7))

print(type('10') == type(10))
print(int(float('9.8')) == 10)

#Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = int(input('Enter hours:'))
rate_per_hour = int(input('Enter rate per hour:'))
pay = hours*rate_per_hour
print('Your weekly earning is', pay)

#Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years = int(input('Enter number of years you have lived:'))
seconds = years * 365 *24 * 60 * 60
print('You have lived for', seconds, 'seconds.')

for i in range(1, 6):
    print(i, i**0, i**1, i**2, i**3)







