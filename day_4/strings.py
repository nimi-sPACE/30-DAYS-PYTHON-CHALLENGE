#prompts the user to  Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
first_name = 'Thirty'
second_name = 'Days'
third_name = 'of'
last_name = 'Python'
space = ' '
full_name = first_name + space + second_name + space + third_name + space + last_name
print(full_name)

#prompts the user to Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
first_name = 'Coding'
second_name = 'For'
last_name = 'All'
space = ' '
full_name = first_name + space + second_name + space + last_name
print(full_name)

#prompts the user to Declare a variable named company and assign it to an initial value "Coding For All".

company = 'Coding For All'
print(company)
print(len(company))

#prompts the user to Change all the characters to uppercase letters using upper() method.
print(company.upper())
print(company.lower())

#Prompts the user to Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

#Prompts the user to Cut(slice) out the first word of Coding For All string.
first_word = company[0:6]
print(first_word)

#prompts the user to Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.find('Coding')!= -1)

#PROMPTS THE USER TO Replace the word coding in the string 'Coding For All' to Python
print(company. replace('Coding', 'Python'))

#prompts the user to Change "Python for Everyone" to "Python for All" using the replace method or other methods.
challenge = 'Python for Everyone'
print(challenge.replace('Everyone', 'All'))

#prompts the user to Split the string 'Coding For All' using space as the separator (split()) .
print(company.split(','))

#prompts the user to "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
apps = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(apps.split(','))

#prompts the user to find the character at index 0 in the string Coding For All
print(company[0])

#prmpts the user to find the last index of the string Coding For All.
print(len(company) -1)

#prompts the user Create an acronym or an abbreviation for the name 'Python For Everyone'.
name = 'Python For Everyone'
words = name.split() 
acronym = words[0][0] + words[1][0] + words[2][0]
print(acronym)

#prompts the user to create an acronym or an abbreviation for the name 'Coding For All'.
name = 'Coding For All'
words = name.split()
acronym = words[0][0] +words[1][0] + words[2][0]
print(acronym)

 #prompts the user to Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index('C'))
#prompts the user to Use index to determine the position of the first occurrence of F in Coding For All.
print(company.index('F'))
#prompts the user to Use rfind to determine the position of the last occurrence of l in Coding For All People.
Enterprise = 'Coding For All People'
print(Enterprise.rfind('l'))
#prompts the user to Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
Sentence = 'You cannot end a sentence with because because because is a conjunction'
print(Sentence.index('because'))
#prompts the user to Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(Sentence.rfind('because'))
#prompts the user to Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
Sentence = 'You cannot end a sentence with because because because is a conjunction'
print(Sentence[31:54])
#prompts the user to Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(Sentence.find('because'))
#prompts the user to find out 'Coding For All' start with a substring Coding?
print(company.startswith('Coding'))
#prompts the user to find out if 'Coding For All' end with a substring coding?
print(company.endswith('coding'))

#prompts the user to '   Coding For All      '  , remove the left and right trailing spaces in the given string.
text = '  Coding For All   '
print(text.strip())

#prompts the user to figure out Which one of the following variables return True when we use the method isidentifier():
challenge = '30DaysOfPython'
print(challenge.isidentifier())
Challenge = 'thirty_days_of_python'
print(Challenge.isidentifier())

#prompts the user to The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
list = ['Django', 'Flask',  'Bottle',  'Pyramid',  'Falcon']
print(' # '.join(list))

#prompts the user to Use the new line escape sequence to separate the following sentences.
sentence_a = 'I am enjoying this challenge'
sentence_b = 'I just wonder what is next'
print(sentence_a + '\n' + sentence_b)

#prompts the user to Use a tab escape sequence to write the following lines.
#'Name'      'Age'     'Country'   'City'
#'Asabeneh'  '250'     'Finland'   'Helsinki'
print('Name\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinki')

#prompts the user to Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
radius = 10
area = 3.14*radius**2
print('The area of a circle with radius {} is {} meters square.'.format(radius,area))

#prompts the user to Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144

a = 8
b = 6
print('{} + {} = {}'.format(a,b,a+b))
print('{} - {} = {}'.format(a,b,a-b))
print('{} * {} = {}'.format(a,b,a*b))
print('{} / {} = {}'.format(a,b,a/b))
print('{} % {} = {}'.format(a,b,a%b))
print('{} // {} = {}'.format(a,b,a//b))
print('{} ** {} = {}'.format(a,b,a**b))





