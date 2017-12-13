"""This module deals with all animation
"""
import pygame
pygame.init()

#constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FONT1 = pygame.font.SysFont("calibrims", 72)
FONT2 = pygame.font.SysFont("calibrims", 16)
DISPLAY_WIDTH = 500
DISPLAY_HEIGHT = 500
TILE_SIZE = 30
TILE_GROUP = pygame.sprite.Group()
HERO_GROUP = pygame.sprite.Group()
ENEMY_GROUP = pygame.sprite.Group()
ITEM_GROUP = pygame.sprite.Group()
MAGIC_GROUP = pygame.sprite.Group()
TILE_SPRITESHEET = pygame.image.load("map\Tile_sheet.png")
MAGE_SPRITESHEET = pygame.image.load("hero\mage_sheet.png")
SHROOM_SPRITESHEET = pygame.image.load("item\shroom_sheet.png")
GRASS_SPRITESHEET = pygame.image.load("enemy\grass_sheet.png")
SHRUMP_SPRITESHEET = pygame.image.load("enemy\shrump_sheet.png")
SEED_SPRITESHEET = pygame.image.load("enemy\seed_sheet.png")
TILES_DICT = {
"grass_earth_middle": [], "grass_earth_right": [], "grass_earth_left": [],
"earth_left": [], "earth_middle": [], "earth_right": [],
"box": [], "hanging_earth": [],
"down_slope_steep": [], "down_slope_shallow1": [], "down_slope_shallow2": [],
"up_slope_steep": [], "up_slope_shallow1": [], "up_slope_shallow2": [],
"ladder": [], "ladder_on_grass": []
}
MAGE_SPRITES = {
"back1": [], "back2": [], "back3": [],
"right1": [], "right2": [], "right3": [],
"left1": [], "left2": [], "left3": []
} #these will be the [topleft coordinates, width, height] for each sprite in the spritesheet
SHROOM_SPRITES = {
"back1": [], "back2": [], "back3": [],
"right1": [], "right2": [], "right3": [],
"left1": [], "left2": [], "left3": []
}
GRASS_SPRITES = {
"back1": [5, 7, 15, 25], "back2": [29, 6, 15, 25], "back3": [53, 5, 15, 25],
"right1": [5, 71, 14, 24], "right2": [29, 70, 14, 24], "right3": [53, 69, 14, 24],
"left1": [5, 104, 14, 24], "left2": [29, 103, 14, 24], "left3": [53, 102, 14, 24]
}
SHRUMP_SPRITES = {
"back1": [], "back2": [], "back3": [],
"right1": [], "right2": [], "right3": [],
"left1": [], "left2": [], "left3": []
}
SEED_SPRITES = {
"back1": [], "back2": [], "back3": [],
"right1": [], "right2": [], "right3": [],
"left1": [], "left2": [], "left3": []
}

#variables
lives = 3
hero_status = 0 # +=1 for powerup

#classes
class SpriteSheet():
    def __init__(self, spritesheet):
        """Creates a spritesheet object
        """
        print("spritesheet class init")
        pass
    def get_sprite():
        """Returns the shape (image) for a paricular sprite
        """
        print("spritesheet class get_sprite")

class Tile(pygame.sprite.Sprite):
    def __init__(self):
        """Creates a Tile sprite
        """
        pygame.sprite.Sprite.__init__(self)
        TILE_GROUP.add(self)
    def move(self):
        """Updates self.rect to allow tiles to move with time
            Most tiles won't move, but some will, there will be an if statement to determine this
        """
        pass

class Mage(pygame.sprite.Sprite):
    def __init__(self):
        """Creates a Mage sprite, player character
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("effect\explosion1.png")
        self.rect = self.image.get_rect(center = [DISPLAY_WIDTH/2, DISPLAY_HEIGHT/2])
        HERO_GROUP.add(self)
    def move(self):
        """Updates self.rect according to keyboard input so that the character may be moved using the arrow keys
        """
        self.image = pygame.transform.scale(self.image, [30, 30])
        self.rect = self.image.get_rect(center = [0, 0])
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
        pygame.sprite.Sprite.__init__(self)
        ITEM_GROUP.add(self)
    def collected(self):
        """Probably just calls Mage.powerup()
        """
        pass

class Gem(pygame.sprite.Sprite):
    def __init__(self):
        """Creates a gem sprite, life item
        """
        pygame.sprite.Sprite.__init__(self)
        ITEM_GROUP.add(self)
    def collected(self):
        """lives += 1
        """

class Grass(pygame.sprite.Sprite):
    def __init__(self):
        """Creates a grass sprite, walking enemy
        """
        pygame.sprite.Sprite.__init__(self)
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
        pygame.sprite.Sprite.__init__(self)
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
        pygame.sprite.Sprite.__init__(self)
        ENEMY_GROUP.add(self)
    def move(self):
        """Creates automatic jumping movement
        """
        pass
    def die(self):
        """Creates splash animation
        """
        pass
