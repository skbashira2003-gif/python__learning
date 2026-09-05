list = [4, 3, 2, 5, 6]

# 1. Print elements in list with for-each loop
for num in list:
    print(num)
# Output: 4 3 2 5 6


# 2. Print elements in list with index-based for loop
for i in range(len(list)):
    print(list[i])
# Output: 4 3 2 5 6


# 3. Skip printing even numbers in list
for num in list:
    if num % 2 == 0:
        continue
    print(num)
# Output: 3 5


# 4. Skip printing odd numbers in list
for num in list:
    if num % 2 != 0:
        continue
    print(num)
# Output: 4 2 6


# 5. When number 2 comes stop printing
for num in list:
    if num == 2:
        break
    print(num)
# Output: 4 3


# 6. When first odd number comes stop printing
for num in list:
    if num % 2 != 0:
        break
    print(num)
# Output: 4


# 7. Print numbers from 1 to 10
for num in range(1, 11):
    print(num)
print("All numbers printed")
# Output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# All numbers printed


# 8. Print numbers from 1 to 10, skipping even numbers
for num in range(1, 11):
    if num % 2 == 0:
        continue
    print(num)
print("All numbers printed")
# Output:
# 1
# 3
# 5
# 7
# 9
# All numbers printed


# 9. Print numbers from 10 to 1, when 5 comes stop printing
for num in range(10, 0, -1):
    if num == 5:
        break
    print(num)
print("All numbers printed")
# Output:
# 10
# 9
# 8
# 7
# 6
# All numbers printed