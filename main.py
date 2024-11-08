import pygame
import sys
from game import Game

#make screen
pygame.init()
screen = pygame.display.set_mode((400,720))
clock = pygame.time.Clock() 
game = Game("img/bird.png", "img/pipe.png", "img/background.png", "img/ground.png")
game.resize_images()

#allow the player to keep the game open
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game.active:
                game.flap()
    
    game.show_background(screen)

    if game.active:
        game.show_bird(screen)
        game.update_bird()
    

    game.show_ground(screen)
    game.move_ground()

    pygame.display.update()
    clock.tick(120)

