# ============================================================
#🟠 LEVEL 1 — BEGINNER
# ============================================================


# ------------------------------------------------------------
# 1. ## 1. Even or Odd Checker
# Write a program that takes an integer input and determines whether it is even or odd.
# ------------------------------------------------------------

# Take a number from the user
num = int(input("Enter a number: "))

# If number is divisible by 2, it is even
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# ------------------------------------------------------------
# 2. Positive, Negative, or Zero   
# Take a number from the user and determine whether it is positive, negative, or zero.
# ------------------------------------------------------------

# Take a number from the user
num = int(input("Enter a number: "))

# Check whether the number is positive, negative, or zero
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# ------------------------------------------------------------
# 3. Multiplication Table
# Print the multiplication table of a given number from 1 to 10.
# ------------------------------------------------------------

# Take a number from the user
num = int(input("Enter a number: "))

# Loop from 1 to 10
for i in range(1, 11):
    # Print multiplication result
    print(num, "x", i, "=", num * i)


# ------------------------------------------------------------
# 4. Sum from 1 to N
# Take a number `N` and calculate the sum of all numbers from 1 to `N`.
# ------------------------------------------------------------

# Take N from the user
n = int(input("Enter N: "))

# Variable to store the total
total = 0

# Add every number from 1 to N
for i in range(1, n + 1):
    total = total + i

# Print the final sum
print("Sum =", total)


# ------------------------------------------------------------
# 5. Factorial Calculator
# Calculate the factorial of a given number.
# ------------------------------------------------------------

# Take a number from the user
num = int(input("Enter a number: "))

# Start factorial with 1
factorial = 1

# Multiply numbers from 1 to num
for i in range(1, num + 1):
    factorial = factorial * i

# Print factorial
print("Factorial =", factorial)


# ------------------------------------------------------------
# 6. Swap Two Numbers
# Swap two numbers without using a third variable.
# ------------------------------------------------------------

# Take two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Swap values using Python's built-in tuple unpacking
a, b = b, a

# Print swapped values
print("After swapping:")
print("a =", a)
print("b =", b)


# ------------------------------------------------------------
# 7. Reverse a String
# Take a string as input and print it in reverse order.
# ------------------------------------------------------------

# Take a string from the user
text = input("Enter a string: ")

# [::-1] reverses the string
reverse = text[::-1]

# Print reversed string
print("Reversed string:", reverse)


# ------------------------------------------------------------
# 8. Count Vowels
# Count the total number of vowels in a string.
# ------------------------------------------------------------

# Take a string from the user
text = input("Enter a string: ")

# Store all vowels
vowels = "aeiou"

# Counter starts from zero
count = 0

# Check every character
for char in text.lower():

    # If character is a vowel, increase counter
    if char in vowels:
        count += 1

# Print total vowels
print("Total vowels:", count)


# ------------------------------------------------------------
# 9. Largest Number in a List
# Find the largest number in a given list.
# ------------------------------------------------------------

# Example list
numbers = [10, 25, 5, 40, 15]

# Assume first number is the largest
largest = numbers[0]

# Check every number in the list
for num in numbers:

    # If current number is greater
    if num > largest:
        largest = num

# Print largest number
print("Largest number:", largest)


# ------------------------------------------------------------
# 10. Count Even Numbers
# Count how many even numbers exist in a list.
# ------------------------------------------------------------

# Example list
numbers = [10, 15, 20, 25, 30, 35, 40]

# Counter starts from zero
count = 0

# Check every number
for num in numbers:

    # Check if number is even
    if num % 2 == 0:
        count += 1

# Print total even numbers
print("Total even numbers:", count)


# ============================================================
# 🟠 Level 2 — INTERMEDIATE
# ============================================================


# ------------------------------------------------------------
# 11. Largest of Three Numbers
# Take three numbers and find the largest one.
# ------------------------------------------------------------

# Take three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# Compare all three numbers
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

