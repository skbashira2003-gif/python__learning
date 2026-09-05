# WHILE LOOP

# 1. Basic while loop - reverse counting

n = 5

while n >= 0:
    print(n, end=' ')
    n -= 1

print("Outside")


# 2. Print numbers from 5 to 10

n = 5

while n <= 10:
    print(n, end=' ')
    n += 1

print("Outside")


# 3. while loop with continue

n = 5

while n <= 10:
    if n == 7:
        n += 1
        continue

    print(n, end=' ')
    n += 1

else:
    print("Loop Successful")


# 4. while loop with break

n = 5

while n >= 0:
    if n == 3:
        break

    print(n, end=' ')
    n -= 1

else:
    print("Loop Successful")

print()


# 5. Print 1 to 10 using while loop

n = 1

while n <= 10:
    print(n, end=' ')
    n += 1

print()


# 6. Print even numbers from 1 to 10

n = 2

while n <= 10:
    print(n, end=' ')
    n += 2

print()


# 7. Print numbers divisible by both 5 and 7
# from 1 to 500

n = 1

while n <= 500:
    if n % 5 == 0 and n % 7 == 0:
        print(n, end=' ')
    n += 1

print()


# 8. Count digits of a number

n = int(input("Enter the number to count digits: "))

temp = abs(n)
count = 0

if temp == 0:
    count = 1
else:
    while temp > 0:
        temp //= 10
        count += 1

print("Number of digits in the given number is:", count)


# 9. Reverse a number

n = int(input("Enter number to reverse: "))

temp = abs(n)
reverse = 0

while temp > 0:
    last_digit = temp % 10
    reverse = reverse * 10 + last_digit
    temp //= 10

if n < 0:
    reverse = -reverse

print("Reverse of the given number is:", reverse)


# 10. Check palindrome number

n = int(input("Enter a number to check palindrome: "))

original = n
temp = abs(n)
reverse = 0

while temp > 0:
    last_digit = temp % 10
    reverse = reverse * 10 + last_digit
    temp //= 10

if n < 0:
    reverse = -reverse

if reverse == original:
    print("Palindrome")
else:
    print("Not a Palindrome")


# 11. Check Armstrong number

n = int(input("Enter a number to check Armstrong number: "))

original = n
temp = abs(n)
total_digits = len(str(abs(n)))
total = 0

while temp > 0:
    last_digit = temp % 10
    total += last_digit ** total_digits
    temp //= 10

if original >= 0 and original == total:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")


# 12. Check palindrome string
# Without slicing and without built-in reverse function

s = input("Enter a string to check palindrome: ")

i = 0
j = len(s) - 1

while i <= j:
    if s[i] != s[j]:
        print("Not a Palindrome")
        break

    i += 1
    j -= 1

else:
    print("Palindrome")
