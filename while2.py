choice=8

while(choice!=0):
 print(""" Options from 0-5 are:
1) Get up
2) Learn python
3) Learn R
4) Attend lectures
5) Go to sleep
0) Exit """)
 choice=int(input("Enter your choice="))
 while(choice!=0):
    
    if(choice==1):
        print("Its 7!! get up.")
    elif(choice==2):
        print("Python is fun.Learn it.")
    elif(choice==3):
        print("R is easy for mathematical calculations.Learn it.")
    elif(choice==4):
        print("Its time for lectures.Go and attend it.")
    elif(choice==5):
        print("You may be tired go to sleep.")
    else:
        print("Invalid option try again !!")
        break
    choice=int(input("Enter your choice="))
        