# largest of three number using nested if 
a=int(input("Enter first number"))
b=int(input("Enter second number"))
c=int(input("Enter third number"))
if a>=b:
    if a>=c:
        largest_number=a
    else:
        largest_number=c
else:
    if b>=c:
        largest_number=b
    else:
        largest_number=c
    print("Largest Number=",largest_number)