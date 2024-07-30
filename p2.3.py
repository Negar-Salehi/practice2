Grades = int(input("Enter First Grade:"))
Number_Grade = 1
while True:
    new_record = input("Enter New Grade:")
    if new_record != "exit":
        Grades = Grades + int(new_record)
        Number_Grade = Number_Grade + 1
    else:
        print("is", str(Grades/Number_Grade))
    break  