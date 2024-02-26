import pygame
from pygame.locals import *

pygame.init()

screen_width = 600
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("BREAKOUT")

font = pygame.font.SysFont('Constantia', 30)

bg = (0, 0, 0)

#block colours
block_blue1 = (0, 0, 255)
block_blue2 = (0, 204, 255)
block_blue3 = (204, 255, 255)
#paddle colours
paddle_col = (234, 218, 184)
paddle_outline = (100, 100, 100)
text_colour = (78, 81, 139)

#defining game variables
cols = 6
rows = 6
clock = pygame.time.Clock()
fps = 60
live_ball = False
game_over = 0


def draw_text(text, font, text_colour, x, y):
    img = font.render(text, True, text_colour)
    screen.blit(img, (x, y))

#brick wall class
class Wall():
    def __init__(self):
        self.width = screen_width // cols
        self.height = 50

    def create_wall(self):
        self.blocks = []
        #define an empty list for an individual block
        block_individual = []
        for row in range(rows):
            #reset the block row list
            block_row = []
            #iterate through each column in that row
            for col in range(cols):
                #generate x and y positions
                #create a rectangle from the above
                block_x = col * self.width
                block_y = row * self.height
                rect = pygame.Rect(block_x, block_y, self.width, self.height)
                #assign blovk strength based on row
                if row < 2:
                    strength = 3
                elif row < 4:
                    strength = 2
                elif row < 6:
                    strength = 1
                #create a list at this point to store the rectangle and colour data
                block_individual = [rect, strength]
                #append individual block to block row
                block_row.append(block_individual)
            # append row to the full list of blocks
            self.blocks.append(block_row)


    def draw_wall(self):
        for row in self.blocks:
            for block in row:
                #assign a colour based on the block strength
                if block [1] == 3:
                    block_col = block_blue1
                elif block [1] == 2:
                    block_col = block_blue2
                elif block [1] == 1:
                    block_col = block_blue3
                pygame.draw.rect(screen, block_col, block[0])
                pygame.draw.rect(screen, bg, (block[0]), 2) 


