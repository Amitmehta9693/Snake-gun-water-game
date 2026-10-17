import random

def game_win(user,computer):
    if user == computer:
        return None

    # snake Vs Water
    if user == "s" and computer == "w":
        return True
    if user == "w" and computer == "s":
        return False
    # water vs Gun
    if user == "w" and computer == "g":
        return True
    if user == "g" and computer == "w":
        return False
    # gun Vs Snack
    if user == "g" and computer == "s":
        return True
    if user == "s" and computer == "g":
        return False

rand_no = random.randint(1, 3)

print("computer turn: snake (s), water (w), gun (g)") 
if rand_no == 1:
    computer = "s"
elif rand_no == 2:
    computer = "w"
else:
    computer = "g"


user = input("your turn's : snake(s), water(w), gun(g) ").lower()
result = game_win(user, computer) # return true if you win, false for you loss, none for draw
print(f"\you choose: {user}")
print(f"\nComputer choose: {computer}")

if result is None:
    print("Its a draw!")
elif(result):
    print("you win!")
else:
    print("you lose!")