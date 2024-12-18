import pygame
import sys
from game import Game

#make screen
pygame.init()
screen = pygame.display.set_mode((400,720) )
clock = pygame.time.Clock() 

SPAWNPIPES = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPES, 1800)

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

            if event.key == pygame.K_SPACE and game.active == False:
                game.restart()
    
        if event.type == SPAWNPIPES:
            game.add_pipe()

        

    game.show_background(screen)

    if game.active:
        game.show_bird(screen)
        game.update_bird()
        game.move_pipes()
        game.show_pipes(screen)
        game.check_collision()
        game.update_score()
        game.show_score("playing", screen, (212, 255, 197))
    
    else:
        game.game_over(screen,(197, 132, 87))

    game.show_ground(screen)
    game.move_ground()

    pygame.display.update()
    clock.tick(120)

