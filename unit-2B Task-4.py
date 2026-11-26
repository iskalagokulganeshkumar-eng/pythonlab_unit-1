# largest number in series
total_count=int(input("Enter how many number:"))
largest_number=float(input("enter number 1:"))
for count in range (2,total_count+1):
    number=float(input("Enter number*:"))
if number > largest_number:
    largest_number=number
print("Largest number=",largest_number)