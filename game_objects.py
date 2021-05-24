from random import random

class Cell:
    def __init__(self, x_index, y_index, is_bomb):
        self.uncovered = False
        self.flagged = False
        self.x_index = x_index
        self.y_index = y_index
        self.is_bomb = is_bomb
        self.number = 0

    def get_neighbours(self, grid):
        neighbours = []
        for x in range(-1,2):
            for y in range(-1,2):
                #own position is not a neighbour
                if x == y == 0: continue
                #edge cases
                if not (0 <= self.x_index + x < grid.width): continue
                if not (0 <= self.y_index + y < grid.height): continue
                #append this index to neighbours
                neighbours.append((self.x_index + x, self.y_index + y))
        return neighbours
                

    def uncover(self, grid, manual = False):
        if self.is_bomb == manual == True:
            #end game
            print("Game Over")
            quit()

        self.uncovered = True
        if not self.number == 0: return

        neighbours = self.get_neighbours(grid)
        for neighbour in neighbours:
            #uncover grid.cells[neighbour[0]][neighbour[1]]
            pass

class Grid:
    def __init__(self, width, height, difficulty):
        self.width = width
        self.height = height

        self.cells = []

        for x in range(width):
            cells.append([])
            for y in range(height):
                is_bomb = random() > 0.5
                cells[x].append(Cell(x, y, is_bomb))
                
