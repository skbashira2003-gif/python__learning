# DATA TYPES


# 1. int
a = 10
print(type(a))                 # Output: <class 'int'>


# 2. float
b = 10.5
print(type(b))                 # Output: <class 'float'>


# 3. complex
c = 5 + 3j
print(type(c))                 # Output: <class 'complex'>


# 4. bool
d = True
print(type(d))                 # Output: <class 'bool'>


# 5. NoneType
e = None
print(type(e))                 # Output: <class 'NoneType'>


# 6. string
f = "Python"
print(type(f))                 # Output: <class 'str'>


# 7. range
g = range(5)
print(type(g))                 # Output: <class 'range'>


# 8. list
h = [1, 2, 3]
print(type(h))                 # Output: <class 'list'>


# 9. tuple
i = (1, 2, 3)
print(type(i))                 # Output: <class 'tuple'>



# 10. set
j = {1, 2, 3}
print(type(j))                 # Output: <class 'set'>


# 11. dict
k = {"name": "Bashira", "age": 23}
print(type(k))                 # Output: <class 'dict'>


# ==========================================
# TYPE CONVERSION
# ==========================================

# 1. int to float
a = 10
b = float(a)
print(b)                       # Output: 10.0


# 2. float to int
a = 10.5
b = int(a)
print(b)                       # Output: 10


# 3. int to str
a = 100
b = str(a)
print(b)                       # Output: 100


# 4. str to int
a = "50"
b = int(a)
print(b)                       # Output: 50


# 5. list to tuple
a = [1, 2, 3]
b = tuple(a)
print(b)                       # Output: (1, 2, 3)


# 6. tuple to list
a = (1, 2, 3)
b = list(a)
print(b)                       # Output: [1, 2, 3]


# 7. list to set
a = [1, 2, 2, 3]
b = set(a)
print(b)                       # Output: {1, 2, 3}


# 8. range to list
a = range(5)
b = list(a)
print(b)                       # Output: [0, 1, 2, 3, 4]