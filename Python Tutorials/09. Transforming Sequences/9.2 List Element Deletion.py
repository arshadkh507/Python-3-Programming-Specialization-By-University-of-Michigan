
# ! del keyword is used to delete element from List
a = ['One', 'Two', 'Three']
del a[1]

print(a)

alist = ['a', 'b', 'c', 'd', 'e', 'f']
# del alist[1:5]

# ! We can delete the whole sequence
del alist
print(alist)  # NameError: name 'alist' is not defined.(b/c it's deleted)


# ===========================================
