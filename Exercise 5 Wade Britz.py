# Question 1: Creating and Modifying Lists

# TODO: Create a list of fruits
fruits = ['Apple', 'Pear', 'Orange', 'Grape', 'Banana', 'Blueberry']
# TODO: Add a fruit to the end of the list
fruits.insert(6, 'lemon')
print(fruits)
# TODO: Insert a fruit at the beginning of the list
fruits.insert(0, 'strawberry' )
print(fruits)
# TODO: Remove a fruit from the list
fruits.pop(4)
# TODO: Print the modified list
print(fruits)

#-------------------------------------------------------------------------
# Question 2: List Operations

# TODO: Create a list of numbers from 1 to 5
num_list = [1,2,3,4,5]
# TODO: Create a new list with each number squared
num_square = [num**2 for num in num_list] 
# TODO: Find the sum and average of the original numbers
sum_numlist = sum(num_list)
avr_numlist = sum_numlist / len(num_list)
# TODO: Print the results
print(num_list)
print(f'The squared values of each number is: {num_square}')
print(f'The total of all the numbers in the list: {sum_numlist}')
print(f'The average of the numbers in the list: {avr_numlist}')

#-------------------------------------------------------------------------
# Question 3: Creating and Modifying Dictionaries

# TODO: Create a dictionary of countries and their capitals
countries_and_capital = {
    "United States": "Washington, D.C.",
    "England": "London",
    "Australia": "Perth",
    "India": "New Delhi",
    "Germany": "Berlin",
    "France": "Paris",
    "Japan": "Tokyo",
}
# TODO: Add a new country-capital pair
countries_and_capital['Slovakia'] = 'Bratislava'
print(countries_and_capital)
# TODO: Update the capital of an existing country
countries_and_capital.update({'Australia': 'Canberra'})
# TODO: Remove a country-capital pair
countries_and_capital.pop('Germany')
# TODO: Print the modified dictionary
print(countries_and_capital)

#-------------------------------------------------------------------------
# Question 4: Dictionary Operations

# TODO: Create a dictionary of fruit colors
fruits_and_colours = {
    "Apple": "red",
    "Pear": "green",
    "Banana": "yellow",
    "Tangerine": "orange"
    }
# TODO: Print all the fruits (keys)
print("Fruits:")
for fruits in fruits_and_colours:
    print(fruits)
# TODO: Print all the colors (values)
print("Colours: ")
for colours in fruits_and_colours.values():
    print(colours)

# TODO: Print each fruit and its color
for fruits, colours in fruits_and_colours.items():
    print(f'The colour of {fruits} is {colours}')
# TODO: Check if a fruit is in the dictionary and print its color
print('Insert fruit to check if its in the dictionary: ')
fruit_check = input('Enter name of fruit: ')

if fruit_check in fruits_and_colours:
    print(f'The fruit {fruit_check} is {fruits_and_colours[fruit_check]} and it is the dictionary')

else:
    print(f'{fruit_check} is not in the dictionary')