catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames)+1) + ' (Or enter nothing to stop.):')
    ans = input()
    if ans == '':
        break
    catNames = catNames + [ans]
print('The cat names are:')
for i in catNames:
    print('   ' + i)
