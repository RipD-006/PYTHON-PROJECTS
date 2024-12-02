# PYTHON PROGRAMMING - [Snake Water Gun : Game] 
import random
computer = random.choice([-1 , 0 , 1])
yourChoice = input("Enter your Choice [SNAKE , WATER or GUN]: ")
yourChoiceDict = {"SNAKE" : 1 , "GUN" : 0 , "WATER" : -1}

# Dictionary created for reference during Output
refrenceDict ={1 : "SNAKE" , 0 : "GUN" , -1 : "WATER"}

choice = yourChoiceDict[yourChoice]

print(f"You Chose {refrenceDict[choice]}" )
print(f"Computer Chose {refrenceDict[computer]}" )

# Base Condition
if(computer == choice):
    print("Its a Draw!")

# If Else() ladder
else:
    if(computer == -1 and choice == 1):
        print("You Win!")
    elif(computer == -1 and choice == 0):
        print("You Lose!")
    elif(computer == 0 and choice == -1):
        print("You Win!")
    elif(computer == 1 and choice == -1):
        print("You Lose!")
    elif(computer == 0 and choice == -1):
        print("You Win!")
    elif(computer == -1 and choice == 0):
        print("You Lose!")
    else:
        print("Something Went Wrong!")