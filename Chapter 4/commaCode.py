spam = []
runningStr = ''
for index, item in enumerate(spam):
    runningStr += str(item)
    if index != len(spam)-1:
        runningStr += ', '
print(runningStr)
