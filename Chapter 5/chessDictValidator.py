
def kings(board): # makes sure each player has exactly one king
    valid = True
    wking = 0
    bking = 0

    for piece in board.values():
        if piece == 'wking':
            wking += 1
        elif piece == 'bking':
            bking += 1

    if wking > 1:
        print('White player has too many kings!')
        valid = False  
    elif wking < 1:
        print('White player does not have a king!')
        valid = False

    if bking > 1:
        print('Black player has too many kings!')
        valid = False
    elif bking < 1:
        print('Black player does not have a king!')
        valid = False   

    return valid


def numCheck(board): # makes each player has at most 16 pieces and at most 8 pawns
    valid = True
    bcount = 0
    wcount = 0
    bpawn = 0
    wpawn = 0

    for piece in board.values():
        color = piece[0]
        
        if color == 'w':
            wcount += 1
            if piece == 'wpawn':
                wpawn += 1
        elif color == 'b':
            bcount += 1
            if piece == 'bpawn':
                bpawn += 1
        else: print(f'Piece {piece} is not on a valid team')

    if bcount > 16:
        print(f'Black team has {bcount} pieces. Only 16 are allowed!')
        valid = False
    if wcount > 16:
        print(f'White team has {wcount} pieces. Only 16 are allowed!')
        valid = False
    if bpawn > 8:
        print(f'Black team has {bpawn} pieces. Only 8 are allowed!')
        valid = False
    if wpawn > 8:
        print(f'White team has {wpawn} pieces. Only 8 are allowed!')
        valid = False

    return valid

def validSpace(board): # makes sure all pieces are on valid spaces
    valid = True

    for space in board.keys():
        if len(space) != 2:
            print(f'The value {space} is not a valid space!')
            valid = False
        if space[0] not in '12345678':
            print(f'The value {space} is not a valid space! The first character is not within the required range!')
            valid = False
        if space[1] not in 'abcdefgh':
            print(f'The value {space} is not a valid space! The second character is not within the required range!')
            valid = False

    return valid


def isValidChessBoard(board):
    king = kings(board) # makes sure each player has exactly one king
    num = numCheck(board) # makes each player has at most 16 pieces and at most 8 pawns
    space = validSpace(board) # makes sure all pieces are on valid spaces

    if king and num and space == True:
        print('This chess board is valid')

    return True

if __name__ == '__main__':

    print('Enter the dictionary value for the chess board:')
    board = eval(input())
    isValidChessBoard(board)
    