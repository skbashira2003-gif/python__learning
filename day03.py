
# ARITHMETIC OPERATORS


print(10 + 5 * 2)          # Output: 20

print(2 ** 3 ** 2)         # Output: 512

print(10 // 3)             # Output: 3

print(10 % 3)              # Output: 1

print(5 / 2)               # Output: 2.5

print([1,2,3] + [4,5,6])   # Output: [1, 2, 3, 4, 5, 6]

print((1,2,3) + (4,5,6))   # Output: (1, 2, 3, 4, 5, 6)

print({1,2,3} | {4,5,6})   # Output: {1, 2, 3, 4, 5, 6}

print([1,2,3] * 4)         # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]

print(*[1,2,43])           # Output: 1 2 43

print(list((1,2,3)) + [4,5,6])  # Output: [1, 2, 3, 4, 5, 6]

print([1,2,3] + list('dog'))      # Output: [1, 2, 3, 'd', 'o', 'g']



# RELATIONAL AND LOGICAL OPERATORS


print(10 > 5 and 20 < 30)  # Output: True

print(10 > 20 and 5 < 10)  # Output: False
# Reason: 10 is not greater than 20.

print(not 1 == 1)          # Output: False
# Reason: 1 == 1 is True, and not True becomes False.

print(1 < 2 < 3)           # Output: True

print(1 > 2 > 3)           # Output: False
# Reason: 1 is not greater than 2.

print('abc' > 'def')       # Output: False
# Reason: 'abc' comes before 'def' alphabetically.

print([1,2,3] < [1,3,4])   # Output: True


# ASSIGNMENT AND WALRUS OPERATOR

a = 10
print(a)                   # Output: 10

print(a := 10)             # Output: 10

if (n := 34) > 10:
    print(n)               # Output: 34



# IDENTITY AND EQUALITY OPERATORS


a = [1,2,3]
b = [1,2,3]

print(a == b)              # Output: True

print(a is b)              # Output: False
# Reason: Both lists have the same values but are different objects.


a = 'abc'
b = 'abc'

print(a == b)              # Output: True

print(a is b)              # Output: True
# Note: Do not use "is" to compare string values.


a = (1,2,3)
b = (1,2,3)

print(a == b)              # Output: True

print(a is b)              # Output: True
# Note: Do not depend on "is" for comparing tuple values.


# MEMBERSHIP OPERATOR


a = [1,2,3,4,5]

print(6 in a)               # Output: False
# Reason: 6 is not present in the list.

print(6 not in a)           # Output: True

print('abc' in 'abcde')     # Output: True
