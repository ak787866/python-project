import random

lst1 = ["s", "w", "g"]
computer_points = 0
human_points = 0
chance = 10
no_of_chance =0

print("snake water gun game")
print("for snake S\n for water W\n for gun G")

while no_of_chance < chance:
    _input = input("Snake, Water, Gun : ")
    _random = random.choice(lst1)

    if _input == _random:
        print("tie both 0 point to each \n")

    if _input == "s" and _random == "g":
        computer_points += 1
        print(f"your guess {_input} and computer guess is {_random}")
        print("computer wins 1 point \n")
        print(f"computer points is {computer_points} and your point is {human_points}\n")
    elif _input == "g" and _random == "s":
        human_points += 1
        print(f"your guess {_input} and the computer guess id {_random}")
        print("human wins 1 point \n")
        print(f"computer point is {computer_points} and your points is {human_points}")
    elif _input == "w" and _random == "s":
        computer_points += 1
        print(f"your guess {_input} and computer guess is {_random}")
        print("computer wins 1 point \n")
        print(f"computer points is {computer_points} and your point is {human_points}\n")
    elif _input == "s" and _random == "w":
        human_points += 1
        print(f"your guess {_input} and the computer guess id {_random}")
        print("human wins 1 point \n")
        print(f"computer point is {computer_points} and your points is {human_points}")
    elif _input == "w" and _random == "g":
        computer_points += 1
        print(f"your guess {_input} and computer guess is {_random}")
        print("computer wins 1 point \n")
        print(f"computer points is {computer_points} and your point is {human_points}\n")
    elif _input == "g" and _random == "w":
        human_points += 1
        print(f"your guess {_input} and the computer guess id {_random}")
        print("human wins 1 point \n")
        print(f"computer point is {computer_points} and your points is {human_points}")
    else:
        print("you have input wrong \n")

        no_of_chance = no_of_chance + 1
        print(f"{chance - no_of_chance} is left out of {chance} \n")

    print("Game over")

if computer_points > human_points:
    print("Computer wins and you loose")

if computer_points < human_points:
    print("you win and computer loose")

print(f"your point is {human_points} and computer point is {computer_points}")



