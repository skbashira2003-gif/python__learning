# ==============================
# LIST SLICING
# ==============================

numbers = [10, 20, 30, 40, 50, 60]

print(numbers[1:4])
# Output: [20, 30, 40]

print(numbers[:3])
# Output: [10, 20, 30]

print(numbers[3:])
# Output: [40, 50, 60]

print(numbers[-2:])
# Output: [50, 60]

print(numbers[::2])
# Output: [10, 30, 50]

print(numbers[::-1])
# Output: [60, 50, 40, 30, 20, 10]


# ==============================
# STRING FORMATTING
# ==============================

name = "Bashira"
age = 30

# f-string approach (Recommended)
print(f"Hello, my name is {name} and I am {age} years old.")
# Output: Hello, my name is Bashira and I am 30 years old.


# .format() approach
print("Hello, my name is {} and I am {} years old.".format(name, age))
# Output: Hello, my name is Bashira and I am 30 years old.