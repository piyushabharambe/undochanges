num=int(input("Enter the number till you which you want to sum="))
if(num<0):
    print("Enter positive number!")
else:
    sum=0
    for num in range(0,num+1,1):
        sum=sum+num
    print("The sum of first {} numbers is {}".format(num,sum))