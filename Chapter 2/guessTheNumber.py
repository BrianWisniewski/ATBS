import random

mostTries = 6
guessnum = 1
minn = 1
maxn = 20
targetn = random.randint(minn, maxn)


print("I'm thinking of an number between "+str(minn)+" and "+str(maxn)+".")

while guessnum < mostTries:
    print("Take a guess.")
    guess = int(input())

    if targetn > guess:
        print("Your guess is too low.")
        guessnum = guessnum + 1
    elif targetn < guess:
        print("Your guess is too high")
        guessnum = guessnum + 1
    else:
        break

if guess != targetn:
    print("Sorry! The correct number was " + str(targetn) + ".")
else:
    print("Good job! You guessed the correct number in "+str(guessnum)+" guesses!")
