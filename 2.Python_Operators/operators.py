# Arithmetic Operators
# --------------------
x = 10
y = 4

# Addition
x + y               # Returns 14

# Subtraction
x - y               # Returns 6

# Multiplication
x * y               # Returns 40

# Division
x / y               # Returns  2.5

# Floor Division
x // y              # Returns 2.0

# Modulus
x % y               # Returns 2

# Exponentiation
x ** y              # Returns 10,000

# They can also be combined and their scope defined by brackets
(x * y) * (x / y) - (x % y)  # Returns 50

# Comparison Operators
# ---------------------
x = 5
y = z = 3

# Greater than
x > y           # Returns True         
y > z           # Returns False

# Less than
x < y           # Returns False
y < z           # Returns False

# Equal to 
x == y          # Returns False
y == z          # Returns True

# Not equal to
x != y          # Returns True          
y != z          # Returns False

# Greater than or equal to
x >= y          # Returns True
y >= z          # Returns True

# Less than or equal to
x <= y          # Returns False
y <= z          # Returns True

# Logical Operators
# -----------------

# Both sides true
(5 > 2) and (9 > 3) # Returns True
(5 > 2) or (9 > 3)  # Returns True
not (5 > 2)         # Returns False
not (9 > 3)         # Returns False

# Both sides false
(5 < 2) and (9 < 3) # Returns True
(5 < 2) or (9 < 3)  # Returns False
not (5 < 2)         # Returns True
not (9 < 3)         # Returns True

# True on one side and false on the other
(5 > 2) and (9 < 3) # Returns False
(5 > 2) or (9 < 3)  # Returns True
not (5 > 2)         # Returns False
not (9 < 3)         # Returns True

# Membership operators
# ---------------------
x = 3
y = 6
odd = [1, 3, 5, 7, 9, 11]
if x in odd:
    print(f'{x} is odd')
elif x not in odd:          # Returns '3 is odd' since it is in the list
    print(f'{x} is even')
elif y in odd:
    print(f'{y} is odd')
else:                       # Returns '6 is even' since it is not in the list
    print(f'{y} is even')
