import calendar                   #importing calendar module
def program():
    year=int(input("Enter the year="))
    month=a=int(input("Enter the month="))
    print(calendar.month(year,month))         #passing year and month to function
program()
while input("Do You Want To Continue? [y/n]") == "y":  #if user want to continue the program
    program()
