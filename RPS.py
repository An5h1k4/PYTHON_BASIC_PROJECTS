import random
def get_Choices():
    playerChoice = input("Rock/Paper/scissors: ").lower()
    options = ["rock", "paper", "scissors"]
    computerChoice = random.choice(options)
    choices = {"player":playerChoice, "computer": computerChoice}
    return choices

def check_Win(player, computer):
    print(f"You chose: {player}\nComputer chose: {computer}")
    if(player == computer):
        return "\nIt's a tie!"
    elif player == "rock":
        if(computer == "scissors"):
            return "\nYou Win, rock breaks scissors."
        else:
            return "\nYou lose, Paper wraps rock."
    elif player == "paper":
        if computer == "rock":
            return "\nYou Win, Paper wraps rock."
        else:
            return "\nYou lose, rock breaks scissors."
    elif player == "scissors":
        if computer == "paper":
            return "\nYou Win, scissors cut paper."
        else:
            return "\nYou lose, rock breaks scissors."
        
choices = get_Choices();
result = check_Win(choices["player"], choices["computer"])
print(result)

