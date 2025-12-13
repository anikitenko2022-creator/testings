import keyword
from random import randint
text = "texts"
num = 10
num_float = 3.14
lst = [text, num, num_float, "Python", 50]
dct = {
    "text": text,
    "number": num,
    num_float: "float",
    1: lst
}
tpl = (num, text, "data")
st = {"element", text, num}
#2
print("Constant None:", None)
print(f"Constant False: {False}")
print("Constant NotImplemented:", NotImplemented)
print(keyword.kwlist)
#3
print(round(3.7), f"is equal to {round(3.2)}", "comparison:", round(3.7) == round(3.2))
print(len("Python"), f"is length of {'Python'}")
print(max(4, 9, 2), f"is greater than {min(4, 9, 2)}")
#4
numbers = [1, 3, 5, 7]

for n in numbers:
    print(f"Value: {n}")
i = 0
while i < 3:
    print(f"Counter: {i}")
    i += 1
else:
    print("Loop finished")
#5
x = randint(-5, 5)

if x > 0:
    print(f"Number {x} is positive")
elif x < 0:
    print(f"Number {x} is negative")
else:
    print("Number is zero")

y = randint(1, 10)
result = "Even number" if y % 2 == 0 else "Odd number"
print(result)
#6
B = "text"
try:
    print("Trying to add number and string:", 5 + B)
except Exception as e:
    print("Caught an error:", e)
finally:
    print("Finally block executed")
#7
with open("example.txt", "w") as file:
    file.write("Hello, Python!\n")
    file.write("This is a test file.\n")

with open("example.txt", "r") as file:
    for i, line in enumerate(file):
        print(f"{i}: {line.strip()}")
#8# 
multiply = lambda x, y: x * y
greet = lambda name: f"Hello, {name}!"

print("Lambda multiply:", multiply(5, 4))
print("Lambda greet:", greet("Alice"))
def values():
    return 3, 7

print("Using lambda with function return:", multiply(*values()))
