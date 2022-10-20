import string

ls = [i * 10 for i in range(10)]
print(ls)
ls = [i * i for i in range(10)]
print(ls)

s = "qwertyuiop"
ls = [i * 3 for i in s]
print(ls)

s = "cvb"
STR = "qri"
ls = [0, 0]
print(ls)
print(all(ls))
print(any(ls))

# print(string.octdigits)
# print(string.digits)
# print(string.hexdigits)
# print(string.printable)
# print(string.whitespace)
# print(string.punctuation)
# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
