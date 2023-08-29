# 10.11. Writing data to a CSV File

# ! Multiples of 12
"""
multiple_of_12_file = open("multiple_of_12.txt", "w")
for n in range(1, 11):
    txt = "{},{} \n".format(n, n * 12)
    multiple_of_12_file.write(txt)
multiple_of_12_file.close()

file_read = open("multiple_of_12.txt", "r")
contents = file_read.read()
print("Multiples of 12")
print(contents)
file_read.close()
"""
# ===================================================

#  By runstone enviroment - The python txt book
"""
n = [0] * 12
for i in range(1, 13):
    n[i-1] = i * 12
outfile = open("Multiples of 12", "w")
for j in range(0, len(n)):
    outfile.write(str(j+1) + ',' + str(n[j]))
    # +1 to j since the array starts at 0 and we start counting at 1
    outfile.write('\n')
outfile.close()
"""

# ===================================================
# Here is a more complex example, where we a have a list of tuples, each representing one Olympian, a subset of the rows and columns from the file we have been reading from.

"""
olympians_lst = [("John Aalberg", 31, "Cross Country Skiing"),
                 ("Minna Maarit Aalto", 30, "Sailing"),
                 ("Win Valdemar Aaltonen", 54, "Art Competitions"),
                 ("Wakako Abe", 18, "Cycling")]


olympians_file = open("reduced_olympics.csv", "w")
olympians_file.write("Name,Age,Sport")
olympians_file.write('\n')
for item in olympians_lst:
    values = item
    olympians_file.write("{},{},{}".format(values[0], values[1], values[2]))
    olympians_file.write("\n")

olympians_file.close()


olympians_file2 = open("reduced_olympics.csv", "r")
olympians_contents = olympians_file2.readlines()
for row in olympians_contents:
    print(row)
olympians_file2.close()

# ! By Runstone enviroment
olympians = [("John Aalberg", 31, "Cross Country Skiing"),
             ("Minna Maarit Aalto", 30, "Sailing"),
             ("Win Valdemar Aaltonen", 54, "Art Competitions"),
             ("Wakako Abe", 18, "Cycling")]

outfile = open("reduced_olympics.csv", "w")
# output the header row
outfile.write('Name,Age,Sport')
outfile.write('\n')
# output each of the rows:
for olympian in olympians:
    row_string = '{},{},{}'.format(olympian[0], olympian[1], olympian[2])
    outfile.write(row_string)
    outfile.write('\n')
outfile.close()
"""
# ===================================================
# In simple words, if we have data with text that might contain commas and we want to distinguish between commas in the text and commas separating values, we can enclose each value in double quotes. This can be a bit complex because we need to handle having double quote characters inside the string itself. Python allows using single quotes or double quotes to define strings, so one type can be used to define the string while the other can be part of the string. If you need to quote all values,
# ! it's recommended to learn to use Python's csv module for easier handling of such cases.s

"""
olympians = [("John Aalberg", 31, "Cross Country Skiing, 15KM"),
             ("Minna Maarit Aalto", 30, "Sailing"),
             ("Win Valdemar Aaltonen", 54, "Art Competitions"),
             ("Wakako Abe", 18, "Cycling")]

outfile = open("reduced_olympics2.csv", "w")
# output the header row
outfile.write('"Name","Age","Sport"')
outfile.write('\n')
# output each of the rows:
for olympian in olympians:
    row_string = '"{}", "{}", "{}"'.format(olympian[0], olympian[1], olympian[2])
    outfile.write(row_string)
    outfile.write('\n')
outfile.close()

"""
