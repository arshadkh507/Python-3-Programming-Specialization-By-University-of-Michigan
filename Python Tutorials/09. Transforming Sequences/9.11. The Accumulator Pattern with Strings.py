
# What is printed by the following statements:
s = "ball"
r = ""
for item in s:
    r = item.upper() + r
print(r)


# ===================================================

# For each character in the string already saved in the variable str1, add each character to a list called chars.
str1 = "I love python"
# HINT: what's the accumulator? That should go here.
chars = []
for ch in str1:
    chars.append(ch)

print(chars)

# ===================================================
# Assign an empty string to the variable output. Using the range function, write code to make it so that the variable output has 35 a s inside it (like "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"). Hint: use the accumulation pattern!

output = ""
count = 0
for n in range(35):
    output = output + "a"
    count += 1

print(output)
print(count)

# ===================================================
# ===================================================
# ===================================================
