#swap two numbers without using a third variable
a=int(input("Enter num1"))
b=int(input("Enter num2"))
a,b=b,a
print(f"swap of a is :{a}")
print(f"swap of b is :{b}")