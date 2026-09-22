![alt text](image.png)

WHAT I LEARNT:

# Boolean
A boolean data type represents one of the two values: True or False. The use of these data types will be clear once we start using the comparison operator. The first letter T for True and F for False should be capital unlike JavaScript. Example: Boolean Values

print(True)

print(False)

# Operators
Python language supports several types of operators. In this section, we will focus on few of them.

Assignment Operators:
Assignment operators are used to assign values to variables. Let us take = as an example. Equal sign in mathematics shows that two values are equal, however in Python it means we are storing a value in a certain variable and we call it assignment or a assigning value to a variable. The table below shows the different types of python assignment operators, taken from w3school.
![alt text](image-1.png)
Arithmetic Operators:
Addition(+): a + b

Subtraction(-): a - b

Multiplication(*): a * b

Division(/): a / b

Modulus(%): a % b

Floor division(//): a // b

Exponentiation(**): a ** b
![alt text](image-2.png)

Example : Integers
```python
# Arithmetic Operations in Python
# Integers

print('Addition: ', 1 + 2)        # 3
print('Subtraction: ', 2 - 1)     # 1
print('Multiplication: ', 2 * 3)  # 6
print ('Division: ', 4 / 2)       # 2.0  Division in Python gives floating number
print('Division: ', 6 / 2)        # 3.0         
print('Division: ', 7 / 2)        # 3.5
print('Division without the remainder: ', 7 // 2)   # 3,  gives without the floating number or without the remaining
print ('Division without the remainder: ',7 // 3)   # 2
print('Modulus: ', 3 % 2)         # 1, Gives the remainder
print('Exponentiation: ', 2 ** 3) # 8 it means 2 * 2 * 2
```
Example : Floats
```python
# Floating numbers
print('Floating Point Number, PI', 3.14)
print('Floating Point Number, gravity', 9.81)
```
Example : Complex numbers.
```python
# Complex numbers
print('Complex number: ', 1 + 1j)
print('Multiplying complex numbers: ',(1 + 1j) * (1 - 1j))
```

# Comparison Operators
In programming we compare values, we use comparison operators to compare two values. We check if a value is greater or less or equal to other value. The following table shows Python comparison operators which was taken from w3shool.
![alt text](image-3.png)
Example: Comparison Operators
```python
print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False


# Comparing something gives either a True or False

print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)
```
# Logical Operators
Unlike other programming languages python uses keywords and, or and not for logical operators. Logical operators are used to combine conditional statements:
![alt text](image-4.png)
Example: Logical OPerators
```python
print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print('True and True: ', True and True)
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statements is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print('True or False:', True or False)
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False
```



