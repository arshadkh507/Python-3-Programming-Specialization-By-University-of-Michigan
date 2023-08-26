
# ! Aliasing
a = [81, 82, 83]
b = [81, 82, 83]
print(a is b)  # False

b = a
print(a == b)  # True
print(a is b)  # True

b[0] = 5
print(a)  # [5, 82, 83]

# alising and mutable object can create some confusions
# Check we have not reassing the a varible but it's value the list is changed

# b/c a and b b/c of line 5 pointing to same object.


# ==============================
