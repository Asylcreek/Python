##current_year = 2020;
##birth_year = int(input("Enter your birth year: "));
##
# print(f'You are {current_year - birth_year} years old')


##username = input('Enter your username: ');
##password = input('Enter your password: ');
##
# print(f"Hey {username.capitalize()}, your password {'*' * len(password)} is {len(password)} characters long")

# picture = [[0,0,0,1,0,0,0],
# [0,0,1,1,1,0,0],
# [0,1,1,1,1,1,0],
# [1,1,1,1,1,1,1],
# [0,0,0,1,0,0,0],
# [0,0,0,1,0,0,0]
# ]
##
# for i in range(len(picture)):
# for j in range(len(picture[i])):
# if picture[i][j] == 0:
##            picture[i][j] = ' '
# else:
##            picture[i][j] = 1
##        print(picture[i][j], end=" ")
# print()

# def highest_even(list):
#     '''This function prints the highest even number in a list'''

#     for i in range(len(list)):
#         maximum_value = max(list)

#         if maximum_value % 2 == 0:
#             return maximum_value
#         else:
#             list.remove(maximum_value)

# print(highest_even([2,8,9]))


# Object Oriented Programming

# class PlayerCharacter:
# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age


# 	def run(self):
# 		return 'run'


# player1 = PlayerCharacter('Moses', 45)
# player2 = PlayerCharacter('Jane', 35)


# print(player1.name, player1.age)
# print(player2.name, player2.age)


# First Exercise Objects

# class Cat():

#     species = 'mammal'

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# moses = Cat('Moses', 24)
# jane = Cat('Jane', 12)
# moody = Cat('Moody', 26)

# # better way would be to remove this
# cat_list = [moses.age, jane.age, moody.age]


# def oldest_cat(_list):  # and use *args as the parameter here
#     return max(_list)


# # so that here would just be oldest_cat(moses.age, jane.age, moody.age)
# x = oldest_cat(cat_list)

# print(f'The oldest cat is {x} years old')

# Second OOP Exercise

# class Pets():
#     animals = []

#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())


# class Cat():

#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'


# class Simon(Cat):

#     def sing(self, sounds):
#         return f'{sounds}'


# class Sally(Cat):

#     def sing(self, sounds):
#         return f'{sounds}'


# class Moses(Cat):

#     def sing(self, sounds):
#         return f'{sounds}'


# cat1 = Simon('Cat1', 12)
# cat2 = Sally('Cat2', 13)
# cat3 = Moses('Cat3', 14)

# my_cats = [cat1, cat2, cat3]

# my_pets = Pets(my_cats)

# my_pets.walk()


# Third Exercise OOP

# Exercise Functional Programming

# from functools import reduce

# my_pets = ['sisi', 'bibi', 'titi', 'carla']

# def capitalize(item):
#     	return item.upper()

# print(list(map(capitalize, my_pets)))

# my_strings = ['a', 'b', 'c', 'd', 'e']

# my_numbers = [5, 4, 3, 2, 1]

# print(list(zip(my_strings, sorted(my_numbers))))

# scores = [73, 20, 65, 19, 76, 100, 88]

# def over_50(item):
#     	return item > 50

# print(list(filter(over_50, scores)))

# def sum_all(default, current):
#     	return default + current

# print(reduce(sum_all, scores + my_numbers, 0))

# Exercise: Lambda expressions

# my_list = [5, 4, 3, 2, 1]

# print(list(map(lambda item: item ** 2, my_list)))

# a = [(0, 2), (4, 3), (9, 9), (10, -1)]

# print(sorted(a, key=lambda item: item[-1]))

# some = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# duplicates = list(set([item for item in some if some.count(item) > 1]))
# print(duplicates)

# Exercise Decorators

user1 = {
	'name': 'Sorna',
	'valid': True
}

def authenticated(func):
	def wrapper(user, *args, **kwargs):
    		# valid = True
    		if user['valid'] == True:
    				return func(user, *args, **kwargs)
	return wrapper


@authenticated
def message_friends(user):
	print('message has been sent')

message_friends(user1)