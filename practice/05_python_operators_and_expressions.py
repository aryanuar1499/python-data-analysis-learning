# ============================================================
# Project : Python for Data Analysis
# Phase   : 01 - Python Programming Fundamentals
# Lesson  : 01.1.5 - Python Operators and Expressions
# ============================================================


# ------------------------------------------------------------
# 01.1.5.4 - Comparison Operators
# ------------------------------------------------------------

# Step 17 - Runtime Validation: Greater Than or Equal To (>=)

minimum_score = 75

student_a = 80
student_b = 75
student_c = 74.5

print(student_a >= minimum_score) # True
print(student_b >= minimum_score) # True
print(student_c >= minimum_score) # False

print(student_b > minimum_score) # False
print(type(student_b >= minimum_score)) # <class 'bool'>

# 01.1.5.4-Q10 — Conceptual Evaluation

minimum_stock = 25

product_a = 30
product_b = 25
product_c = 15

print(product_a <= minimum_stock) # False
print(product_b <= minimum_stock) # True
print(product_c <= minimum_stock) # True

print(product_b < minimum_stock) # False

current_stock = 25
minimum_stock = 25

result = current_stock < minimum_stock

print(result) # False
print(type(result)) # <class 'bool'>
print(current_stock <= minimum_stock) # True
print(type(current_stock <= minimum_stock)) # <class 'bool'>

# Final Evaluation: Comparison Operators

a = 25
b = 25.0
c = "25"

print(a == b)
print(a == c)
print(b != c)
print(a >= b)
print(a <= b)
print(type(a) == type(b))

# Conceptual Re-evaluation

a = 100
b = 100.0
c = "100"

print(a == b)
print(a == c)
print(a == int(c))
print(type(a) == type(b))
print(type(a) == type(int(c)))
print(a is b)

# Value Equality, Object Identity, and Mutability

a = [10, 20, 30]
b = [10, 20, 30]
c = a

print(a == b)
print(a is b)
print(a == c)
print(a is c)

c.append(40)

print(a)
print(b)
print(c)

print(a == b)
print(a is c)

# Comparison Operators & Business Rules

current_stock = 20
minimum_stock = 20
maximum_stock = 100

# Replenishment Alert
print(current_stock <= minimum_stock)

# Overstock Alert
print(current_stock > maximum_stock)

# At Maximum Capacity
print(current_stock == maximum_stock)

# ------------------------------------------------------------
# Step 22 - Final Runtime Validation
# Boundary Testing - Inventory Business Rules
# ------------------------------------------------------------

# minimum_stock = 20
# maximum_stock = 100

# stock_values = [19, 20, 21, 99, 100, 101]

# for stock in stock_values:
#     print("Current Stock:", stock)
#     print("Replenisment Alert:", stock <= minimum_stock)
#     print("Overstock Alert:", stock > maximum_stock)
#     print("At Maximum Capacity:", stock == maximum_stock)

# Implementasi Nested Loop

minimum_stock = 20
maximum_stock = 100

stock_values = [19, 20, 21, 99, 100, 101]

for stock in stock_values:
    print("Current Stock:", stock)

    alerts = [
        ["Replenishment Alert", stock <= minimum_stock],
        ["Overstock Alert", stock > maximum_stock],
        ["At Maximum Capacity", stock == maximum_stock]
    ]

    for alert in alerts:
        print(alert[0] + ":", alert[1])

        print()
print(len(alerts))
print(alerts[2])
print(alerts[2][0])
print(alerts[2][1])

# Implementasi Nested Loop Alert
minimum_stock = 20
maximum_stock = 100

stock_values = [19, 20, 21, 99, 100, 101]

for stock in stock_values:
    print("Current Stock:", stock)

    alerts = [
        ["Replenishment Alert", stock <= minimum_stock],
        ["Overstock Alert", stock > maximum_stock],
        ["At Maximum Capacity", stock == maximum_stock]
    ]

    for alert in alerts:
        print("Alert:", alert)
        print("Length:", len(alert))
        print("Index 0:", alert[0])
        print("Index 1:", alert[1])
        print()