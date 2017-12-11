#imports
import pygame
pygame.__init__()

#constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FONT1 = pygame.font.SysFont("calibrims", 72)
FONT2 = pygame.font.SysFont("calibrims", 16)
TILE_SIZE = 30
DISPLAY_WIDTH = 500
DISPLAY_HEIGHT = 500
TILE_GROUP = pygame.sprite.Group()
HERO_GROUP = pygame.sprite.Group()
ENEMY_GROUP = pygme.sprite.Group()
ITEM_GROUP = pygame.sprite.Group()
MAGIC_GROUP = pygame.sprite.Group()
MAGE_SPRITES = [] #these will be the topleft coordinates and (width, height) for each sprite in the spritesheet
SHROOM_SPRITES = []
GRASS_SPRITES = []
SHRUMP_SPRITES = []
SEED_SPRITES = []

#variables
lives = 3
hero_status = 0 # +=1 for powerup

#classes
class SpriteSheet():
    def __init__(self, spritesheet):
        """Creates a spritesheet object
        """
        pass
    def get_sprite():
        """Returns the shape (image) for a paricular sprite
        """
        pass

class Mage(pygame.sprite.Sprite):
    def __init__(self):
        """Creates a Mage sprite, player character
        """
        pygame.sprite.Sprite.__init__()
        HERO_GROUP.add(self)
    def control(self):
        """Updates self.rect according to keyboard input so that the character may be moved using the arrow keys
        """
        pass
    def powerup(self):
        """Changes colour palette of self and += 1 to status
        """
        pass
    def die(self):
        """Probably just call game over
        """
        pass

class Shroom(pygame.sprite.Sprite):
    def __init__(self):
        """Creates a shroom sprite, powerup item
        """
        pygame.sprite.Sprite.__init__()
        ITEM_GROUP.add(self)
    def collected(self):
        """Probably just calls Mage.powerup()
        """
        pass

class Gem(pygame.sprite.Sprite):
    def __init__(self):
        """Creates a gem sprite, life item
        """
        pygame.sprite.Sprite.__init__()
        ITEM_GROUP.add(self)

class Grass(pygame.sprite.Sprite):
    def __init__(self):
        """Creates a grass sprite, walking enemy
        """
        pygame.sprite.Sprite.__init__()
        ENEMY_GROUP.add(self)
    def move(self):
        """Creates automatic walking movement
        """
        pass
    def die(self):
        """Creates splash animation
        """
        pass

class Shrump(pygame.sprite.Sprite):
    def __init__(self):
        """Creates a shrump sprite, static enemy
        """
        pygame.sprite.Sprite.__init__()
        ENEMY_GROUP.add(self)
    def move(self):
        """Creates automatic shifting movement
        """
        pass
    def die(self):
        """Creates splash animation
        """
        pass

class Seed(pygame.sprite.Sprite):
    def __init__(self):
        """Creates a seed sprite, jumping enemy
        """
        pygame.sprite.Sprite.__init__()
        ENEMY_GROUP.add(self)
    def move(self):
        """Creates automatic jumping movement
        """
        pass
    def die(self):
        """Creates splash animation
        """
        pass

class Game():
    def __init__(self):
        """
        Creates the main game object
        """
        pass
    def game_loop(self):
        """
        Main game loop
        """
        pass

#run code
if __name__ == __main__:
    GameObj = Game()
    GameObj.game_loop()
