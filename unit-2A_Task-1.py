a=int(input("Enter first angle"))
b=int(input("Enter second angle"))
c=int(input("Enter third angle"))
total_angle=a+b+c
if a>0 and b>0 and c>0 and total_angle==180:
    print("valid triangle")
else:
    print("Invalid triangle")
    
