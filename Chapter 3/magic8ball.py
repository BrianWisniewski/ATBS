import random

def getAnswer(num):
    if num == 1:
        return "You like men"
    elif num == 2:
        return "you are trans but you still like men"
    elif num == 3:
        return "you're fucked (from behind)"
    elif num == 4:
        return "you are a casually gay man that occasionally acts straight"
    elif num == 5:
        return "you are a homophobic gay man"
    elif num == 6:
        return "you like your friend in a very gay way"
    elif num == 7:
        return "you think straight should be abolished"
    elif num == 8:
        return "you are straight with the exception of Colin Dineley"
    elif num == 9:
        return "you are THE BIGGEST GAY"

print("You're personality is...")

roll = random.randint(1, 9)
fourtune = getAnswer(roll)
print(fourtune)
