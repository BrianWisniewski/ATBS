import random

streakCount = 0
testLength = 10000

def generateNums():
    for i in range(100):
        value = random.randint(0, 1)
        if value == 0:
            flip = 'H'
        elif value == 1:
            flip = 'T'
        flipList.append(flip)
def findStreaks():
    hcount = 0
    tcount = 0
    streaks = 0
    for i in flipList:
        if i == 'H':
            hcount += 1
            tcount = 0
        elif i == 'T':
            tcount += 1
            hcount = 0
        if hcount == 6 or tcount == 6:
            streaks += 1
            hcount = 0
            tcount = 0
    return streaks

for i in range(testLength):
    flipList = []
    generateNums()
    streakCount += findStreaks()
print('Chance of streak: ' + str(round((streakCount/testLength), 4)) + '%')
