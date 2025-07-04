#!/usr/bin/env python3
# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(text):
    # returns first 5 characters from the string
    return text[:5]

def last_seven(text):
    # returns last 7 characters from the string
    return text[-7:]

def middle_number(number):
    # converts number to string and returns the 2nd and 3rd characters
    return str(number)[1:3]

def first_three_last_three(a, b):
    # first 3 characters from a + last 3 characters from b
    return a[:3] + b[-3:]

if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))
