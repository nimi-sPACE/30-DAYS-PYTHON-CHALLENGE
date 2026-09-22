#prompts the user to  Declare an empty list
my_list = []
print(my_list)
#prompts the user to Declare a list with more than 5 items
my_list = ['Taiwo', 'Precious',  'Toluwanimi',  'Python',  'Programming']
print(my_list)
#prompts the user to Find the length of your list
print(len(my_list))
#prompts the user to Get the first item, the middle item and the last item of the list
print(my_list[0])
print(my_list[2])
print(my_list[4])
#prompts the user to Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Precious', 18, 5.6, 'Single',  'Lagos']
print(mixed_data_types)
#prompts the user to Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook',  'Google',  'Microsoft Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print(len(it_companies))

#prompts the user to Print the first, middle and last company
print(it_companies[0])
print(it_companies[3])
print(it_companies[5])

#prompts the user to Print the list after modifying one of the companies
it_companies[2] = 'Tiktok'
print(it_companies)
#prompt the user to Add an IT company to it_companies
it_companies.append('Twitter')
print(it_companies)
#prompt the user to Insert an IT company in the middle of the companies list
it_companies.insert(3,  'Snapchat')
print(it_companies)
#prompt the user to Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[0] = it_companies[0].upper()
print(it_companies)

#prompt the user to Join the it_companies with a string '#;  '
result=' #; ' .join(it_companies)
print(result)

#prompt the user to Check if a certain company exists in the it_companies list.
does_exist = 'IBM' in it_companies
print(does_exist)
does_exist = 'FACEBOOK' in it_companies
print(does_exist)

#PROMPT THE USER TO Sort the list using sort() method
it_companies.sort()
print(it_companies)
#prompt the user to Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)
#prompt the user to Slice out the first 3 companies from the list
the_first_three = it_companies[0:3]
print(the_first_three)
#prompt the user to Slice out the last 3 companies from the list
the_last_three = it_companies[5:]
print(the_last_three)
#prompt the user to Slice out the middle IT company or companies from the list
middle_index = len(it_companies) //2
print(it_companies[middle_index])
#prompt the user to Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)
#prompt the user to Remove the middle IT company or companies from the list
middle = len(it_companies) //2
it_companies.pop(middle)
print(it_companies)
#prompt the user to Remove the last IT company from the list
it_companies.pop()
print(it_companies)
#prompt the user to Remove all IT companies from the list
it_companies.clear()
print(it_companies)
#prompt the user to Destroy the IT companies list
del it_companies[0:]
print(it_companies)
#prompt the user to Join the following lists:
# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node','Express', 'MongoDB']
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print('Frontend and Backend:',front_end)
#prompt the user to After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack = front_end.copy()
full_stack.insert(5, 'python')
full_stack.insert(6, 'SQL')
print('Full Stack:', full_stack)

#LEVEL 2
#ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#prompt the user to Sort the list and find the min and max age
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
print(min(ages))
print(max(ages))
#prmpt the user to Add the min age and the max age again to the list
ages.append(min(ages))
ages.append(max(ages))
print(ages)
#prompt the user to Find the median age (one middle item or two middle items divided by two)
median_age = len(ages)//2
print(ages[median_age])
#prompt the user to Find the average age (sum of all items divided by their number )
average = sum(ages)/len(ages)
print(average)
#prompt the user to find the range of the ages (max minus min)
range = max(ages) - min(ages)
print(range)
#prompt the user to Compare the value of (min - average) and (max - average), use abs() method











