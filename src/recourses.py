import pygame
from src.Util import SpriteManager, Animation
import src.Util as Util
from src.StateMachine import *

g_state_manager = StateMachine()

sprite_collection = SpriteManager().spriteCollection


gPlayer_animation_list = {"down": sprite_collection["character_walk_down"].animation,
                         "right": sprite_collection["character_walk_right"].animation,
                         "up": sprite_collection["character_walk_up"].animation,
                         "left": sprite_collection["character_walk_left"].animation,
                        "attack_down": sprite_collection["character_attack_down"].animation,
                        "attack_right": sprite_collection["character_attack_right"].animation,
                        "attack_up": sprite_collection["character_attack_up"].animation,
                        "attack_left": sprite_collection["character_attack_left"].animation,
                        "throw_down": sprite_collection["character_throw_down"].animation,
                        "throw_right": sprite_collection["character_throw_right"].animation,
                        "throw_up": sprite_collection["character_throw_up"].animation,
                        "throw_left": sprite_collection["character_throw_left"].animation,
                        "carry_pot_down": sprite_collection["character_carry_down"].animation,
                        "carry_pot_right": sprite_collection["character_carry_right"].animation,
                        "carry_pot_up": sprite_collection["character_carry_up"].animation,
                        "carry_pot_left": sprite_collection["character_carry_left"].animation,
                        "carry_down": sprite_collection["character_walk_carry_down"].animation,
                        "carry_right": sprite_collection["character_walk_carry_right"].animation,
                        "carry_up": sprite_collection["character_walk_carry_up"].animation,
                        "carry_left": sprite_collection["character_walk_carry_left"].animation,
}

gSkeleton_animation_list = {"down": sprite_collection["skeleton_walk_down"].animation,
                         "right": sprite_collection["skeleton_walk_right"].animation,
                         "up": sprite_collection["skeleton_walk_up"].animation,
                         "left": sprite_collection["skeleton_walk_left"].animation,
}
gSlime_animation_list = {"down": sprite_collection["slime_walk_down"].animation,
                         "right": sprite_collection["slime_walk_right"].animation,
                         "up": sprite_collection["slime_walk_up"].animation,
                         "left": sprite_collection["slime_walk_left"].animation,
}
gSpider_animation_list = {"down": sprite_collection["spider_walk_down"].animation,
                         "right": sprite_collection["spider_walk_right"].animation,
                         "up": sprite_collection["spider_walk_up"].animation,
                         "left": sprite_collection["spider_walk_left"].animation,
}
gBat_animation_list = {"down": sprite_collection["bat_walk_down"].animation,
                         "right": sprite_collection["bat_walk_right"].animation,
                         "up": sprite_collection["bat_walk_up"].animation,
                         "left": sprite_collection["bat_walk_left"].animation,
}


gHeart_image_list = [sprite_collection["heart_0"].image,sprite_collection["heart_2"].image,
                    sprite_collection["heart_4"].image]

gRoom_image_list = Util.GenerateTiles("./graphics/tilesheet.png", 16, 16)
gDoor_image_list = Util.GenerateTiles("./graphics/tilesheet.png", 16, 16, colorkey=(13, 7, 17, 255))
gSwitch_image_list = Util.GenerateTiles("./graphics/switches.png", 16, 18)
gPot_image_list = Util.GenerateTiles("./graphics/tilesheet.png", 16, 16, colorkey=(0, 0, 0))

gSounds = {
    'music': pygame.mixer.Sound('sounds/music.mp3'),
    'sword':  pygame.mixer.Sound('sounds/sword.wav'),
    'hit_enemy':  pygame.mixer.Sound('sounds/hit_enemy.wav'),
    'hit_player':  pygame.mixer.Sound('sounds/hit_player.wav'),
    'door':  pygame.mixer.Sound('sounds/door.wav'),
    'vampStrike': pygame.mixer.Sound('sounds/VampiricStrike.wav'),
    'carry': pygame.mixer.Sound('sounds/PickPot.wav'),
    'break': pygame.mixer.Sound('sounds/Potbroke.wav')
}

gFonts = {
    'small': pygame.font.Font('fonts/font.ttf', 24),
    'medium': pygame.font.Font('fonts/font.ttf', 48),
    'large': pygame.font.Font('fonts/font.ttf', 96),
    'zelda_small': pygame.font.Font('fonts/zelda.otf', 96),
    'zelda': pygame.font.Font('fonts/zelda.otf', 192),
    'gothic_medium': pygame.font.Font('fonts/GothicPixels.ttf', 48),
    'gothic_large': pygame.font.Font('fonts/GothicPixels.ttf', 96),

}