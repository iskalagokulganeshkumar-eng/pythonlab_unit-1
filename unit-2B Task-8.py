#sum of digits of number
number=int(input("Enter a number:"))
number=abs(number)
total_sum=0
while number > 0:
    digits=number%10
    total_sum=total_sum+digits
    number>number//10
print("sum of digits=",total_sum)