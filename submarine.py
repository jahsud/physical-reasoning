import numpy as np
import random as r

# Create a 6x6 grid. Identify the grid squares similar to Battleship with letters for the rows and number for the columns
grid = np.full((6,6), '?', dtype = 'U1')
rows = "A", "B", "C", "D", "E", "F"

# Have the computer randomly assign the "submarine" location to one location on the grid
r1 = r.randint(0,grid.shape[0]-1)
r2 = r.randint(0,grid.shape[0]-1)
ranloc = rows[r1] + str(r2)

# Prompt the user to choose a location for the submarine (e.g., B3)
newGrid = np.copy(grid)
print(newGrid, '\n')
guess = input("Choose a location for the submarine: \n")

# Tell the user if their guess is correct and how much information was gained with that guess and how much total information they have gained so far (summed over all guesses)
while (guess != ranloc):
    newGrid[rows.index(guess[0]),int(guess[1])] = "X"
    print(newGrid, "\n")
    chances = np.count_nonzero(newGrid == '?')
    h = np.log2((chances + 1) / chances)
    guess = input("Your guess %s is NOT correct! \nH = %.2f \nChoose a new location: " % (guess, h))
newGrid[r1,r2] = "S"
print("Your guess %s is correct! \nH = %.2f" % (guess, h))

