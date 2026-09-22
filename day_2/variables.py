first_name = 'Taiwo Precious'
last_name = 'Toluwanimi'
full_name = 'Taiwo Precious Toluwanimi'
country = 'Nigeria'
city = 'Lagos'
age = 18
year = 2008
is_married = 'No'
is_true = 'No'
is_light_on = 'Yes'

first_name, last_name, full_name, country, city, age, is_married = 'Taiwo Precious','Toluwanimi','Taiwo Precious Toluwanimi','Nigeria', 'Lagos', 18, 'No'

# Check the Data type of all my variables 
print(type('Taiwo Precious'))
print(type('Toluwanimi'))
print(type('Taiwo Precious Toluwanimi'))
print(type('Nigeria'))
print(type('Lagos'))
print(type(18))
print(type(2008))
print(type('No'))
print(type('No'))
print(type('Yes'))

print(len('Taiwo Precious'))

if len(first_name) > len(last_name):
    print('First name is longer')
else:
    print('Last name is longer')

num_1= 5
num_2 = 4

Total= 5+4
Difference = 5-4
Product = 5*4
Division = 5/4
Remainder = 5%4
exp = 5**4
floor_division = 5//4
#Display result
print(Total)
print(Difference )
print(Product )
print(Division )
print(Remainder )
print(exp)
print(floor_division )

#Finding Area of a Circle
import math
radius = int(input('Enter the radius of the circle:'))
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print('Area', area)
print('Circumference', circumference)

#get the variable
first_name = input('Enter your first name:')
last_name = input('Enter your last name:')
country = input('Enter your Country:')
age = input('Enter your Age:')

help('keywords')
