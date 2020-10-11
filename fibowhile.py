n=int(input("Enter the number of terms="))
n0=0
n1=1
count=0
if n<=0:
    print("Invalid number! please enter more than 0")
elif n==1:
    print("Fibonacci series till {} is={}".format(n,n0))
else:
    print("Fibonacci series=")
    while count < n:
        print(n0)
        nt=n0+n1
        n0=n1
        n1=nt
        count=count+1