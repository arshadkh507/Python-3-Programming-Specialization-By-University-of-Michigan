# 10.8. Writing Text Files

# ! write()

# file_obj = open('squares.txt', "w")


# for number in range(13):
#     square = number * number
#     file_obj.write(str(square))
#     file_obj.write("\n")

# print("file is written.")
# file_obj.close()

# ! close() is important


new_file_obj = open("squares.txt", "r")
print(new_file_obj.read()[:10])
