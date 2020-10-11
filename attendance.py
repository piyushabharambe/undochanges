clas=int(input("Enter the number of classes held="))
att=int(input("Enter the number of classes you attended="))
perc=(att/clas)*100
print("The percentage of your class attended is="+str(perc)+"%")
if(perc>=75):
    print("You are allowed to sit for the exam")
else:
    print("You are not allowed to sit for the exam")