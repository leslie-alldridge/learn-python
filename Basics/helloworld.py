# basic print
print("Hello, World!")

# identation
x = 1
if x == 1:
    # indented four spaces
    print("x is 1.")

# int float and strings

mystring = "hello"
myfloat = 10.0
myint = 20

if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)

# lists (arrays)

numbers = [1, 2, 3]
strings = ["hello", "world"]
names = ["John", "Eric", "Jessica"]

second_name = names[1]

print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)
