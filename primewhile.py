# prime or not with while loop
while(True):

 num=int(input("Enter the number which you want to check="))
 f=0
 i=2
 if(num>1):
    while i<=num/2:
        if(num%i==0):
            print("{} is not a prime number!".format(num))
            break
        i=i+1
    else:
            print("{} is a prime number!".format(num))
 else:
    print("{} is not a prime number!".format(num))