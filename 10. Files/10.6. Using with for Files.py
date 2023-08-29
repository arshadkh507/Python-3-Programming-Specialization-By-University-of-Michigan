# 10.6. Using with for Files


# it is equavilant to md = open("squares.txt" , "r")
with open("squares.txt", 'r') as md:
    for line in md:
        print(line)

# ! with (with) close() happen automatically for us.
