classroom = []
while True:
    print('Do you want the names sorted forwards(f) or backwards(b) alphebetically?')
    ans = input()
    if ans == 'f':
        direction = False
        break
    elif ans == 'b':
        direction = True
        break
    else:
        print('Please enter a valid command.')

while True:
    print('Enter your name (If every name has been entered type nothing):')
    name = input()
    if name == '':
        break
    else:
        classroom.append(name)
classroom.sort(key=str.lower, reverse=direction)
print(classroom)
