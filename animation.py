"""This module deals with all animation
"""
import pygame
pygame.init()

#constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FONT1 = pygame.font.SysFont("calibrims", 72)
FONT2 = pygame.font.SysFont("calibrims", 16)
DISPLAY_WIDTH = 650
DISPLAY_HEIGHT = 650
TILE_SIZE = 30
TILE_GROUP = pygame.sprite.Group()
HERO_GROUP = pygame.sprite.Group()
ENEMY_GROUP = pygame.sprite.Group()
ITEM_GROUP = pygame.sprite.Group()
MAGIC_GROUP = pygame.sprite.Group()
TILE_SPRITE_POSITIONS = {
"grass_earth_middle": [0, 0, 65, 65], "grass_earth_right": [65, 0, 65, 65], "grass_earth_left": [65*2, 0, 65, 65],
"earth_left": [7*65, 65, 65, 65], "earth_middle": [6*65, 65, 65, 65], "earth_right": [2*65, 65, 65, 65],
"box": [6*65, 0, 65, 65], "hanging_earth": [65, 65],
"down_slope_steep": [4*65, 2*65, 65, 65], "down_slope_shallow1": [0, 3*65, 65, 65], "down_slope_shallow2": [65, 3*65, 65, 65],
"up_slope_steep": [0, 7*65, 65, 65], "up_slope_shallow1": [4*65, 6*65, 65, 65], "up_slope_shallow2": [5*65, 6*65, 65, 65],
"ladder": [4*65, 5*65, 65, 65], "ladder_on_grass": [5*65, 5*65, 65, 65],
"tunnel1": [2*65, 4*65, 65, 65], "tunnel2": [3*65, 4*65, 65, 65], "tunnel3": [4*65, 4*65, 65, 65],
"hole_top": [5*65, 65, 65, 65], "hole_bottom": [7*65, 3*65, 65, 65]
}
MAGE_SPRITE_POSITIONS = {
"back1": [5, 4, 14, 28], "back2": [29, 3, 14, 28], "back3": [52, 4, 14, 28],
"right1": [5, 37, 14, 28], "right2": [29, 36, 14, 28], "right3": [53, 37, 14, 28],
"left1": [6, 101, 14, 28], "left2": [30, 100, 14, 28], "left3": [54, 101, 14, 28]
} #these will be the [topleft coordinates, width, height] for each sprite in the spritesheet
SHROOM_SPRITE_POSITIONS = {
"back1": [], "back2": [], "back3": [],
"right1": [], "right2": [], "right3": [],
"left1": [], "left2": [], "left3": []
}
GRASS_SPRITE_POSITIONS = {
"back1": [5, 7, 15, 25], "back2": [29, 6, 15, 25], "back3": [53, 5, 15, 25],
"right1": [5, 71, 14, 24], "right2": [29, 70, 14, 24], "right3": [53, 69, 14, 24],
"left1": [5, 104, 14, 24], "left2": [29, 103, 14, 24], "left3": [53, 102, 14, 24]
}
SHRUMP_SPRITE_POSITIONS = {
"back1": [], "back2": [], "back3": [],
"right1": [], "right2": [], "right3": [],
"left1": [], "left2": [], "left3": []
}
SEED_SPRITE_POSITIONS = {
"back1": [], "back2": [], "back3": [],
"right1": [], "right2": [], "right3": [],
"left1": [], "left2": [], "left3": []
}

#variables
lives = 3
hero_status = 0 # +=1 for powerup

#classes
class SpriteSheet():
    def __init__(self, spritesheet, sprite_positions):
        """Creates a spritesheet object
        """
        self.spritesheet = spritesheet
        self.sprite_positions = sprite_positions

    def get_sprite(self, sprite):
        """Returns the shape (image) for a paricular sprite
        """
        surf = pygame.Surface((self.sprite_positions[sprite][2], self.sprite_positions[sprite][3]))
        surf.blit(self.spritesheet, (-self.sprite_positions[sprite][0], -self.sprite_positions[sprite][1])) # area =
        return surf

#Tile = SpriteSheet(pygame.image.load("map\Tile_sheet.png"), TILE_SPRITE_POSITIONS)
#Shroom = SpriteSheet(pygame.image.load("item\shroom_sheet.png"), SHROOM_SPRITE_POSITIONS)
#Grass = SpriteSheet(pygame.image.load("enemy\grass_sheet.png"), GRASS_SPRITE_POSITIONS)
#Shrump = SpriteSheet(pygame.image.load("enemy\shrump_sheet.png"), SHRUMP_SPRITE_POSITIONS)
#Seed = SpriteSheet(pygame.image.load("enemy\seed_sheet.png"), SEED_SPRITE_POSITIONS)

