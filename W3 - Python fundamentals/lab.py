print("Exercise 1: Data type detective")
print("===============================")
age = 20
height = 1.2
name = "Olaf"
is_Student = True

print(f"{name} is {age} years old, {height}m tall: {is_Student}")
print(f"Types: {type(age)}, {type(height)}, {type(name)}, {type(is_Student)}")

print("Exercise 2: Type converter")
print("==========================")
name = input("What's your name?")
age_text = input("What's your age?")

age = int(age_text)
birth_year=2026-age
print(f"{name}, you were born around {birth_year}")
import sys
try:
    age = int(input("Your age: "))
    print(f"Birth year:{2026-age}")
    print(f"Memory: int size = {sys.getsizeof(age)} bytes")
except ValueError:
    print("Please enter a valid number!")
print("")
print("Exercise 3: Dynamic typing")

x=5
print(f"x = {x}, type = {type(x)}, length = {len(str(x))}")
x="hello"
print(f"x={x}, type={type(x)},length={len(x)}")
x=[1,2,3]
print(f"x= {x}, type = {type(x)}, length = {len(x)}")
x=3.14
print(f"x = {x}, type = {type(x)}")

import sys
print("\n===MEMORY COMPARISON===")
print(f"int(42): {sys.getsizeof(42)} bytes")
print(f"float(3.14): {sys.getsizeof(3.14)} bytes")
print(f"str('hello'): {sys.getsizeof('hello')} bytes")
print("\n Exercise 4: Mini Calculator ")

while True:
    num1 = float(input("First number"))
    op = input("Operator(+,-,*,/): ")
    num2 = float(input("Second number: "))

    if op=="+":
        result=num1+num2
    elif op=="-":
        result=num1-num2
    elif op=="*":
        result=num1*num2
    elif op=="/":
      if num2==0:
          print("Error: cannot divide by zero!")
          result=None
      else:
        result=num1/num2
    else:
        print("Error: invalid operator!")
        result=None

    if result is not None:
        print(f"{num1}{op}{num2} = {result}")

    if op =="/":
        int_result = int(num1) // int(num2)
        print(f"Integer division: {int(num1)}//{int(num2)} = {int_result}")
    again = input("Calculate again? (yes/no):")
    if again.lower() != "yes":
        break
print("Thanks for using calculator!")