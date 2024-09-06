
# print("Hello I have been looking for you")
# print("Hello " + " World!")

# his_name = "Karim"
# his_country = "Uzbekistan"
# print(his_name + " " + his_country)
# name = input("Enter your name: ")
# print(f"Hello {name}")


#! Numeric Operators
a = 12
b = 2
print(a / b)  # it returns 6.0
print(a // b)  # it returns 6 integer division, rounded down towards minus infinity

# ? for example below code is correct
for i in range(1, 4):
    print(i)

# ? this code is incorrect because (a/b) returns n.n
# for i in range(1, a / b):
#     print(i)

# ? but this one is correct version
for i in range(1, a // b):
    print(i)
