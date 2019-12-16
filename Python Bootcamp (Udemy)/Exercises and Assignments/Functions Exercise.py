# Problems are arranged in increasing difficulty:
#     Warmup - these can be solved using basic comparisons and methods
#     Level 1 - these may involve if/then conditional statements and simple methods
#     Level 2 - these may require iterating over sequences, usually with some kind of loop
#     Challenging - these will take some creativity to solve

## WARMUP SECTION:
#### LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers *if* both numbers are even, but returns the greater if one or both numbers are odd
#### lesser_of_two_evens(2,4) --> 2"
#### lesser_of_two_evens(2,5) --> 5"
def lesser_of_two_evens(a,b):
    if a and b %2 == 0:
        if a > b:
            return b
        elif b > a:
            return a
    elif a or b %2 != 0:
        if a > b:
            return a
        else:
            return b

# Check
lesser_of_two_evens(2,4)

# Check
lesser_of_two_evens(2,5)

# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
#### animal_crackers('Levelheaded Llama') --> True
#### animal_crackers('Crazy Kangaroo') --> False
def animal_crackers(text):
    letters = []
    for let in text.split():
        letters.append(let[0])
    return letters[0] == letters[1]

# Check
animal_crackers('Levelheaded Llama')

# Check
animal_crackers('Crazy Kangaroo')

# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
#### makes_twenty(20,10) --> True
#### makes_twenty(12,8) --> True
#### makes_twenty(2,3) --> False
def makes_twenty(n1,n2):
    return n1 == 20 or n2 == 20 or n1 + n2 == 20

# Check
makes_twenty(20,10)

# Check
makes_twenty(2,3)

# ------------------------------------------------------------ # 
# LEVEL 1 PROBLEMS
# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
#### old_macdonald('macdonald') --> MacDonald
#### Note: 'macdonald'.capitalize() returns 'Macdonald'
def old_macdonald(name):
    first_part = name[:3]
    second_part = name[3:]
    return first_part.capitalize() + second_part.capitalize()

# Check
old_macdonald('macdonald')

# MASTER YODA: Given a sentence, return a sentence with the words reversed
#### master_yoda('I am home') --> 'home am I'
#### master_yoda('We are ready') --> 'ready are We'

# Note: The .join() method may be useful here. The .join() method allows you to join together strings in a list with some connector string. For example, some uses of the .join() method:

#### >>> "--".join(['a','b','c'])
#### >>> 'a--b--c'

# This means if you had a list of words you wanted to turn back into a sentence, you could just join them with a single space string:

#### >>> " ".join(['Hello','world'])
#### >>> "Hello world"
def master_yoda(text):
    text = text.split()
    text.reverse()
    return " ".join(text)

# Check
master_yoda('I am home')

# Check
master_yoda('We are ready')

# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
#### almost_there(90) --> True
#### almost_there(104) --> True
#### almost_there(150) --> False
#### almost_there(209) --> True

# NOTE: abs(num) returns the absolute value of a number
def almost_there(n):
    return (abs(100-n) <= 10) or (abs(200-n) <= 10)
# Check
almost_there(104)

# Check
almost_there(150)

# Check
almost_there(209)
# ------------------------------------------------------------ # 

# LEVEL 2 PROBLEMS
# FIND 33:
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

#### has_33([1, 3, 3]) → True
#### has_33([1, 3, 1, 3]) → False
#### has_33([3, 1, 3]) → False
def has_33(nums):
    i = 1
    while i < len(nums):
        if nums[i] == nums[i - 1] and nums[i] == 3:
            return True
        i += 1
    return False

# Check
has_33([1, 3, 3])

# Check
has_33([1, 3, 1, 3])

# Check
has_33([3, 1, 3])

# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
#### paper_doll('Hello') --> 'HHHeeellllllooo'
#### paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'
def paper_doll(text):
    s = ""
    for letter in text:
        s += letter*3
    print(s)

# Check
paper_doll('Hello')

# Check
paper_doll('Mississippi')

# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
#### blackjack(5,6,7) --> 18
#### blackjack(9,9,9) --> 'BUST'
#### blackjack(9,9,11) --> 19
def blackjack(a,b,c):
    nums = [a,b,c]
    total = 0
    for num in nums:
        if num != 11:
            total += num
        elif num == 11:
            total += num - 10
    if total > 21:
        return 'BUST'
    return total

# Check
blackjack(5,6,7)

# Check
blackjack(9,9,9)

# Check
blackjack(9,9,11)

# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
#### summer_69([1, 3, 5]) --> 9
#### summer_69([4, 5, 6, 7, 8, 9]) --> 9
#### summer_69([2, 1, 6, 9, 11]) --> 14
def summer_69(arr):
    found_6 = False
    good_numbers = []
    for number in arr:
        if number == 6:
            found_6 = True
            continue
        elif number == 9 and found_6:
            found_6 = False
            continue
        elif found_6:
            continue
        good_numbers.append(number)
    return sum(good_numbers)

# ix = arr.index(num)
# badNums = badNums + arr[ix]

# Check
summer_69([1, 3, 5])

# Check
summer_69([4, 5, 6, 7, 8, 9])

# Check
summer_69([2, 1, 6, 9, 11])
# ------------------------------------------------------------ # 

# CHALLENGING PROBLEMS
#### SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
####  spy_game([1,2,4,0,0,7,5]) --> True
####  spy_game([1,0,2,4,0,5,7]) --> True
####  spy_game([1,7,2,0,4,5,0]) --> False
def spy_game(nums):
    i = 0
    while i < len(nums):
        if i + 1 == len(nums):
            break
        elif nums[i] == 0 and nums[i] == nums[i + 1] and nums[i + 2] == 7:
            return True
        i += 1
    return False


# Check
spy_game([1,2,4,0,0,7,5])

# Check
spy_game([1,0,2,4,0,5,7])

# Check
spy_game([1,7,2,0,4,5,0])

# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
#### count_primes(100) --> 25

# By convention, 0 and 1 are not prime.
def count_primes(num):
    prime_total = 0
    for prime_num in range(2, num + 1): 
        prime_counter = 0
        i = 1
        while i <= prime_num:
            if prime_num % i == 0:
                prime_counter += 1
                if prime_counter > 2:
                    break
                elif prime_counter == 2 and i == prime_num:
                    prime_total += 1
                i += 1
            else:
                i += 1
    return prime_total

# Check
count_primes(100)
# ------------------------------------------------------------ # 

# Just for fun:
#### PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter
#### print_big('a')

#### out:   *  
####       * *
####      *****
####      *   *
####      *   *
# HINT: Consider making a dictionary of possible patterns, and mapping the alphabet to specific 5-line combinations of patterns.
# For purposes of this exercise, it's ok if your dictionary stops at "E".
def print_big(letter):
    letter_dict = {"a":'* * * ***** *   * *   *'
                      }
    print(letter_dict)

print_big('a')