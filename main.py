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
    
    game.show_background(screen)

    pygame.display.update()
    clock.tick(120)

