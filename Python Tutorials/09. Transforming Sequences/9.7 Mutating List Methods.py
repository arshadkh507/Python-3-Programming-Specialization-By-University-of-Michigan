
# Mutating Methods


# ! append() =>  add item to the end of the list
mylist = []
mylist.append(5)
mylist.append(27)
mylist.append(3)
mylist.append(12)
# print(mylist)


# ! insert() => To insert a list item at a specified index, use the insert() method.

mylist.insert(1, 12)
# print(mylist)

# ! count() => go through all the values in list and count how many of them are equal to 12.

# print(mylist.count(12))


# ! index() => we pass a value and it will tell us the position where the value can be found (the first index position).

# print(mylist.index(3))
# print(mylist.count(5))


# ! reverse() => reverse the list order change the list not make a new copy of the list

mylist.reverse()
# print(mylist)


#! sort() => it sort the list  from smallest to biggest
mylist.sort()
# print(mylist)

# ! remove() => remove the item from the list
mylist.remove(5)  # Or => del mylist[1]
# print(mylist)

# ! pop() => remove the last item from the list
lastitem = mylist.pop()
# print(lastitem)
# print(mylist)


# ===================================