# Print largest number
print("Largest number:", largest)


# ------------------------------------------------------------
# 12. Prime Number Checker
# Check whether a number is prime or not.
# ------------------------------------------------------------

# Take a number from the user
num = int(input("Enter a number: "))

# Assume number is prime
is_prime = True

# Numbers less than 2 are not prime
if num < 2:
    is_prime = False
else:

    # Check divisibility from 2 to num - 1
    for i in range(2, num):

        # If divisible, number is not prime
        if num % i == 0:
            is_prime = False
            break

# Print result
if is_prime:
    print("Prime number")
else:
    print("Not a prime number")


# ------------------------------------------------------------
# 13. Fibonacci Series
# Print the first `N` terms of the Fibonacci sequence.
# ------------------------------------------------------------

# Take number of terms
n = int(input("Enter number of terms: "))

# First two Fibonacci numbers
a = 0
b = 1

# Print N terms
for i in range(n):

    # Print current number
    print(a, end=" ")

    # Calculate next number
    a, b = b, a + b

print()


# ------------------------------------------------------------
# 14. Palindrome Checker
# Check whether a word or number is a palindrome.
# ------------------------------------------------------------

# Take text from the user
text = input("Enter a word: ")

# Reverse the text
reverse = text[::-1]

# Compare original and reversed text
if text == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")


# ------------------------------------------------------------
# 15. Remove Duplicates
# Remove duplicate values from a list.
# ------------------------------------------------------------

# Example list containing duplicate values
numbers = [10, 20, 10, 30, 20, 40, 30]

# Empty list for unique values
unique_numbers = []

# Check every number
for num in numbers:

    # Add number only if it is not already present
    if num not in unique_numbers:
        unique_numbers.append(num)

# Print list without duplicates
print("Original list:", numbers)
print("Without duplicates:", unique_numbers)


# ------------------------------------------------------------
# 16. Second Largest Number
# Find the second-largest number in a list.
# ------------------------------------------------------------

# Example list
numbers = [10, 25, 5, 40, 15, 30]

# Remove duplicate values first
unique_numbers = list(set(numbers))

# Sort numbers in ascending order
unique_numbers.sort()

# Second last value is the second largest
second_largest = unique_numbers[-2]

# Print result
print("Second largest number:", second_largest)


# ------------------------------------------------------------
# 17. Character Frequency Counter
# Count how many times each character appears in a string.
# ------------------------------------------------------------

# Take a string from the user
text = input("Enter a string: ")

# Empty dictionary to store character counts
frequency = {}

# Check every character
for char in text:

    # If character already exists, increase count
    if char in frequency:
        frequency[char] += 1

    # Otherwise, create the character with count 1
    else:
        frequency[char] = 1

# Print character frequencies
print("Character frequency:")

for char, count in frequency.items():
    print(char, "=", count)


# ------------------------------------------------------------
# 18. Number Guessing Game
# Generate a random number and allow the user to guess until correct.
# ------------------------------------------------------------

# Import random module
import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Keep asking until the user guesses correctly
while True:

    # Take user's guess
    guess = int(input("Guess a number (1-100): "))

    # Check if guess is too low
    if guess < secret_number:
        print("Too low!")

    # Check if guess is too high
    elif guess > secret_number:
        print("Too high!")

    # Guess is correct
    else:
        print("Correct! You guessed the number.")
        break


# ------------------------------------------------------------
# 19. Simple Calculator
# Create a calculator supporting `+`, `-`, `*`, and `/`.
# ------------------------------------------------------------

# Take two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Take operation from the user
operator = input("Enter operation (+, -, *, /): ")

# Perform addition
if operator == "+":
    result = num1 + num2

# Perform subtraction
elif operator == "-":
    result = num1 - num2

# Perform multiplication
elif operator == "*":
    result = num1 * num2

# Perform division
elif operator == "/":

    # Prevent division by zero
    if num2 == 0:
        print("Cannot divide by zero.")
        result = None
    else:
        result = num1 / num2

