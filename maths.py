import random

print("Welcome to the maths quiz")

user_name = input("Please input your name : ")

print("Welcome " + user_name + " to the quiz")
y = True
points = 0
while y == True:
    
    print("The first question is : ")

    number1 = random.randint(0,100)
    number2 = random.randint(0,100)
    question = number1 + number2
    x = True
    while x == True:
        print("What is " + str(number1) + " plus " + str(number2) + "?")
        answer = input("Please type your answer here : ")
        if int(answer) == question:
            print("Correct")
            points = points + 1
            x = False
        else:
            print("Incorrect, your test is over")
            x = Falsenumber1 = random.randint(0,100)
            y = False

print("You have completed the quiz")
print("Your score is " + str(points))
    


