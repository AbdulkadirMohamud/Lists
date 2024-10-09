empty_list = list() # this is an empty list,  no item in the list 
print(len (empty_list)) # 0

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'avocado', 'carrot', 'blueberries']
animal_products = ['yoghurt', 'beef', 'chicken', 'fish']
web_techs = ['HTML', 'CSS', 'JS', 'React' 'Python', 'Node', 'MongoDB', 'MySQL',]
countries = ['DenMark', 'Netherlands', 'Australia', 'Qatar', 'Spain', 'Lebanon,']

# print the lists and it length
print('Fruits:', fruits) 
print('Numbers of fruits:', len (fruits))
print('Vegetables:',  vegetables)
print('Animal products:', animal_products)
print('Number of animal products:', len (animal_products))
print('Number of web technologies:', len(web_techs))
print('Number of countries:', len(countries))

# modifying list

fruits = ['banana', 'orange', 'mango', 'lemon', ]
first_fruit = fruits [0] # we are accessing the first item using its index
print(first_fruit) # banana
second_fruit = fruits [1]
print(second_fruit) # orange
last_fruit = fruits [3]
print(last_fruit) # lemon
# last index
last_index = len(fruits) -1
last_fruit = fruits[last_index]

# accessing items
fruits = ['banana', 'orange', 'mango', 'lemon', ]
last_fruit = fruits [-1]
second_fruit = fruits [-2]
print(last_fruit) # lemon
print(second_fruit) # mango

# slicing items
fruits = ['banana', 'orange', 'mango', 'lemon', ]
all_fruits = fruits [0:4]
some_fruits = fruits [1:3]
print(all_fruits) # ['banana', 'orange', 'mango', 'lemon']
print(some_fruits) # ['orange', 'mango']
fruits = ['banana', 'orange', 'mango', 'lemon', ]
fruits[0] = 'avocado'
print(fruits) # ['avocado', 'orange', 'mango', 'lemon']
fruits [1] = 'apple'
last_index = len(fruits) -1
fruits [last_index] = 'lime'
print(fruits) # ['avocado', 'apple', 'mango', 'lime']

# checking items in list
fruits = ['banana', 'orange', 'mango', 'lemon', ]
print('banana' in fruits) # True
print('apple' in fruits) # False

# insert 
fruits = ['banana', 'orange', 'mango', 'lemon', ]
fruits.insert(2, 'apple')
print(fruits) # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, 'lime') # ['banana', 'orange', 'apple', 'lime', 'mango', 'lemon']
print(fruits)

# remove 
fruits = ['banana', 'orange', 'mango', 'lemon', ]
fruits.remove('banana')
print(fruits) # ['orange', 'mango', 'lemon']
fruits.remove('lemon')
print(fruits) # ['orange', 'mango']

# pop
fruits = ['banana', 'orange', 'mango', 'lemon', ]
fruits.pop()
print(fruits) # ['banana', 'orange', 'mango']

# del
fruits = ['banana', 'orange', 'mango', 'lemon', ]
del fruits[0]
print(fruits) # ['orange', 'mango', 'lemon']
del fruits
# print(fruits) # NameError: name 'fruits' is not defined

# clear
fruits = ['banana', 'orange', 'mango', 'lemon', ]
fruits.clear()
print(fruits) # []

# copying a lists
fruits = ['banana', 'orange', 'mango', 'lemon', ]
fruits_copy = fruits.copy()
print(fruits_copy) # ['banana', 'orange', 'mango', 'lemon']

# join
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-1, -2, -3, -4, -5]
integers = positive_numbers + zero + negative_numbers
print(integers) 
fruits = ['banana', 'orange', 'mango', 'lemon', ]
vegetables = ['Tomato', 'avocado', 'carrot', 'blueberries']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)

# join with extend
num1 = [0, 1, 2, 3]
num2 = [4, 5, 6,]
num1.extend(num2)
print('Numbers:', num1)
negative_numbers [-5, -4, -3, -2, -1]
positive_numbers [1, 2, 3, 4, 5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers)
fruits = ['banana', 'orange', 'mango', 'lemon', ]
vegetables = ['Tomato', 'avocado', 'carrot', 'blueberries']
fruits.extend(vegetables)
print('Fruits and vegetables:', fruits)

# count 
fruits = ['banana', 'orange', 'mango', 'lemon', ]
print(fruits.count('banana')) # 1
ages = [22,19,24, 25, 26,24, 25,24]
print(ages.count(24))
# reverse
fruits = ['banana', 'orange', 'mango', 'lemon', ]
fruits.reverse()
print(fruits)
ages = [22,19,24, 25, 26,24, 25,24]
ages.reverse()
print(ages)

# sort
fruits = ['banana', 'orange', 'mango', 'lemon', ]
fruits.sort()
print(fruits)
ages = [22,19,24, 25, 26,24, 25,24]
ages.sort()
print(ages)
ages.sort(reverse = True)
print(ages)



