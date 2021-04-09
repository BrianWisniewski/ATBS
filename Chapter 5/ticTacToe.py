
## Board setup
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

##printing Board Status:
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

##Taking Turns
turn = 'X'
Win = False
while Win == False:
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    if theBoard[move] == ' ':
        theBoard[move] = turn
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    else:
        print('Already taken, choose another square.')
    
    if theBoard['top-L'] == theBoard['top-M'] == theBoard['top-R'] != ' ' or theBoard['mid-L'] == theBoard['mid-M'] == theBoard['mid-R'] != ' ' or theBoard['low-L'] == theBoard['low-M'] == theBoard['low-R'] != ' ' or theBoard['top-L'] == theBoard['mid-M'] == theBoard['low-R'] != ' ' or theBoard['top-R'] == theBoard['mid-M'] == theBoard['low-L'] != ' ' or theBoard['top-L'] == theBoard['mid-L'] == theBoard['low-L'] != ' ' or theBoard['top-M'] == theBoard['mid-M'] == theBoard['low-M'] != ' ' or theBoard['top-R'] == theBoard['mid-R'] == theBoard['low-R'] != ' ' :
        printBoard(theBoard)
        print(turn + ' has won!')
        break
    if theBoard['top-L'] != ' ' and theBoard['top-M'] != ' ' and theBoard['top-R'] != ' ' and theBoard['mid-L'] != ' ' and theBoard['mid-M'] != ' ' and theBoard['mid-R'] != ' ' and theBoard['low-L'] != ' ' and theBoard['low-M'] != ' ' and theBoard['low-R'] != ' ':
        printBoard(theBoard)
        print('The game ended in a tie. Nobody won!')
        break
