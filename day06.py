# ==========================================================
# SET METHODS
# ==========================================================


# ==========================================================
# CREATE EMPTY DICT AND SET
# ==========================================================

# Create an empty dict and print its type
d = {}
print(type(d))                         # Output: <class 'dict'>


# Create an empty set and print its type
s = set()
print(type(s))                         # Output: <class 'set'>


# ==========================================================
# ADD METHOD
# ==========================================================

# Add 5 non-sequence elements using add()

s.add(10)
s.add(10.5)
s.add(3 + 4j)
s.add(True)
s.add(None)

print(s)                               # Output: Set containing 10, 10.5, (3+4j), True, None


# ==========================================================
# ADD SEQUENCE / IMMUTABLE ELEMENTS
# ==========================================================

# List and dictionary cannot be added because they are unhashable.
# String, tuple and frozenset can be added.

s.add("python")
s.add((1, 2, 3))
s.add(frozenset({4, 5}))
s.add("abc")
s.add((6, 7))

print(s)                               # Output: Set containing the added values


# ==========================================================
# UPDATE METHOD
# ==========================================================

# update() requires an iterable.
# Therefore, non-sequence values are placed inside a list.

s.update([10])
s.update([20.5])
s.update([3 + 5j])
s.update([False])
s.update([None])

print(s)                               # Output: Set containing the added values


# Add elements from different iterables

s.update("abc")
s.update([1, 2, 3])
s.update((4, 5, 6))
s.update({7, 8, 9})
s.update({10: 11, 12: 13})

print(s)                               # Output: Set containing all added elements


# ==========================================================
# REMOVE ELEMENTS
# ==========================================================

s = {1, 2, 3, 4, 5}

print(s)                               # Output: {1, 2, 3, 4, 5}


# Remove one element using pop()
x = s.pop()
print(x)                               # Output: One element from the set
print(s)                               # Output: Remaining elements

# Note:
# Set is unordered, so pop() removes an arbitrary element.


# Remove existing element
s.remove(3)
print(s)                               # Output: Remaining elements without 3


# Removed s.remove(100)
# Reason: remove() gives KeyError if element does not exist.


# Discard existing element
s.discard(2)
print(s)                               # Output: Remaining elements without 2


# Discard non-existing element
s.discard(100)
print(s)                               # Output: Same set
# Reason: discard() does not give an error if element is absent.


# Remove all elements
s.clear()
print(s)                               # Output: set()


# ==========================================================
# SET AND LIST OPERATIONS
# ==========================================================

s = {1, 2, 3, 4}
l = [3, 4, 5, 6]


# Union
print(s.union(l))                      # Output: {1, 2, 3, 4, 5, 6}


# Intersection
print(s.intersection(l))               # Output: {3, 4}


# Difference
print(s.difference(l))                 # Output: {1, 2}


# Symmetric Difference
print(s.symmetric_difference(l))       # Output: {1, 2, 5, 6}


# ==========================================================
# SET OPERATIONS WITH ANOTHER SET
# ==========================================================

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}


# Union
print(s1 | s2)                         # Output: {1, 2, 3, 4, 5, 6}


# Intersection
print(s1 & s2)                         # Output: {3, 4}


# Difference
print(s1 - s2)                         # Output: {1, 2}


# Symmetric Difference
print(s1 ^ s2)                         # Output: {1, 2, 5, 6}


# ==========================================================
# DICT METHODS
# ==========================================================

# Create an empty dictionary
d = {}
print(d)                               # Output: {}


# ==========================================================
# UPDATE DICTIONARY
# ==========================================================

# Update dictionary with another dictionary

d.update({1: 'a', 2: 'b'})
print(d)                               # Output: {1: 'a', 2: 'b'}


# Update dictionary with a list of key-value pairs

d.update([('name', 'Bashira'), ('age', 23)])
print(d)                               # Output:
                                      # {1: 'a', 2: 'b',
                                      #  'name': 'Bashira', 'age': 23}


# Update dictionary with a tuple of key-value pairs

d.update((('city', 'Repalle'), ('marks', 65)))
print(d)                               # Output: Dictionary with city and marks added


# Removed:
# d.update({'x', 'y'})
# Reason: Dictionary update requires key-value pairs.


# ==========================================================
# POP METHODS
# ==========================================================

d = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}


# Remove pair with key 4
print(d.pop(4))                        # Output: d
print(d)                               # Output: {1: 'a', 2: 'b', 3: 'c'}


# Removed:
# print(d.pop(100))
# Reason: KeyError because key 100 does not exist.


# Remove key 100, if not present return 'z'
print(d.pop(100, 'z'))                 # Output: z


# Remove the last key-value pair
d = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

print(d.popitem())                     # Output: (4, 'd')
print(d)                               # Output: {1: 'a', 2: 'b', 3: 'c'}


# Remove all elements
d.clear()
print(d)                               # Output: {}


# ==========================================================
# GET METHOD
# ==========================================================

d = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

print(d.get(4))                        # Output: d

print(d.get(100))                      # Output: None

print(d.get(100, 'z'))                 # Output: z


# ==========================================================
# SETDEFAULT METHOD
# ==========================================================

print(d.setdefault(4))                 # Output: d

print(d.setdefault(100))               # Output: None

print(d.setdefault(100, 'z'))          # Output: z

print(d)                               # Output:
                                       # {1: 'a', 2: 'b', 3: 'c', 4: 'd', 100: None, ...}


# ==========================================================
# KEYS, VALUES AND ITEMS
# ==========================================================

d = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}


# Get all keys
keys = d.keys()

print(keys)                            # Output: dict_keys([1, 2, 3, 4])
print(type(keys))                      # Output: <class 'dict_keys'>


# Get all values
values = d.values()

print(values)                          # Output: dict_values(['a', 'b', 'c', 'd'])
print(type(values))                    # Output: <class 'dict_values'>


# Get all items
items = d.items()

print(items)                           # Output:
                                       # dict_items([(1, 'a'), (2, 'b'),
                                       #             (3, 'c'), (4, 'd')])

print(type(items))                     # Output: <class 'dict_items'>