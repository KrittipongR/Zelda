import math

from src.states.BaseState import BaseState
from src.HitBox import Hitbox
import pygame
from src.recourses import *

class PlayerCarryState(BaseState):
    def __init__(self, player, dungeon=None):
        self.player = player
        self.dungeon = dungeon

        self.player.curr_animation.Refresh()
        self.player.ChangeAnimation("carry_pot_"+self.player.direction)

    def Enter(self, params):
        
        self.player.offset_x = 0
        self.player.offset_y = 15
        self.power = params['power']

        direction = self.player.direction

        if direction == 'left':
            hitbox_width = 24
            hitbox_height = 48
            hitbox_x = self.player.x - hitbox_width
            hitbox_y = self.player.y + 6
        elif direction == 'right':
            hitbox_width = 24
            hitbox_height = 48
            hitbox_x = self.player.x + self.player.width
            hitbox_y = self.player.y + 6
        elif direction == 'up':
            hitbox_width = 48
            hitbox_height = 24
            hitbox_x = self.player.x
            hitbox_y = self.player.y - hitbox_height
        elif direction == 'down':
            hitbox_width = 48
            hitbox_height = 24
            hitbox_x = self.player.x
            hitbox_y = self.player.y + self.player.height

        self.player.curr_animation.Refresh()
        gSounds['carry'].play()
        print("Picking up Pot")
        self.player.ChangeAnimation("carry_pot_"+self.player.direction)

    def Exit(self):
        pass

    def update(self, dt, events):
        if self.player.curr_animation.times_played > 0:
            self.player.curr_animation.times_played = 0
            #self.player.ChangeState("carry_pot_idle") #check
            self.player.state_machine.Change('carry_pot_idle', {
                'power':self.power,
            })

    def render(self, screen):
        animation = self.player.curr_animation.image
        screen.blit(animation, (math.floor(self.player.x - self.player.offset_x), math.floor(self.player.y - self.player.offset_y)))