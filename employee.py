age=int(input("Enter your age="))
sex=input("Enter your gender=[m/f]")
mar=input("Are you married?[y/n]")
if(sex=='f'):
    print("You will work only in urban areas.")
elif(sex=='m' and age<40 and age>=20):
    print("You may work anywhere.")
elif(sex=='m' and age<60 and age>=40):
    print("You will work only in urban areas.")
else:
    print("Error try again with proper values!!")