

cont="y"

while(cont=="y"):

 print("Welcome to tel's Address book")
 tel={}
 num=int(input("Enter the number of contacts you would like to enter in directory="))
 for i in range(0,num):
    name=input("Enter the name of the person:")
    phone=int(input("Enter the phone number"))
    tel[name]=phone

 choice=int(input("""Please select from the following menu depending upon the operations you would like to perform=
 1)Find Contact
 2)Add Contact
 3)Delete contact
 4)Quit address book"""))
 if(choice==1):
    name1=input("Enter the name of the person whoes contact you want to search:")
    for i in tel:
        if(i==name1):
            print ("The contact of person with name {} is {}".format(name1,tel[i]))
 
 if(choice==2):
    name2=input("Enter Name of the person whos contact you would like to add=")
    con=int(input("Enter Contact of that person="))
    tel[name2]=con
    print("Updated directory is= {}".format(tel))
 if(choice==3):
    name3=input("Enter Name of the person whos contact you would like to delete=")
    tel.pop(name3)
    print("Updated directory is= {}".format(tel))
 if(choice==4):
    exit
  
 cont=input("Would you like to execute it again y/n=")


