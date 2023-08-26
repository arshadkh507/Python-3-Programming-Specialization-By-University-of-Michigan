
# 9.16. Chapter Assessment - List Methods
# =================================================
# Write code to add ‘horseback riding’ to the third position (i.e., right before volleyball) in the list sports.

"""
sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']

sports.insert(2, "horseback riding")
print(sports)

"""

# =================================================
# Write code to take ‘London’ out of the list trav_dest.

"""
trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'London', 'Melbourne']

trav_dest.remove('London')
print(trav_dest )
"""

# =================================================
# Write code to add ‘Guadalajara’ to the end of the list trav_dest using a list method.

"""

trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'Melbourne']

trav_dest.append('Guadalajara')

"""

# =================================================
# What will be the value of a after the following code has executed?

# a = ["holiday", "celebrate!"]
# quiet = a
# quiet.append("company")
# The value of a will be

"""
["holiday", "celebrate!", "company"]
"""

# =================================================
#

"""
Could aliasing cause potential confusion in this problem?

b = ['q', 'u', 'i']
z = b
b[1] = 'i'
z.remove('i')
print(z)
A. yes
B. no

✔️ Yes, b and z reference the same list and changes are made using both aliases.
"""

# =================================================
#

"""
Could aliasing cause potential confusion in this problem?

sent = "Holidays can be a fun time when you have good company!"
phrase = sent
phrase = phrase + " Holidays can also be fun on your own!"
A. yes
B. no

✔️ Since a string is immutable, aliasing won't be as confusing. Beware of using something like item = item + new_item with mutable objects though because it creates a new object. However, when we use += then that doesn't happen.
"""

# =================================================
#

"""
Which of these is a correct reference diagram following the execution of the following code?

x = ["dogs", "cats", "birds", "reptiles"]
y = x
x += ['fish', 'horses']
y = y + ['sheep']


Sure, let's break down the code and explain it step by step:

x = ["dogs", "cats", "birds", "reptiles"]: Here, you're creating a list named x with four initial items: "dogs", "cats", "birds", and "reptiles".

y = x: You're creating a new variable y and making it refer to the same list as x. Both x and y are pointing to the same list in memory.

x += ['fish', 'horses']: You're using the += operator to add two more items, "fish" and "horses", to the list referred to by x. This operation modifies the original list that x is pointing to.

y = y + ['sheep']: Here, you're using the + operator to concatenate the list referred to by y with another list containing just "sheep". This creates a new list in memory with the combined items and assigns it to the variable y.

In simple words, let's create a reference diagram to visualize how the variables x and y are pointing to the lists:

less
Copy code
Initial state:
x ---> ["dogs", "cats", "birds", "reptiles"]
y ---> ["dogs", "cats", "birds", "reptiles"]

After x += ['fish', 'horses']:
x ---> ["dogs", "cats", "birds", "reptiles", "fish", "horses"]
y ---> ["dogs", "cats", "birds", "reptiles", "fish", "horses"]

After y = y + ['sheep']:
x ---> ["dogs", "cats", "birds", "reptiles", "fish", "horses"]
y ---> ["dogs", "cats", "birds", "reptiles", "fish", "horses", "sheep"]
In summary, the key takeaway is that += modifies the original list in place, while the + operator creates a new list with combined elements. This leads to the difference in behavior between x += ['fish', 'horses'] and y = y + ['sheep'].

"""

# =================================================
# Below are a set of scores that students have received in the past semester. Write code to determine how many are 90 or above and assign that result to the value a_scores.

"""
scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"
a_scores = 0

for score in scores.split():
    if int(score) >= 90:
        a_scores = a_scores + 1
"""
# =================================================
# Write code that uses the string stored in org and creates an acronym which is assigned to the variable acro. Only the first letter of each word should be used, each letter in the acronym should be a capital letter, and there should be nothing to separate the letters of the acronym. Words that should not be included in the acronym are stored in the list stopwords. For example, if org was assigned the string “hello to world” then the resulting acronym should be “HW”.

"""
stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"
acro = ""


for word in sent.split():
    if word in stopwords:
        continue
    else:
        if (sent.split())[-1] == word:
            acro = acro + word[:2].upper()
        else: 
            acro = acro + word[:2].upper() + ". " 
        
print(acro)
"""

# =================================================
# Write code that uses the string stored in sent and creates an acronym which is assigned to the variable acro. The first two letters of each word should be used, each letter in the acronym should be a capital letter, and each element of the acronym should be separated by a “. ” (dot and space). Words that should not be included in the acronym are stored in the list stopwords. For example, if sent was assigned the string “height and ewok wonder” then the resulting acronym should be “HE. EW. WO”.

"""

stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"
acro = ""
length_sent = sent.split()
count  = 0

for word in sent.split():
    if word == "The" or word == "the" or word == "to" or word == "and" or word == "for":
        stopwords.append(word)
    else:
        if length_sent[-1] == word:
            acro = acro + word[:2].upper()
        else: 
            acro = acro + word[:2].upper() + ". " 
        
print(acro)
"""
# =================================================
# A palindrome is a phrase that, if reversed, would read the exact same. Write code that checks if p_phrase is a palindrome by reversing it and then checking if the reversed version is equal to the original. Assign the reversed version of p_phrase to the variable r_phrase so that we can check your work.

"""
p_phrase = "was it a car or a cat I saw"

r_phrase = ""

for char in p_phrase:
        r_phrase =  char + r_phrase 
    
if r_phrase == p_phrase:
   r_phrase = p_phrase

print(r_phrase)

"""
# =================================================
# Provided is a list of data about a store’s inventory where each item in the list represents the name of an item, how much is in stock, and how much it costs. Print out each item in the list with the same formatting, using the .format method (not string concatenation). For example, the first print statment should read The store has 12 shoes, each for 29.99 USD.

"""
inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]

for item in inventory:
    item_data = item.split(", ")
    name = item_data[0]
    stock = int(item_data[1])
    price = float(item_data[2])
    result_str = "The store has {1} {0}, each for {2:.2f} USD.".format(name , stock, price)
    print(result_str)

"""
# =================================================
#

"""

"""
# =================================================
#

"""

"""
# =================================================
#

"""

"""
# =================================================
#

"""

"""
# =================================================
#

"""

"""
