# HACKERRANK IF-ELSE PROBLEM

n = int(input())                         # Input: 3

if n % 2 != 0:
    print("Weird")                       # Output: Weird
elif 2 <= n <= 5:
    print("Not Weird")                   # Output: Not Weird
elif 6 <= n <= 20:
    print("Weird")                       # Output: Weird
else:
    print("Not Weird")                   # Output: Not Weird


# WRITE A FUNCTION – LEAP YEAR PROBLEM

year = int(input("Enter year: "))        # Input: 2000

if year % 400 == 0:
    print("Leap Year")                   # Output: Leap Year
elif year % 100 == 0:
    print("Not a Leap Year")             # Output: Not a Leap Year
elif year % 4 == 0:
    print("Leap Year")                   # Output: Leap Year
else:
    print("Not a Leap Year")             # Output: Not a Leap Year


# DAYS PROBLEM

n = int(input("Enter the day number: ")) # Input: 1

match n:
    case 1:
        print("Sunday")                  # Output: Sunday
    case 2:
        print("Monday")                  # Output: Monday
    case 3:
        print("Tuesday")                 # Output: Tuesday
    case 4:
        print("Wednesday")               # Output: Wednesday
    case 5:
        print("Thursday")                # Output: Thursday
    case 6:
        print("Friday")                  # Output: Friday
    case 7:
        print("Saturday")                # Output: Saturday
    case _:
        print("Invalid day number")       # Output: Invalid day number
        