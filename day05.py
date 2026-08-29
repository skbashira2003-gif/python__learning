# ==========================================================
# LIST - INSERT OPERATIONS
# ==========================================================

# Create a list with 3 elements
l = [1, 2, 3]
print(l)                              # Output: [1, 2, 3]


# ==========================================================
# APPENDING
# ==========================================================

# Add 5 types of non-sequence elements using append

l.append(10)
print(l)                              # Output: [1, 2, 3, 10]

l.append(10.5)
print(l)                              # Output: [1, 2, 3, 10, 10.5]

l.append(3 + 4j)
print(l)                              # Output: [1, 2, 3, 10, 10.5, (3+4j)]

l.append(True)
print(l)                              # Output: [1, 2, 3, 10, 10.5, (3+4j), True]

l.append(None)
print(l)                              # Output: [1, 2, 3, 10, 10.5, (3+4j), True, None]


# ==========================================================
# SEQUENCE ELEMENTS USING APPEND
# ==========================================================

l.append("python")
print(l)                              # Output: [..., 'python']

l.append([4, 5])
print(l)                              # Output: [..., [4, 5]]

l.append((6, 7))
print(l)                              # Output: [..., (6, 7)]

l.append({8, 9})
print(l)                              # Output: [..., {8, 9}]

l.append({10: 11})
print(l)                              # Output: [..., {10: 11}]


# ==========================================================
# EXTENDING
# ==========================================================

# Create a new list
l = [1, 2, 3]


# ==========================================================
# SEQUENCE ELEMENTS USING EXTEND
# ==========================================================

l.extend("abc")
print(l)                              # Output: [1, 2, 3, 'a', 'b', 'c']

l.extend([4, 5])
print(l)                              # Output: [1, 2, 3, 'a', 'b', 'c', 4, 5]

l.extend((6, 7))
print(l)                              # Output: [1, 2, 3, 'a', 'b', 'c', 4, 5, 6, 7]

l.extend({8, 9})
print(l)                              # Output: Order of 8 and 9 may vary

l.extend({10: 11})
print(l)                              # Output: 10 is added as dictionary key


# ==========================================================
# INSERTING
# ==========================================================

l = [1, 2, 3]

l.insert(1, 100)
print(l)                              # Output: [1, 100, 2, 3]

l.insert(-1, 200)
print(l)                              # Output: [1, 100, 2, 200, 3]

l.insert(10000, 300)
print(l)                              # Output: [1, 100, 2, 200, 3, 300]

l.insert(-10000, 400)
print(l)                              # Output: [400, 1, 100, 2, 200, 3, 300]


# ==========================================================
# DELETE OPERATIONS
# ==========================================================

l = [1, 2, 1, 3, 4, 1]

# Pop element at index 3
x = l.pop(3)
print(x)                              # Output: 3
print(l)                              # Output: [1, 2, 1, 4, 1]

# Pop last element
x = l.pop()
print(x)                              # Output: 1
print(l)                              # Output: [1, 2, 1, 4]

# Remove first 1
l.remove(1)
print(l)                              # Output: [2, 1, 4]

# Clear all elements
l.clear()
print(l)                              # Output: []


# ==========================================================
# UPDATE OPERATIONS
# ==========================================================

# Ascending order
l = [3, 2, 1, 5, 4]
l.sort()
print(l)                              # Output: [1, 2, 3, 4, 5]


# Descending order
l = [3, 2, 1, 5, 4]
l.sort(reverse=True)
print(l)                              # Output: [5, 4, 3, 2, 1]


# Reverse the list
l = [3, 2, 1, 5, 4]
l.reverse()
print(l)                              # Output: [4, 5, 1, 2, 3]


# ==========================================================
# READ OPERATIONS
# ==========================================================

l = [1, 2, 1, 3, 1, 2]

# Find count of 1 and 2
print(l.count(1))                     # Output: 3
print(l.count(2))                     # Output: 2

# Find index of 1 from start
print(l.index(1))                     # Output: 0

# Find index of 1 from 2nd index
print(l.index(1, 2))                  # Output: 2

# Find index of 1 from 5th index
# Removed because it causes ValueError.


# ==========================================================
# TUPLE
# ==========================================================

t = (1, 2, 1, 3, 1, 2)

# Find count of 1 and 2
print(t.count(1))                     # Output: 3
print(t.count(2))                     # Output: 2

# Find index of 1 from start
print(t.index(1))                     # Output: 0

# Find index of 1 from 2nd index
print(t.index(1, 2))                  # Output: 2

# Find index of 1 from 5th index
# Removed because it causes ValueError.