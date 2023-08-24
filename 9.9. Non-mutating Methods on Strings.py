# 9.9. Non-mutating Methods on Strings

ss = "Hello, World!"
# print(ss.upper())  # ! Does the mutate the string

tt = ss.lower()
# print(tt)
# print(ss)

# ==========================================

els = ss.count('l')
# print(els)


# ==========================================
print("***" + ss.strip() + "***")
print("***" + ss + "***")
# ==========================================n
news = ss.replace('o',  "***")
# print(news)


# ==========================================

name = "Arshad"
score = 1
print("Hello" + name + ". Your score is. " + str(score))

# ! format() is the better method then concatenation
print("Hello {}. Your score is {}.".format(name, score))

# ==========================================
