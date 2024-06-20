import random

def rpc(choice,comp_choice):
    
    if(choice==1 and comp_choice=='PAPER') or (choice==2 and comp_choice=='SCISSOR') or (choice==3 and comp_choice=='ROCK'):
        return "YOU WIN!!!"
    
    if(choice==3 and comp_choice=='PAPER') or (choice==1 and comp_choice=='SCISSOR') or (choice==2 and comp_choice=='ROCK'):
        return "COMPUTER WINS!"
    
    if(choice==2 and comp_choice=='PAPER') or (choice==3 and comp_choice=='SCISSOR') or (choice==1 and comp_choice=='ROCK'):
        return "IT'S A DRAW!"

        
choices=['ROCK','PAPER','SCISSOR']
print("ROCK PAPER SCISSORS GAME")
print("------------------------")
while True:
    print("=========================")
    print("1. ROCK")
    print("2. PAPER")
    print("3. SCISSOR")
    print("4. EXIT")
    print("----------------")
    choice=int(input("YOUR CHOICE?:"))
    print("----------------")
    
    if(choice==1 or choice==2 or choice==3):
        print("Your choice:",choices[choice-1])
        comp_choice=random.choice(choices)
        print("Computer's choice:",comp_choice)
        print("=========================")
        result=rpc(choice,comp_choice)
        print(result)
        
    elif(choice==4):
        print("Exiting Rock Paper Scissors Game.....")
        break
     
    else:
        print("Invalid input! Please try again.")