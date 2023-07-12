import random
computer_number = random.randint(0 ,50)
number_count = 0
while True:
    user_number = int(input("Please Enter A Number:"))
    number_count +=1
    if computer_number == user_number:
        print ("Cograts You Win")
        print ("The Number of Your Guesses Are:" + str(number_count))
        break
    elif computer_number > user_number:
        print("Up")
    elif computer_number < user_number:
        print("Down")
