inport random, time, copyc  
size = (60, 20)
wait = 1
nextCells = []
for x in range(size[0]):
    column = []
    for y in range(size[1]):
        if random.randint(0, 1) == 0:
            column.append('#')
        else:
            column.append(' ')
    nextcells.append(column)
while True:
    print('\n\n\n\n\n')
    currentCells = copy.deepcopy(nextCells)

    for y in range(size[0]):
        for x in range(size[1]):
            print(currentCells[x][y], end='')
        print()
    for x in range(size[0]):
        for y in range(size[1]):
            # Get neighboring coordinates:
            # `% WIDTH` ensures leftCoord is always between 0 and WIDTH - 1
            leftCoord  = (x - 1) % size[0]
            rightCoord = (x + 1) % size[0]
            aboveCoord = (y - 1) % size[1]
            belowCoord = (y + 1) % size[1]

            # Count number of living neighbors:
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1 # Top-left neighbor is alive.
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1 # Top neighbor is alive.
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1 # Top-right neighbor is alive.
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1 # Left neighbor is alive.
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1 # Right neighbor is alive.
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1 # Bottom-left neighbor is alive.
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1 # Bottom neighbor is alive.
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1 # Bottom-right neighbor is alive.

            # Set cell based on Conway's Game of Life rules:
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                # Living cells with 2 or 3 neighbors stay alive:
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                # Dead cells with 3 neighbors become alive:
                nextCells[x][y] = '#'
            else:
                # Everything else dies or stays dead:
                nextCells[x][y] = ' '
    time.sleep(wait) #adds a 1 sec. pause to reduce flickering.
