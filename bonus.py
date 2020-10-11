years=int(input("Enter the years of service="))
sal=float(input("Enter your salary="))
if(years>5):
    print("You are applicable for bonus=")
    print("Bonus is {0}".format(5*sal/100))
else:
    print("You are not applicable as your service is less than 5 years.")
