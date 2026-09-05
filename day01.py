# TASK 1: Tokens & Statements

name = "Bashira"
age = 23
city = "Repalle"

print("Name:", name)   # Output: Name: Bashira
print("Age:", age)     # Output: Age: 23
print("City:", city)   # Output: City: Repalle


# TASK 2: Identifiers

student_name = "Bashira"   
student_age = 23
student_marks = 65          
print("Student Name:", student_name)    # Output: Student Name: Bashira
print("Student Age:", student_age)      # Output: Student Age: 23
print("Student Marks:", student_marks)  # Output: Student Marks: 65

# student-name = "Bashira"
# Error: Hyphen (-) is not allowed in Python identifiers.


# TASK 3: Single-Line Comments

# This variable stores the student's name.
name = "Bashira"

# This variable stores the student's age.



age = 23

print("Name:", name)   # Output: Name: Bashira
print("Age:", age)     # Output: Age: 23



# TASK 4: Multi-Line Comments

# This program prints three messages.
# It shows that I am learning Python.
# Python is easy to learn.

print("Welcome to Python")              # Output: Welcome to Python
print("I am learning programming")     # Output: I am learning programming
print("Python is easy to learn")       # Output: Python is easy to learn


# TASK 5: Variables

name = "Bashira"
age = 23
height = 5.4
is_student = True

print("Name:", name)            # Output: Name: Bashira
print("Age:", age)              # Output: Age: 23
print("Height:", height)        # Output: Height: 5.4
print("Is Student:", is_student) # Output: Is Student: True


# TASK 6: Multiple Assignment

name, age, city = "Bashira", 23, "Repalle"

print("Name:", name)   # Output: Name: Bashira
print("Age:", age)     # Output: Age: 23
print("City:", city)   # Output: City: Repalle


# TASK 7: Reassignment

age = 23
print(age)             # Output: 23

age = 24
print(age)             # Output: 24


# TASK 8: Swapping Variables

a = 10
b = 20

print("Before:", a, b)     # Output: Before: 10 20

a, b = b, a

print("After:", a, b)      # Output: After: 20 10


# TASK 9: Deleting Variables

name = "Bashira"


print(name)                # Output: Bashira

del name

# print(name)
# Output: Error: name 'name' is not defined
# Reason: The variable was deleted using del.


# TASK 10: Keywords

import keyword

print(keyword.kwlist)      # Output: List of Python keywords
print(len(keyword.kwlist)) # Output: 35