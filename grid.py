from enum import Enum
from queue import Queue
import queue
import numpy as np
from requests import head

class Grid:
    EMPTY = 0
    HEAD = 1
    APPLE = 2
    BODY = 3
    WALL = 4


    def __init__(self, nbRows: int, nbColumns: int):
        self.nbRows = nbRows + 1
        self.nbColumns = nbColumns + 1
        self.appleEaten = 99
        self.isDead = False

        self.setupGrid()

        # Place player on the center
        self.headPos = (self.nbColumns // 2, self.nbRows // 2)
        self.grid[self.headPos] = Grid.HEAD
        self.direction = (0, 1)
        self.queue = Queue()



    def setupGrid(self):
        self.grid = np.zeros((self.nbRows + 1, self.nbColumns + 1), dtype=np.int8)

        # Setup walls on every side
        self.grid[:, 0] = Grid.WALL
        self.grid[:, self.nbColumns] = Grid.WALL
        self.grid[0, :] = Grid.WALL
        self.grid[self.nbRows, :] = Grid.WALL


    def moveHead(self):
        # Add the current headPos to the body
        self.queue.put(self.headPos)
        self.grid[self.headPos] = Grid.BODY 

        # Move head
        self.headPos = (self.headPos[0] + self.direction[0], self.headPos[1] + self.direction[1])
        if (self.grid[self.headPos] == Grid.WALL or self.grid[self.headPos] == Grid.BODY):
            self.die()
            return

        # Eat apple if its present
        if self.grid[self.headPos] == Grid.APPLE:
            self.appleEaten+=1
        self.grid[self.headPos] = Grid.HEAD

        # Make snake longer
        if self.appleEaten > 0:
            self.appleEaten -= 1
        # Remove last pos in the queue
        elif not self.queue.empty():
            lastPos = self.queue.get()
            self.grid[lastPos] = Grid.EMPTY

    
    def update(self):
        self.moveHead()


    def die(self):
        self.isDead = True
        print("You died")


grid = Grid(9, 9)

while not grid.isDead:
    grid.update()
    if not grid.isDead: print(grid.grid)

