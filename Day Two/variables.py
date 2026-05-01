#Day 2: 30 Days of Python Programming
import math

#Exercise 1
first_name = "Daniella"
last_name = "Brookstone"
full_name = "Daniella Brookstone"
country = "USA"
city = "Fiction Town"
age = 26
year = 2021
is_married = True
is_true = False
is_light_on = False
new_first, new_last, new_age, married = "Amber", "Woods", 30, True

#Exercise 2
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(new_first))
print(type(new_last))
print(type(new_age))
print(type(married))

print(len(first_name))

print("First Name Length:" + str(len(first_name)))
print("Last Name Length:" + str(len(last_name)))

num_one = 5
num_two = 4

total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

radius = 30
area_of_circle = math.pi * radius ** 2
circum_of_circle = math.pi * radius * 2

new_radius = int(input("Enter new radius: "))
new_area = math.pi * new_radius ** 2

first = input("Enter first name: ")
last = input("Enter last name: ")
new_country = input("Enter new country: ")
how_old = input("Enter new city: ")