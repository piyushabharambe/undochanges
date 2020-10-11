#total cost of shopping
print("Each quantity costs 1000rs!")
quantity=int(input("Enter the number of the quantity you want="))
total=quantity*1000
if(total>10000):
    print("Your total including 10% discount=",total-(0.1*total))
else:
    print("your total excluding discount",total)


    