'''
1 for snake 
-1 for water
0 for gun

'''
import random

def game_rule(player_choice,computer_choice):

    # rule for game
    
    if player_choice == computer_choice:
        return "It's a tie !"
    elif (player_choice == "snake" and computer_choice == "water") or \
         (player_choice == "gun" and computer_choice == "snake") or \
         (player_choice == "water" and computer_choice == "gun"):
        return "You win!"
    else:
        return("Computer win ! ")

def game():
     print("****Welcome to snake, water and gun game !!**** ")
     print("choice = [snake, gun , water]")
       
     choices = [ "snake","water","gun"]            
     player_choice = input("Enter your choice : ").lower()
     computer_choice = random.choice(choices)

     if player_choice not in choices:
      print("Invalid choice! Please try again.")
      return

     print(f"Your choice : {player_choice }")
     print(f"Computer choice : {computer_choice}")

     result = game_rule(player_choice,computer_choice)
     print(result)

game()