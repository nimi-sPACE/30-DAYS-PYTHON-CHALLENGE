WHAT I LEARNT 
~ Built in functions
In Python we have lots of built-in functions. Built-in functions are globally available for your use that mean you can make use of the built-in functions without importing or configuring. Some of the most commonly used Python built-in functions are the following: print(), len(), type(), int(), float(), str(), input(), list(), dict(), min(), max(), sum(), sorted(), open(), file(), help(), and dir(). In the following table you will see an exhaustive list of Python built-in functions taken from python documentation.
![alt text](image.png)

VARIABLES: 
Variables store data in a computer memory. Mnemonic variables are recommended to use in many programming languages. A mnemonic variable is a variable name that can be easily remembered and associated. A variable refers to a memory address in which data is stored. Number at the beginning, special character, hyphen are not allowed when naming a variable. A variable can have a short name (like x, y, z), but a more descriptive name (firstname, lastname, age, country) is highly recommended.

Python Variable Name Rules

A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (firstname, Firstname, FirstName and FIRSTNAME) are different variables)

Here are some example of valid variable names:

firstname,
lastname,
age,
country,
city,
first_name,
last_name,
capital_city,
 # if we want to use reserved word as a variable
year_2021,
year2021,
current_year_2021,
birth_year,
num1,
num2,

INVALID VARIABLE NAMES:

first-name, 
first@name, 
first$name, 
num-1, 
1num.

We will use standard Python variable naming style which has been adopted by many Python developers. Python developers use snake case(snake_case) variable naming convention. We use underscore character after each word for a variable containing more than one word(eg. first_name, last_name, engine_rotation_speed). The example below is an example of standard naming of variables, underscore is required when the variable name is more than one word.

When we assign a certain data type to a variable, it is called variable declaration. For instance in the example below my first name is assigned to a variable first_name. The equal sign is an assignment operator. Assigning means storing data in the variable. The equal sign in Python is not equality as in Mathematics.






# Declaring Multiple Variable in a Line
Declaring Multiple Variable in a Line
Multiple variables can also be declared in one line:

Example:

first_name, last_name, country, age, is_married = 'Taiwo', 'Precious', 'Nigeria', 18, True

print(first_name, last_name, country, age, is_married)

print('First name:', first_name)

print('Last name: ', last_name)

print('Country: ', country)

print('Age: ', age)

print('Married: ', is_married)

Getting user input using the input() built-in function. Let us assign the data we get from a user into first_name and age variables. Example:

first_name = input('What is your name: ')

age = input('How old are you? ')

print(first_name)

print(age)


# DATA TYPES
Data Types
There are several data types in Python. To identify the data type we use the type built-in function. I would like to ask you to focus on understanding different data types very well. When it comes to programming, it is all about data types. I introduced data types at the very beginning and it comes again, because every topic is related to data types. We will cover data types in more detail in their respective sections.

CHECKING DATA TYPES AND CASTING
Check Data types: To check the data type of certain data/variable we use the type Examples:
# Different python data types
Let's declare variables with various data types

first_name = 'Taiwo'     # str

last_name = 'Precious'       # str

country = 'Nigeria'         # str

city= 'Ogun'            # str

age = 18                 # int, it is not my real age, don't worry about it


# Printing out types
print(type('Taiwo'))          # str

print(type(first_name))          # str

print(type(10))                  # int

print(type(3.14))                # float

print(type(1 + 1j))              # complex

print(type(True))                # bool

print(type([1, 2, 3, 4]))        # list

print(type({'name':'Precious'})) # dict

print(type((1,2)))               # tuple

print(type(zip([1,2],[3,4])))    # zip


Casting: Converting one data type to another data type. We use int(), float(), str(), list, set When we do arithmetic operations string numbers should be first converted to int or float otherwise it will return an error. If we concatenate a number with a string, the number should be first converted to a string. We will talk about concatenation in String section.

Examples:

# int to float
num_int = 10

print('num_int',num_int)         # 10

num_float = float(num_int)

print('num_float:', num_float)   # 10.0

# float to int
gravity = 9.81

print(int(gravity))             # 9

# int to str
num_int = 10

print(num_int)                  # 10

num_str = str(num_int)

print(num_str)                  # '10'

# str to int or float
num_str = '10.6'

num_float = float(num_str)  # Convert the string to a float first

num_int = int(num_float)    # Then convert the float to an integer

print('num_int', int(num_str))      # 10

print('num_float', float(num_str))  # 10.6

num_int = int(num_float)

print('num_int', int(num_int))      # 10


# str to list
first_name = 'Asabeneh'

print(first_name)               # 'Asabeneh'

first_name_to_list = list(first_name)

print(first_name_to_list)            # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']




# Numbers
Number data types in Python:

1.Integers: Integer(negative, zero and positive) numbers Example: ... -3, -2, -1, 0, 1, 2, 3 ...

2.Floating Point Numbers(Decimal numbers) Example: ... -3.5, -2.25, -1.0, 0.0, 1.1, 2.2, 3.5 ...

3.Complex Numbers Example: 1 + j, 2 + 4j, 1 - 1j


EXERCISES: Level 1
Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
Write a python comment saying 'Day 2: 30 Days of python programming'

Declare a first name variable and assign a value to it

Declare a last name variable and assign a value to it

Declare a full name variable and assign a value to it

Declare a country variable and assign a value to it

Declare a city variable and assign a value to it

Declare an age variable and assign a value to it

Declare a year variable and assign a value to it

Declare a variable is_married and assign a value to it

Declare a variable is_true and assign a value to it

Declare a variable is_light_on and assign a value to it

Declare multiple variable on one line


# EXERCISES: Level 2

1.Check the data type of all your variables using type() built-in function

2.Using the len() built-in function, find the length of your first name

3.Compare the length of your first name and your last name

4.Declare 5 as num_one and 4 as num_two

5.Add num_one and num_two and assign the value to a variable total

6.Subtract num_two from num_one and assign the value to a variable diff

7.Multiply num_two and num_one and assign the value to a variable product

8.Divide num_one by num_two and assign the value to a variable division

9.Use modulus division to find num_two divided by num_one and assign the value to a variable remainder

10.Calculate num_one to the power of num_two and assign the value to a variable exp

11.Find floor division of num_one by num_two and assign the value to a variable floor_division

12.The radius of a circle is 30 meters.

13.Calculate the area of a circle and assign the value to a variable name of area_of_circle

14.Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle

15.Take radius as user input and calculate the area.

16.Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names

17.Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords