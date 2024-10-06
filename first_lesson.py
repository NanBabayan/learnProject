# from xml.sax import parse
#
# x = 5
# name = "test"
# z = str(x) + " " + name
# print(z)
#
# a = 5
# b = "10"
# c = a + int(b)
# print(c)
#
# print(type(x))
# print(type(name))
# print(z)
#
# d = f"My name is ... {x}"
# print(d)
# print(d[-12:0])
# print(d[0:8])
#
# print("___________")
# print(d[::-1])
#
# print(d.replace("M","N"))
# print(d.upper())
# print(d.strip())
# print(d.split("..."))
import string
import time
from ast import Bytes
from itertools import count
from math import factorial
from os import times
from random import random

# print("___________")


# age = int(input("Enter your age: "))
#
# if age < 10:
#     print("Tae a water")
# elif 10 < age < 18:
#     print("Take a juice")
# elif 19 < age < 30:
#     print("Take a Latte")
# else:
#     print("Take a tea")

# print("___________")
#
# # 1.
#
# x = str(input("Print your value: "))
# print("___________")
#
# print(x.upper())
# print("___________")
# print(x.lower())
# print("___________")
# print(x[::-1])
# print("___________")
# print(x.count("a"))

# print("___________")

# z = float(input("Type your score here: "))
# if 10 < z < 60:
#     print("F")
# elif 60 < z < 69:
#     print("D")
# elif 70 < z < 79:
#     print("C")
# elif 80 < z < 89:
#     print("B")
# elif 90 < z < 100:
#     print("A")
# else:
#     print("0 SCORE")


# print("1.___________")


# while True:
#     input_text = int(input("Enter your number: "))
#
#     if 1 <=input_text <= 100:
#         print("Greate you guess the number")
#         break
#     else:
#         print(int(input("Try again: ")))

# print("1.___________")

# total = 0
# for number in range(1, 101):
#     total +=number
#     print(f"The total sum of numbers 1-100 is {total}")
#
# print("1.___________")
#
# n = int(input("Your Fibonacci number: "))
#
# a = 0
# b = 1
# count = 0
#
# while count < n:
#     print(a, end = " ")
#     a = b
#     b = a + b
#     count += 1
# print("1.___________")
#
# import random
# import string
#
# length = int(input("Your desirable pass length: "))
# passwrd = ""
# characters = string.ascii_letters + string.punctuation
#
# while len(passwrd) < length:
#     passwrd += random.choice(characters)
#
# print("Your new password: ", passwrd)
#
#
# print("1.___________")

# num = int(input("Your number: "))
# factorial = 1
# i = 1
#
# while i <= num:
#     factorial *= i
#     i+=1
#
# print(f"factorial of {num} is equal to {factorial}")

# print("1.___________")

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# even_numbers = 0
# odd_numbers = 0
# i = 0
#
# while i < len(numbers):
#     if numbers[i] % 2 == 0:
#         even_numbers +=1
#     else:
#         odd_numbers +=1
#     i+=1
# print("Even numbers count:", even_numbers)
# print("Odd numbers count:", odd_numbers)

# print("1.___________")

# list = [1, 2, 3, 4, 5, 5, 1]
# for i in list:
#     if list.count(i) > 1:
#         print(i, end = " ")

# print("1.___________")
# Iterate through numbers from 2 to 100
# for num in range(2, 101):
#     is_prime = True  # Assume the number is prime
#
#     # Check for factors from 2 to num - 1
#     for i in range(2, num):
#         if num % i == 0:  # If num is divisible by i
#             is_prime = False  # Not a prime number
#             break  # Exit the inner loop
#
#     # If the number is prime, print it
#     if is_prime:
#         print(num)

# print("1.___________")

# myList = [1, 2, 3, 4, 5, 6]
# myList[0] = 15
# print(myList)
# myList.remove(2)
# print(myList)
# myList.insert(0, 1111)
# print(myList)


# furniture = ["table", "chair", "sofa", "armchair"]
# fruits = ("banana", "apple", "pineapple")
# furniture.extend(fruits)
# myList = furniture.copy()
# myList.remove("chair")
# print(myList)

# cars = {"bmw", "mercedes", "volvo"}
# cars.add("audi")
# print(cars)

# myDict = {
#    "child1": {
#        "name": "Nancy",
#        "year": 1990
#    },
#     "child2": {
#         "name": "John",
#         "year": 1995
#     },
#     "child3": {
#         "name": "Garry",
#         "year": {
#             "1": "kkk",
#             "2": {
#                 "3": "last"
# }
#         }
#
#     }
# }
# print(myDict["child3"]["year"]["2"]["3"])

# def greeting_by_list(list_of_names):
#     print(f"Ni {list_of_names[1]}")
#
# list_of_names = ["Nana", "Hayk", "Mari"]
# greeting_by_list(list_of_names)


# def user_input(input):
#     print(f"Here is an input {input}")
#
# user_input(str(input()))


# class Cars:
#
#     def __init__(self, model, year, color):
#         self.model = model
#         self.year = year
#         self.color = color
#
#     def details_of_obj(self):
#         print(f"My car is {self.model} of {self.year} year and the color is {self.color}")
#
# car_1 = Cars("Audi", 2024, "Red")
# car_1.details_of_obj()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://www.python.org/")
# about_section_element = driver.find_element(By.ID, "about" )
# about_section_element.click()
# time.sleep(2)
#
# menu_elems = driver.find_elements(By.XPATH, "//*[@role='menubar']/li")
# for elem in menu_elems:
#     element = elem.text
#     print(element)
#
# menu_elems = driver.find_element()
# menu_elems.click()

