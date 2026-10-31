"""1] Even or Odd Function
Write a function is_even(n) that returns "Even" if the number is even, otherwise "Odd"."""

def check():
    print("EVEN or ODD")
    n = float(input("enter no: "))
    if n  %2==0:
        print(n,"is Even no.")
    else:
        print(n," is odd no.")
check()

    
"""2] Largest of Two Numbers
Write a function largest(a, b) that returns the larger number.
"""
def large(a,b):
    print("largest unmber finding")
    a = float(input("enter no. a: "))
    b = float(input("enter no. b: "))
    if a>b:
        print(a, "is grater then",b)
    elif a<b:
        print(b,"is grater then",a)
    else:
        print("Enter valid number")
large(1.2,2.2)

"""3] Print Numbers
Write a function print_numbers(n) that prints numbers from 1 to n using a loop.
"""

def num(n):
    n =int(input("enter no.: "))
    
    for i in range(1,n+1):
        print(i)
num(3)

"""3] Sum of Numbers
Write a function sum_n(n) that returns the sum of numbers from 1 to n.
"""
def sum_n():
    s=0
    n= int(input("enter no: "))

    for i in range(1,n+1):
        s=s+i
        
    return s    
print(sum_n())

"""4] Multiplication Table
Write a function table(n) that prints the multiplication table of n from 1 to 10.
"""


def table():
    n= int(input("enter no: "))
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")
table()

"""5] Count Even Numbers
Write a function that takes a list and returns how many even numbers it contains.
"""
def count_even():
    count = 0
    numbers = [int(x) for x in input("enter numbers separated by commas: ").split(",")]

    for num in numbers:
        if num % 2 == 0:
            count += 1

    print("Count of even numbers:", count)

print(count_even())

"""6] Find Maximum
Without using max(), write a function that returns the largest number in a list.
"""
def find_maximum(numbers):
    if not numbers:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num


print(find_maximum([3, 5, 2, 8, 1]))  

"""11] FizzBuzz
Write a function that prints numbers from 1 to 100.
If divisible by 3, print "Fizz".
If divisible by 5, print "Buzz".
If divisible by both, print "FizzBuzz".
"""
def fizz_buzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizz_buzz()

"""12] Palindrome Checker
Write a function that returns True if a string is a palindrome.
"""
def is_palindrome(text):
    return text == text[::-1]


print(is_palindrome("madam"))
print(is_palindrome("hello"))

"""13] Count Vowels
Write a function that counts the vowels in a string.
"""
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

print(count_vowels("He zzi xo"))

"""14] Second Largest Number
Write a function that returns the second largest number in a list without using sort().
"""
def second_largest(numbers):
    largest = float('-inf')
    second = float('-inf')

    for num in numbers:
        if num > largest:
            second = largest
            largest = num
        elif largest > num > second:
            second = num

    if second == float('-inf'):
        return None

    return second


print(second_largest([10, 2.0, 5, 8, 15]))


"""16]      Write a function grade(marks) that:
Returns "A" for marks ≥ 90
Returns "B" for marks ≥ 80
Returns "C" for marks ≥ 70
Returns "D" for marks ≥ 60
Otherwise returns "F"
"""
import random

def guessing_game():
    number = random.randint(1, 10)

    while True:
        guess = int(input("Guess a number between 1 and 10: "))

        if guess == number:
            print("Correct! You guessed it.")
            break
        elif guess < number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

guessing_game()

def grade(marks):
    # marks= int(input("Enter yuor marks: "))

    if marks >90 and marks <100:
        print("Grades A")
    elif marks>80 and marks<90:
        print("Grades B")
    elif marks>70 and marks<80:
        print("Grades C")
    elif marks>60 and marks<70:
        print("Grades D")
    elif marks<60:
        print("Grade F \n result is fail....")
    return marks


print(grade(85))