# Invalid operator
else:
    print("Invalid operator.")
    result = None

# Print result if calculation was successful
if result is not None:
    print("Result:", result)


# ------------------------------------------------------------
# 20. Password Strength Checker
# Check whether a password meets basic security requirements.
# ------------------------------------------------------------

# Take password from the user
password = input("Enter your password: ")

# Check password length
has_length = len(password) >= 8

# Check if password contains a digit
has_digit = False

# Check if password contains an uppercase letter
has_upper = False

# Check if password contains a lowercase letter
has_lower = False

# Check every character in password
for char in password:

    # Check for digit
    if char.isdigit():
        has_digit = True

    # Check for uppercase letter
    elif char.isupper():
        has_upper = True

    # Check for lowercase letter
    elif char.islower():
        has_lower = True


# Check all password requirements
if has_length and has_digit and has_upper and has_lower:
    print("Strong password")
else:
    print("Weak password")

    # Tell user what is missing
    if not has_length:
        print("- Password must contain at least 8 characters.")

    if not has_digit:
        print("- Password must contain at least one number.")

    if not has_upper:
        print("- Password must contain at least one uppercase letter.")

    if not has_lower:
        print("- Password must contain at least one lowercase letter.")


# ============================================================
# 🟠 Level 3 — Strong Logic
# ============================================================

# ------------------------------------------------------------
# 21. Find Missing Number
# Given numbers from 1 to N with one missing, find the missing number.
# ------------------------------------------------------------

# Example list
numbers = [1, 2, 3, 5]

# N means numbers should be from 1 to N
n = 5

# Check every number from 1 to N
for i in range(1, n + 1):

    # If number is not present in the list
    if i not in numbers:

        # This is the missing number
        print("Missing number:", i)


# ------------------------------------------------------------
# 22. Move Zeros to End
# Move all zeros in a list to the end while preserving order.
# ------------------------------------------------------------

# Example list
numbers = [0, 1, 0, 3, 12]

# Empty list to store the result
result = []

# First, add all non-zero numbers
for number in numbers:

    # Check if number is not zero
    if number != 0:

        # Add non-zero number to result
        result.append(number)


# Now add all zeros
for number in numbers:

    # Check if number is zero
    if number == 0:

        # Add zero to the end
        result.append(number)


# Print original and final list
print("Original list:", numbers)
print("After moving zeros:", result)


# ------------------------------------------------------------
# 23. Anagram Checker
# Check whether two strings are anagrams.
# ------------------------------------------------------------

# Take two words from the user
word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

# Convert both words to lowercase
word1 = word1.lower()
word2 = word2.lower()

# Sort both words
sorted_word1 = sorted(word1)
sorted_word2 = sorted(word2)

# Compare sorted words
if sorted_word1 == sorted_word2:
    print("Anagram")
else:
    print("Not an anagram")

# ------------------------------------------------------------
# 24. Longest Word Finder
# Find the longest word in a sentence.
# ------------------------------------------------------------

# Take a sentence from the user
sentence = input("Enter a sentence: ")

# Split sentence into separate words
words = sentence.split()

# Assume the first word is the longest
longest_word = words[0]

# Check every word
for word in words:

    # If current word is longer
    if len(word) > len(longest_word):

        # Make current word the longest word
        longest_word = word

# Print the longest word
print("Longest word:", longest_word)


# ------------------------------------------------------------
# 25. FizzBuzz
# Print:

# * Fizz for multiples of 3
# * Buzz for multiples of 5
# * FizzBuzz for multiples of both
# ------------------------------------------------------------

# Loop from 1 to 100
for i in range(1, 101):

    # Check multiples of both 3 and 5 first
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")

    # Check multiples of 3
    elif i % 3 == 0:
        print("Fizz")

    # Check multiples of 5
    elif i % 5 == 0:
        print("Buzz")

    # Print the number if it is not a multiple of 3 or 5
    else:
        print(i)


