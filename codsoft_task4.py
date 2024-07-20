import random
c=0
f=0


a="y"
while a=="y":
    opts = ("rock","paper","scissors")
    user = 0
    computer = random.choice(opts)

    
    user=input("Enter your choice: (rock, paper or scissors): ")

    print("Your choice is:  ", user)
    print("The computer's choice is: ",computer)

    
  
    if user==computer:
        print("It is a tie!")
    elif user=="rock" and computer=="scissors":
        print("You win!")
        c=c+1
       
    elif user=="scissors" and computer=="paper":
        print("You win!")
        c=c+1
        
    elif user=="paper" and computer=="rock":
        print("You win!")
        c=c+1
       
    else:
        print("You lose!")
        f=f+1
    
    print("Your score is: ",c)
    print("Computer's score is: ",f)
        
    
    a=input("Do you want to continue? Enter y or n: ")
    if a=="n":
        print("Thanks for playing")




    
