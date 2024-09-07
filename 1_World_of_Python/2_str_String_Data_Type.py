parrot = "Norwegian Blue"
#         01234567890123         14 chars in this string
#   -14,-13,-12,-11 ... ,-3,-2,-1
print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])
print("---------------------------------")
#! negative indexing in strings
print(parrot[-11])
print(parrot[-10])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])
#! Trick to divide pos n to max element. here it is 14
print("---------------------------------")
print(parrot[3 - 14])
print(parrot[4 - 14])
print(parrot[9 - 14])
print(parrot[3 - 14])
print(parrot[6 - 14])
print(parrot[8 - 14])
# ? the results are same # we win
