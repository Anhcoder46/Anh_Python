import random

player1 = input("Select Hammer, Bag or Scissor: ").lower()
player2 = random.choice(["Hammer", "Bag", "Scissor"]).lower()
print("Player 2 selected: ", player2)

if player1 == "hammer" and player2 == "bag":
    print("Player 2 win!")
elif player1 == "bag" and player2 == "scissor":
    print("Player 2 win!")
elif player1 == "scissor" and player2 == "hammer":
    print("Player 2 win!")
elif player1 == player2:
    print("Tie")
else:
    print("Player 1 win!")