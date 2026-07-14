import random

def rps_game():

    print ("Let's play rock, paper, scissors!")
    
    rounds = input("How many rounds do you want to play? (3,5 or 7): ")
    round_number = 0
    user_wins = 0
    computer_wins = 0
    
    #win cases
    wins = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }
    
    #asks nr of rounds and checks if valid
    while True:
        try:
            rounds = int(rounds)
            if rounds in [3,5,7]:
                break
            else:
                rounds = input('Type either "3" or "5" or "7": ')
        except ValueError:
            rounds = input('Type either "3" or "5" or "7": ')
        
    while round_number < rounds:
        #asks user's choice and checks if valid       
        user_choice = input("Type your choice (rock, paper or scissors): ")
        
        while user_choice not in ["rock","paper","scissors"]:
            user_choice = input('Please only type "rock" or "paper" or "scissors": ')
         
        #the computer makes a choice and displays his and the user's choices        
        computer_choice = random.choice(["rock","paper","scissors"])
        print(f"Your choice: {user_choice}")
        print(f"My choice: {computer_choice}")
        round_number += 1
        
        #computer analyses who won
        if user_choice == computer_choice:
            pass
        elif wins[user_choice] == computer_choice:
            user_wins += 1  
        else:
            computer_wins += 1
            
    #tells each nr of wins
    print (f"Your wins: {user_wins}")
    print (f"My wins: {computer_wins}")
    
    #announces the winner
    if user_wins > computer_wins:
        print ("You won! Lucky...")
    elif computer_wins > user_wins:
        print ("I won! Not that I had any doubts :)")
    else:
        print ("It's a tie!")

while True:        
    rps_game()
    replay = input("Do you want to play again? (yes/no): ")
    while replay not in ["yes","no"]:
        replay = input('Type either "yes" or "no": ')
    if replay == "no":
        break
        
