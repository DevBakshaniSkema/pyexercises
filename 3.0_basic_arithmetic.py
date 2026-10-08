"""Exercise 3.0 — Computing with what the user typed

WHAT THE PROGRAM MUST DO
    Ask for two numbers and display the result of the four operations.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should your program do when the second number is zero? Decide, write your
       decision down, and only then implement it.

WHAT THE AI CANNOT KNOW
    Your answer to question 4. There are at least three defensible ones: refuse the
    value and ask again, display a message instead of a result, or stop the program.
    Pick one and be able to defend it.

CHECK IT YOURSELF
    Compute 7 divided by 2 in your head. Run your program with 7 and 2. If your program
    shows 3, it is not wrong by accident: find out why, and write the reason in a comment.
    Then run it with 0 as the second number.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# 2. Process:
# 3. Out:
# 4. What happens when the second number is zero, and why:


# Your code below
# 1. In: two numbers typed by the user
# 2. Process: the program turns both answers into numbers (float), then does +, -, *, /
# 3. Out: the result of the four operations
# 4. What happens when the second number is zero, and why:
#    The program shows a message instead of the division result. I chose this
#    because dividing by zero is impossible, and a message is clearer than a crash.
#    The other three operations still work.

# Your code below
# ask for the two numbers
number_1 = float(input("Enter the first number: "))
number_2 = float(input("Enter the second number: "))

# the three operations that always work
print(f"{number_1} + {number_2} = {number_1 + number_2}")
print(f"{number_1} - {number_2} = {number_1 - number_2}")
print(f"{number_1} * {number_2} = {number_1 * number_2}")

# division: check for zero first
if number_2 == 0:
    print("Division impossible: the second number is zero.")
else:
    print(f"{number_1} / {number_2} = {number_1 / number_2}")

# CHECK IT YOURSELF
# Test with 7 and 2: 
# Why it is not 3: 
# Test with 7 and 0:
20
