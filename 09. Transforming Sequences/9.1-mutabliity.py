

# Mutabtability

fruits = ["apple", "banana", "cherry"]
# print(fruits)

fruits[0] = "pear"
fruits[-1] = "orange"

# ! Lists are Mutatable means changable
# print(fruits)


#  ====================================

alist = ['a', 'b', 'c', 'd', 'e', 'f']
alist[1:3] = ['x', 'y']
# ! Lists are Mutatable means changable
# print(alist)

#  ====================================

greeting = "Hello, World!"
# ! String are not Mutable means cannot reassign
# greeting[0] = "J" # TypeError: 'str' object does not support item assignment

greeting = "J" + greeting[1:]
# print(greeting)

#  ====================================


#  ====================================
