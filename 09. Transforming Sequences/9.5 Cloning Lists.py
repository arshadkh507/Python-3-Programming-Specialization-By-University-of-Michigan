
# Cloning Lists

a = [81, 82, 83]
b = a[:]  # make a clone using slice operator

print(a == b)  # True

# ! (is Operator) does a is the same object as b or not
print(a is b)  # False

b[0] = 5
print(a)  # [81, 82, 83]
print(b)  # [5, 82, 83]

# with slicing when we clone a list it make new list for it.


# =============================
