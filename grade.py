#grading of students according to their marks
while (True):
 marks=float(input("Enter your marks="))
 if(marks<25):
    print("Fail! Your grade =F")
 elif(marks>=25 and marks<45):
    print("Improvement needed! Your grade=E")
 elif(marks>=45 and marks<50):
    print("Average Performance! Your grade=D")
 elif(marks>=50 and marks<60):
    print("Good! Your grade=C")
 elif(marks>=60 and marks<80):
    print("Very Good Performance! Your grade=B")
 elif(marks>=80 and marks<=100):
    print("Excellent! Your grade=A")
 else:
    print("Enter valid marks")