class Paddle():
    def __init__(self):
        #self.height = 20
        #self.width = int(screen_width / cols)
        #self.x = int((screen_width / 2) - (self.width / 2))
        #self.y = screen_height - (self.height * 2)
        #self.speed = 10
        #self.rect = Rect(self.x, self.y, self.width, self.height)
        #self.direction = 0

        self.reset()

    
    def move(self):
        #reset mpvement direction
        self.direction = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
            self.direction = -1
        elif key[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.x += self.speed
            self.direction = 1


    def draw(self):
        pygame.draw.rect(screen, paddle_col, self.rect)
        pygame.draw.rect(screen, paddle_outline, self.rect, 3)

    def reset(self):
        self.height = 20
        self.width = int(screen_width / cols)
        self.x = int((screen_width / 2) - (self.width / 2))
        self.y = screen_height - (self.height * 2)
        self.speed = 10
        self.rect = Rect(self.x, self.y, self.width, self.height)
        self.direction = 0



#ball class
class game_Ball():
    def __init__(self, x, y):
        #self.ball_rad = 10
        #self.x = x - self.ball_rad
        #self.y = y
        #self.rect = Rect(self.x, self.y, self.ball_rad * 2, self.ball_rad * 2)
        #self.speed_x = 4
        #self.speed_y = -4
        #self.speed_max = 5
        #self.game_over = 0

        self.reset(x, y)

    def move(self):

        collision_threshold = 5

        #start off witht eh assumption that wall has been destroyed completely
        wall_destroyed = 1
        row_count = 0
        for row in wall.blocks:
            item_count = 0
            for item in row:
                #check collision
                if self.rect.colliderect(item[0]):
                    #check if collision was from above
                    if abs(self.rect.bottom - item[0].top) < collision_threshold and self.speed_y > 0:
                        self.speed_y *= -1
                    #check if collision was from bottom
                    if abs(self.rect.top - item[0].bottom) < collision_threshold and self.speed_y < 0:
                        self.speed_y *= -1
                    #check if collision was from left
                    if abs(self.rect.right - item[0].left) < collision_threshold and self.speed_x > 0:
                        self.speed_x *= -1
                    #check if collision was from right
                    if abs(self.rect.left - item[0].right) < collision_threshold and self.speed_x < 0:
                        self.speed_x *= -1

                    #reduce block strength with damage
                    if wall.blocks[row_count][item_count][1] > 1:
                        wall.blocks[row_count][item_count][1] -= 1
                    else:
                        wall.blocks[row_count][item_count][0] = (0, 0, 0, 0)

                #check if block still exists, in which case the wall is not destroyed
                if wall.blocks[row_count][item_count][0] != (0, 0, 0, 0):
                    wall_destroyed = 0
                #increase item counter
                item_count += 1
            #increase row counter
            row_count += 1
        #after iterating through all the blocks, check if wall is destroyed
            if wall_destroyed == 1:
                self.game_over = 1


        #check for collision with walls
        if self.rect.left < 0 or self.rect.right > screen_width:
            self.speed_x *= -1
        
        #check for collision with top and bottom walls
        if self.rect.top < 0:
            self.speed_y *= -1
        if self.rect.bottom > screen_height:
            self.game_over = -1


        #look for collisions with paddle
        if self.rect.colliderect(player_paddle): 
            #check for collisions from the top
            if abs(self.rect.bottom - player_paddle.rect.top) < collision_threshold and self.speed_y > 0:
                self.speed_y *= -1
                self.speed_x += player_paddle.direction
                if self.speed_x > self.speed_max:
                    self.speed_x = self.speed_max
                elif self.speed_x < 0 and self.speed_x < self.speed_max:
                    self.speed_x = -self.speed_max
            else:
                self.speed_x *= -1

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        return self.game_over

    def draw(self):
        pygame.draw.circle(screen, paddle_col, (self.rect.x + self.ball_rad, self.rect.y + self.ball_rad), self.ball_rad)
        pygame.draw.circle(screen, paddle_outline, (self.rect.x + self.ball_rad, self.rect.y + self.ball_rad), self.ball_rad, 3)


    def reset(self, x, y):
        self.ball_rad = 10
        self.x = x - self.ball_rad
        self.y = y
        self.rect = Rect(self.x, self.y, self.ball_rad * 2, self.ball_rad * 2)
        self.speed_x = 4
        self.speed_y = -4
        self.speed_max = 5
        self.game_over = 0
    

wall = Wall()
wall.create_wall()

player_paddle = Paddle()

#create ball
ball = game_Ball(player_paddle.x + (player_paddle.width // 2), player_paddle.y - player_paddle.height)


run = True
while run:


    clock.tick(fps)
    screen.fill(bg)

    #draw all objects 
    wall.draw_wall()
    player_paddle.draw()
    ball.draw()

    if live_ball:
        #draw paddle
        player_paddle.move()
        #draw ball
        game_over = ball.move()
        if game_over != 0:
            live_ball = False

    if not live_ball:
        if game_over == 0:
            draw_text("CLICK ANYWHERE TO START", font, text_colour, 100, screen_height // 2 + 100)
        elif game_over == 1:
            draw_text("YOU WON!", font, text_colour, 240, screen_height // 2 + 50)
            draw_text("CLICK ANYWHERE TO START", font, text_colour, 100, screen_height // 2 + 100)
        elif game_over == -1:
            draw_text("YOU LOST!", font, text_colour, 240, screen_height // 2 + 50)
            draw_text("CLICK ANYWHERE TO START", font, text_colour, 100, screen_height // 2 + 100)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and live_ball == False:
            live_ball = True
            ball.reset(player_paddle.x + (player_paddle.width // 2), player_paddle.y - player_paddle.height)
            player_paddle.reset()
            wall.create_wall()

    pygame.display.update()

pygame.quit()
