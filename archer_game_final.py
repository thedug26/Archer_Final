import pygame
from adventurer import Adventurer
from target import Target
from archer_game_constants import *
from archer_background import *

# Set the width and height of the game window
#WIDTH = 1200
#HEIGHT = 600

pygame.init()
# create clock
clock = pygame.time.Clock()

# Create a timer to end the game after X seconds
start_ticks=pygame.time.get_ticks()#starter tick

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# make arrows group
arrows = pygame.sprite.Group()


# Create an adventurer at left of the screen
my_adventurer = Adventurer(4*TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE * 5 -5, arrows, screen)

# Create a target
my_target = Target(SCREEN_WIDTH-4*TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE * 5 -5, screen)

# Set the running flag to True
running = True

background=screen.copy()
draw_background(background)

# Main game loop
score = 0

while running:
    # Check for events
    for event in pygame.event.get():
        # If the user closes the window, set running to False
        if event.type == pygame.QUIT:
            running = False



    # Set the game's FPS
    clock.tick(120)

    screen.fill('black')

    screen.blit(background, (0, 0))
    # Update the adventurer & arrows
    my_adventurer.update()
    arrows.update()

    # Draw the adventurer, arrows, & target
    #[b.draw(my_target, screen) for b in arrows]
    for b in arrows:
        b.draw(my_target, screen)
        score += b.score
        if b.score:
            b.kill()
    #create timer
    seconds = (pygame.time.get_ticks() - start_ticks) // 1000  # calculate how many seconds
    if seconds > 60:  # if more than 10 seconds close the game
        break
    print(score)

    my_adventurer.draw()
    my_target.draw()
    score_font = pygame.font.Font("../Archer_Final/assets/fonts/Kenney Future.ttf", 48)
    #timer and score texts
    text = score_font.render(f'Score: {score}', True, (255, 0, 0))
    timer_text = score_font.render(f'Time: {60-seconds}', True, (255, 0, 0))
    #displays timer and scoreboard
    screen.blit(text, (SCREEN_WIDTH/1.2-text.get_width()/2, SCREEN_HEIGHT-SCREEN_HEIGHT*0.9))
    screen.blit(timer_text, (SCREEN_WIDTH/5-timer_text.get_width()/2, SCREEN_HEIGHT-SCREEN_HEIGHT*0.9))

    background = screen.copy()
    draw_background(background)
    # Update the display
    pygame.display.flip()

pygame.quit()
