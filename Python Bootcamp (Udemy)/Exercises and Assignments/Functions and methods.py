#!/usr/bin/env python
# coding: utf-8

# # Functions and Methods Homework 
# 
# Complete the following questions:
# **Write a function that computes the volume of a sphere given its radius.**

def vol(rad):
    from fractions import Fraction
    from math import pi

    volume = Fraction(4, 3) * pi * rad**3
    return volume
    

# **Write a function that checks whether a number is in a given range (Inclusive of high and low)**

def ran_check(num,low,high):
    return num in range(low, high)
        

# If you only wanted to return a boolean:

def ran_bool(num,low,high):
    return num in range(low, high)

ran_bool(3,1,10)

# **Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.**
# 
#    Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
#    Expected Output : 
#    No. of Upper case characters : 4
#    No. of Lower case Characters : 33
# 
# If you feel ambitious, explore the Collections module to solve this problem!

def up_low(s):
    import collections
    upper_count = 0
    lower_count = 0
    for key, value in dict(collections.Counter(s)).items():
        if str(key).isupper():
            upper_count = upper_count + value
        elif str(key).islower():
            lower_count = lower_count + value
    print(f'No. of Upper case characters: {upper_count}\n', f'No. of Lower case characters: {lower_count}')

# **Write a Python function that takes a list and returns a new list with unique elements of the first list.**
# 
#    Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
#    Unique List : [1, 2, 3, 4, 5]

def unique_list(l):
    new_list = []
    for num in set(l):
        new_list.append(num)
    return new_list

unique_list([1,1,1,1,2,2,3,3,3,3,4,5])

# **Write a Python function to multiply all the numbers in a list.**
# 
#    Sample List : [1, 2, 3, -4]
#    Expected Output : -24

def multiply(numbers):  
    total = 1
    for num in numbers:
        total *= num
    return total

multiply([1,2,3,-4])

# **Write a Python function that checks whether a passed string is palindrome or not.**
# 
# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.

def palindrome(s):
    return s == s[::-1]

palindrome('helleh')

# **Hard**:
# 
# Write a Python function to check whether a string is pangram or not.
# 
#    Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
#    For example : "The quick brown fox jumps over the lazy dog"
# 
# Hint: Look at the string module

import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    str_let = ''
    letters = sorted(list(set([let for let in str1.lower() if let in alphabet])))
    for let in letters:
        str_let += let
    return str_let == alphabet

    #print(str(letter_check))

ispangram("The quick brown fox jumps over the lazy dog")

# Great Job!