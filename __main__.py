"""This module contains the main game game_loop and rendering for the game
"""

#imports
import pygame
import sys
from animation import *
pygame.init()

#constants
DISPLAY_SURF = pygame.display.set_mode([DISPLAY_WIDTH, DISPLAY_HEIGHT])

#classes
class Game():
    def __init__(self):
        """Creates the main game object
        """
        pass

    def intro(self):
        pass

    def level1(self):
        tile_map = [] # an array of numbers, each of which refers to a tile from the tile spritesheet
        enemies = []
        items = []

    def level2(self):
        pass

    def game_loop(self):
        """Main game loop
        """
        mage = Mage()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                else:
                    pass

            for sprite in HERO_GROUP.sprites():
                sprite.move()
            HERO_GROUP.update(mage.image, mage.rect)

            #rendering
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