class Level():
    def __init__(self):
        self.tile_map = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self.level1()

    def level1(self):
        self.tile_map = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self.sprite_map = {
        "mage": [(0, 0)], #position wrt tile map
        "shroom": (),
        "gem": (),
        "grass": (),
        "shrump": (),
        "seed": ()
        }
        row_number = 0
        column_number = 0
        for row in self.tile_map:
            for number in row:
                if number == 0:
                    pass
                else:
                    Tile(number, row_number, column_number)
                column_number += 1
            row_number += 1

        for position in self.sprite_map["mage"]:
            Mage(position)


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_number, row_number, column_number):
        """Creates a Tile sprite
        """
        pygame.sprite.Sprite.__init__(self)
        self.tile_numbers = {
        1: "grass_earth_middle", 2: "grass_earth_right", 3: "grass_earth_left",
        4: "earth_left", 5: "earth_middle", 6: "earth_right",
        7: "box", 8: "hanging_earth",
        9: "down_slope_steep", 10: "down_slope_shallow1", 11: "down_slope_shallow2",
        12: "up_slope_steep", 13: "up_slope_shallow1", 14: "up_slope_shallow2",
        15: "ladder", 16: "ladder_on_grass",
        17: "tunnel1", 18: "tunnel2", 19: "tunnel3",
        20: "hole_top", 21: "hole_bottom"
        }
        self.spritesheet = SpriteSheet(pygame.image.load("map\Tile_sheet.png"), TILE_SPRITE_POSITIONS)
        self.image = self.spritesheet.get_sprite(self.tile_numbers[tile_number])
        self.rect = self.image.get_rect(topleft = (row_number*65, column_number*65))
        TILE_GROUP.add(self)
        print("tile made")

    def move(self):
        """Updates self.rect to allow tiles to move with time
            Most tiles won't move, but some will, there will be an if statement to determine this
        """
        pass

class Mage(pygame.sprite.Sprite):
    def __init__(self, position):
        """Creates a Mage sprite, player character
        """
        pygame.sprite.Sprite.__init__(self)
        self.spritesheet = SpriteSheet(pygame.image.load("hero\Trans_mage_sheet.png"), MAGE_SPRITE_POSITIONS)
        self.x = TILE_SIZE/2 + position[0]*TILE_SIZE
        self.y = DISPLAY_HEIGHT - TILE_SIZE/2 - position[1]*TILE_SIZE
        self.image = self.spritesheet.get_sprite("left1")
        self.rect = self.image.get_rect(center = [self.x, self.y])
        HERO_GROUP.add(self)
        self.count = 0

    def move(self, event):
        """Updates self.rect according to keyboard input so that the character may be moved using the arrow keys
        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if self.x == TILE_SIZE/2:
                    pass
                else:
                    if self.count == 0:
                        self.image = self.spritesheet.get_sprite("left1")
                        self.count += 1
                    elif self.count == 1:
                        self.image = self.spritesheet.get_sprite("left2")
                        self.count += 1
                    elif self.count == 2:
                        self.image = self.spritesheet.get_sprite("left3")
                        self.count += 1
                    elif self.count == 3:
                        self.image = self.spritesheet.get_sprite("left2")
                        self.count = 0
                    self.x -= 1
            elif event.key == pygame.K_RIGHT:
                if self.x == DISPLAY_WIDTH - TILE_SIZE/2:
                    pass
                else:
                    if self.count == 0:
                        self.image = self.spritesheet.get_sprite("right1")
                        self.count += 1
                    elif self.count == 1:
                        self.image = self.spritesheet.get_sprite("right2")
                        self.count += 1
                    elif self.count == 2:
                        self.image = self.spritesheet.get_sprite("right3")
                        self.count = 0
                    elif self.count == 3:
                        self.image = self.spritesheet.get_sprite("right2")
                        self.count = 0
                    self.x += 1
            elif event.key == pygame.K_UP:
                print("UP")
            else:
                pass
        self.rect = self.image.get_rect(center = [self.x, self.y])
    def powerup(self):
        """Changes colour palette of self and += 1 to status
        """
        pass
    def die(self):
        """Probably just call game over
        """
        pass

class Shroom(pygame.sprite.Sprite):
    def __init__(self, position):
        """Creates a shroom sprite, powerup item
        """
        pygame.sprite.Sprite.__init__(self)
        self.x = position[0]
        self.y = position[1]
        ITEM_GROUP.add(self)
    def collected(self):
        """Probably just calls Mage.powerup()
        """
        pass

class Gem(pygame.sprite.Sprite):
    def __init__(self, position):
        """Creates a gem sprite, life item
        """
        pygame.sprite.Sprite.__init__(self)
        self.x = position[0]
        self.y = position[1]
        ITEM_GROUP.add(self)
    def collected(self):
        """lives += 1
        """

class Grass(pygame.sprite.Sprite):
    def __init__(self, position):
        """Creates a grass sprite, walking enemy
        """
        pygame.sprite.Sprite.__init__(self)
        self.x = position[0]
        self.y = position[1]
        self.image = pygame.image.load("effect\explosion1.png")
        self.rect = self.image.get_rect(center = [DISPLAY_WIDTH/2, DISPLAY_HEIGHT/2])
        ENEMY_GROUP.add(self)
    def move(self):
        """Creates automatic walking movement
        """
        self.image = pygame.transform.scale(self.image, [30, 30])
        self.rect = self.image.get_rect(center = [0, 0])
    def die(self):
        """Creates splash animation
        """
        pass

class Shrump(pygame.sprite.Sprite):
    def __init__(self, position):
        """Creates a shrump sprite, static enemy
        """
        pygame.sprite.Sprite.__init__(self)
        self.x = position[0]
        self.y = position[1]
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
    def __init__(self, position):
        """Creates a seed sprite, jumping enemy
        """
        pygame.sprite.Sprite.__init__(self)
        self.x = position[0]
        self.y = position[1]
        ENEMY_GROUP.add(self)
    def move(self):
        """Creates automatic jumping movement
        """
        pass
    def die(self):
        """Creates splash animation
        """
        pass
