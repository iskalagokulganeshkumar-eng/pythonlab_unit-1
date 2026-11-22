# calculate compound interest
principal=int(input("Enter the principal amount:"))
rate=int(input("Enter the rate of interest:"))
time=int(input("Enter the time period:"))
total=principal*(1+rate/100)**time
compound_interest=total-principal
print("compound interest:",compound_interest)
