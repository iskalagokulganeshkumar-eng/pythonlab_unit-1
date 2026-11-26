# smallest of three number using nested if 
a=int(input("Enter first number"))
b=int(input("Enter second number"))
c=int(input("Enter third number"))
if a<=b:
   if a<b:
    smallest_number=a
   else:
    smallest_number=c
else:
  if b<=c:
    smallest_number=b
  else:
    smallest_number=c
print("smallest number=", smallest_number)