# ------------------------------------------------------------
# 26. Binary Search
# Implement binary search on a sorted list.
# ------------------------------------------------------------

# Binary search works on a sorted list
numbers = [10, 20, 30, 40, 50, 60, 70]

# Number we want to find
target = 50

# Starting position
left = 0

# Ending position
right = len(numbers) - 1

# Keep searching while left is not greater than right
while left <= right:

    # Find the middle position
    middle = (left + right) // 2

    # If middle value is the target
    if numbers[middle] == target:
        print("Number found at index:", middle)
        break

    # If target is greater than middle value
    elif target > numbers[middle]:

        # Search in the right half
        left = middle + 1

    # If target is smaller than middle value
    else:

        # Search in the left half
        right = middle - 1

else:
    # Target was not found
    print("Number not found")


# ------------------------------------------------------------
# 27. Merge Sorted Lists
# Merge two sorted lists into a single sorted list.
# ------------------------------------------------------------

# Two sorted lists
list1 = [1, 3, 5]
list2 = [2, 4, 6]

# Empty list to store merged values
result = []

# Start positions for both lists
i = 0
j = 0

# Compare values from both lists
while i < len(list1) and j < len(list2):

    # If value from list1 is smaller
    if list1[i] < list2[j]:

        # Add list1 value
        result.append(list1[i])

        # Move to next value in list1
        i += 1

    else:

        # Add list2 value
        result.append(list2[j])

        # Move to next value in list2
        j += 1


# Add remaining values from list1
while i < len(list1):
    result.append(list1[i])
    i += 1


# Add remaining values from list2
while j < len(list2):
    result.append(list2[j])
    j += 1


# Print merged list
print("Merged list:", result)


# ------------------------------------------------------------
# 28. Valid Parentheses
# Check whether parentheses/brackets are balanced.
# ------------------------------------------------------------

# Example brackets
text = "({[]})"

# Empty list will work as a stack
stack = []

# Store matching closing brackets
pairs = {
    ")": "(",
    "]": "[",
    "}": "{"
}

# Assume brackets are valid
is_valid = True

# Check every character
for char in text:

    # If opening bracket, add it to stack
    if char in "([{":
        stack.append(char)

    # If closing bracket
    elif char in ")]}":

        # Check if stack is empty
        if not stack:

            # No opening bracket to match
            is_valid = False
            break

        # Remove the last opening bracket
        last = stack.pop()

        # Check whether brackets match
        if last != pairs[char]:

            # Brackets do not match
            is_valid = False
            break


# If stack is not empty, some opening brackets are left
if stack:
    is_valid = False


# Print result
if is_valid:
    print("Valid parentheses")
else:
    print("Invalid parentheses")


# ------------------------------------------------------------
# 29. Frequency of Elements
# Count occurrences of each element in a list.
# ------------------------------------------------------------

# Example list
numbers = [10, 20, 10, 30, 20, 10, 40]

# Empty dictionary to store frequencies
frequency = {}

# Check every number
for number in numbers:

    # If number already exists
    if number in frequency:

        # Increase its count
        frequency[number] += 1

    # If number does not exist
    else:

        # Start its count from 1
        frequency[number] = 1


# Print frequency of every element
print("Frequency:")

for number, count in frequency.items():
    print(number, "=", count)


# ------------------------------------------------------------
# 30. Two Sum Problem
# Find two numbers whose sum equals a target value.
# ------------------------------------------------------------

# Example list
numbers = [2, 7, 11, 15]

# Target sum
target = 9

# Check every number
for i in range(len(numbers)):

    # Check numbers after the current number
    for j in range(i + 1, len(numbers)):

        # Check if two numbers add up to target
        if numbers[i] + numbers[j] == target:

            # Print the two numbers
            print("Numbers:", numbers[i], "and", numbers[j])

            # Print their indexes
            print("Indexes:", i, "and", j)