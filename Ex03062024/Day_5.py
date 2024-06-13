for i in range (1,10,2):
    print(i)


year = int(input("Enter a year: "))
if year % 4 == 0:
 print(f"{year} is a leap year")
elif year % 100 == 0:
 print(f"{year} is not a leap year")
 print("It is divisible by 100")
elif year % 400 == 0:
    print (f"{year} is a leap year")
