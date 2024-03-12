#RULES:
#1. This is a zero player game - evolution determined at initial state. No further input required from the players.
#2. Any live cell with fewer than two live neighbours die. - underpopulation
#3. Any live cell with two or three neighbours live on to the next generation. - statis
#4. Any dead cell with exactly three live neighbours becomes a live cell. - reproduction
#5. A live cell with more than 3 live neighnours die.
# In this game we have still lives, oscillators, space ships.

#developing the game
#1. create blank screen and the simulation loop
#2. create grid
#3. count live neighbours
#4. implement simulation rules
#5. starting and stopping the simulation
#6. create custom initial state

#divide and conquer approach

#grid - 1 for alive cells and 0 for dead. This is the foundational grid
# one square in the grid 25x25 px. So for 750 we divide by 25 to get 30.


#the update grid function gets the output in the temporary grid and then moves them to the main grid.
# r to assign at random
# enter to start
# space to stop
# c to clear

import pygame
import sys
import random

pygame.init()

grey = (29, 29, 29)
window_width = 1200
window_height = 800
cell_size = 10
fps = 12

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("GAME OF LIFE")



class Grid:
    def __init__(self, width, height, cell_size):
        self.rows = height // cell_size
        self.columns = width // cell_size
        self.cell_size = cell_size
        self.cells = [[0 for _ in range(self.columns)] for _ in range(self.rows)]

    def draw(self, window):
        for row in range(self.rows):
            for column in range(self.columns):
                color = (0, 255, 0) if self.cells[row][column] else (55, 55, 55) 
                pygame.draw.rect(window, color, (column * self.cell_size, row *  self.cell_size, self.cell_size -1, self.cell_size -1))

    def fill_random(self):
        for row in range(self.rows):
            for column in range(self.columns):
                self.cells[row][column] = random.choice([1, 0, 0, 0])

    def clear(self):
        for row in range(self.rows):
            for column in range(self.columns):
                self.cells[row][column] = 0


class Simulation:
    def __init__(self, width, height, cell_size):
        self.grid = Grid(width, height, cell_size)
        self.temp_grid = Grid(width, height, cell_size)
        self.rows = height // cell_size
        self.columns = width // cell_size
        self.run = False

    def draw(self, window):
        self.grid.draw(window)

    def count_live_neighbours(self, grid, row, column):
        live_neighbors = 0

        neighbour_offset = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for offset in neighbour_offset:
            new_row = (row + offset[0]) % self.rows
            new_column = (column + offset[1]) % self.columns
            if self.grid.cells[new_row][new_column] == 1:
                live_neighbors += 1

        return live_neighbors
    
    def update(self):
        if self.is_running():
            for row in range(self.rows):
                for column in range(self.columns):
                    live_neighbors = self.count_live_neighbours(self.grid, row, column)
                    cell_value = self.grid.cells[row][column]

                    if cell_value == 1:
                        if live_neighbors > 3 or live_neighbors < 2:
                            self.temp_grid.cells[row][column] = 0
                        else:
                            self.temp_grid.cells[row][column] = 1
                    else:
                        if live_neighbors == 3:
                            self.temp_grid.cells[row][column] = 1
                        else:
                            self.temp_grid.cells[row][column] = 0
            for row in range(self.rows):
                for column in range(self.columns):
                    self.grid.cells[row][column] = self.temp_grid.cells[row][column]

    def is_running(self):
        return self.run
    
    def start(self):
        self.run = True

    def stop(self):
        self.run = False

    def clear(self):
        if self.is_running() == False:
            self.grid.clear()

    def create_random_state(self):
        if self.is_running() == False:
            self.grid.fill_random()

    



clock = pygame.time.Clock()
simulation = Simulation(window_width, window_height, cell_size)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                simulation.start()
                pygame.display.set_caption("GAME IS RUNNING")
            elif event.key == pygame.K_SPACE:
                simulation.stop()
                pygame.display.set_caption("GAME HAS STOPPED")
            elif event.key == pygame.K_f:
                fps += 2
            elif event.key == pygame.K_s:
                if fps > 2:
                    fps -= 2
            elif event.key == pygame.K_r:
                simulation.create_random_state()
            elif event.key == pygame.K_c:
                simulation.clear()
                
            

    simulation.update()

    window.fill(grey)
    simulation.draw(window)
    
    pygame.display.update()
    clock.tick(fps)
