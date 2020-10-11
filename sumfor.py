num=int(input("Enter the number till you which you want to sum="))
if(num<0):
    print("Enter positive number!")
else:
    sum=0
    while(num>0):
        sum=sum+num
        num=num-1
    print("The sum of  numbers is {}".format(sum))