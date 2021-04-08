import random
import sys

print("ROCK, PAPER SCISSORS")

win = 0
loss = 0
tie = 0

while True:
    print(str(win) + " Wins, " + str(loss) + " Losses, " + str(tie) + " Ties")
    print("Enter  your move: (r)ock, (p)aper, (s)cissors, (q)uit")

    while True:
        move = input()
        move = move.lower()
        if move == "q":
            print("Thanks for playing!")
            sys.exit()
        elif move == "r":
            print("ROCK Versus...")
            break
        elif move == "p":
            print("PAPER Versus...")
            break
        elif move == "s":
            print("SCISSORS Versus")
            break
        else:
            print("Please enter a valid move.")
            continue

    cpuMove = random.randint(1, 3)
    if cpuMove == 1:
        cpuMove = "r"
        print("ROCK")
    elif cpuMove == 2:
        cpuMove = "p"
        print("PAPER")
    elif cpuMove == 3:
        cpuMove = "s"
        print("SCISSORS")

    if cpuMove == move:
        print("It's a Tie!")
        tie = tie + 1
    elif cpuMove == "r" and move == "p":
        print("You win!")
        win = win + 1
    elif cpuMove == "s" and move == "r":
        print("You win!")
        win = win + 1
    elif cpuMove == "p" and move == "s":
        print("You win!")
        win = win + 1
    elif cpuMove == "p" and move == "r":
        print("You lose!")
        loss = loss + 1
    elif cpuMove == "r" and move == "s":
        print("You lose!")
        loss = loss + 1
    elif cpuMove == "s" and move == "p":
        print("You lose!")
        loss = loss + 1
