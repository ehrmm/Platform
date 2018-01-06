"""This module contains the main game game_loop and rendering for the game
"""

#imports
import pygame
import sys
from animation import *
pygame.init()
pygame.key.set_repeat(10, 10)

#constants
DISPLAY_SURF = pygame.display.set_mode([DISPLAY_WIDTH, DISPLAY_HEIGHT])

#classes
class Game():
    def __init__(self):
        """Creates the main game object
        """
        pass

    def game_loop(self):
        """Main game loop
        """
        level = Level()
        clock = pygame.time.Clock()
        clock.tick(30)

        while True:
            print(clock.get_fps())
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                for sprite in HERO_GROUP.sprites():
                    sprite.move(event)
                    HERO_GROUP.update(sprite.image, sprite.rect)
                else:
                    pass

            for sprite in TILE_GROUP.sprites():
                TILE_GROUP.update(sprite.image, sprite.rect)
            for sprite in ENEMY_GROUP.sprites():
                #sprite.move()
                ENEMY_GROUP.update(sprite.image, sprite.rect)
            for sprite in ITEM_GROUP.sprites():
                #sprite.move()
                ITEM_GROUP.update(sprite.image, sprite.rect)

            print(TILE_GROUP.sprites())
            #rendering
            DISPLAY_SURF.fill(BLACK)
            TILE_GROUP.draw(DISPLAY_SURF)
            HERO_GROUP.draw(DISPLAY_SURF)
            ENEMY_GROUP.draw(DISPLAY_SURF)
            ITEM_GROUP.draw(DISPLAY_SURF)
            MAGIC_GROUP.draw(DISPLAY_SURF)

            pygame.display.update()

#run code
if __name__ == "__main__":
    GameObj = Game()
    GameObj.game_loop()
