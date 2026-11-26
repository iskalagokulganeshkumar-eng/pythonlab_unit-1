#prime or not for loop
number=int(input("Enter a number:"))
is_prime=True
if number<=1:
    is_prime=False
else:
    for count in range (2,number):
        if number %count==0:
            is_prime=False
            break
    if is_prime:
        print("print Number")
    else:
        print("Not a prime number")