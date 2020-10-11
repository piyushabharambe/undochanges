def program():                                    #function for recurssion purpose of program
 n=int(input("""Which operation would you like to perform? Enter the number according to the below menu  
 1) Addition
 2) Subtraction
 3)Multiplication
 4)Division
 5)Floor operation
 6)Mod --to find remainder
 7)Power to term= """))                            #menu for operations
 a=int(input("Enter the first number="))
 b=int(input("Enter the second number="))
 if n==1:
    c=a+b
    print("Sum is={0}".format(c))                #printing addition using replacement
 if n==2:
    d=a-b
    print("Difference is={0}".format(d))          #printing using replacement
 if n==3:
    e=a*b
    print("Product is={0}".format(e))            #printing using replacement
 if n==4:
    f=a/b
    print("Quotient is={0}".format(f))           #printing using replacement
 if n==5:
    g=a//b
    print("Rounded Quotient is={0}".format(g))   #printing using replacement
 if n==6:
    h=a%b
    print("Remainder is={0}".format(h))        #printing using replacement
 if n==7:
    i=a**b
    print("Answer is={0}".format(i))        #printing using replacement
program()
while input("Do You Want To Continue? [y/n]") == "y":   # if user want to do program again 
    program()






