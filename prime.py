# prime or not
while(True):
 num=int(input("Enter the number which you want to check="))
 if(num>1):
    for i in range(2,num):
        if(num%i==0):
            print("{} is not a prime number!".format(num))
            break
    else:
            print("{} is a prime number!".format(num))
 else:
    print("{} is not a prime number!".format(num))