import math

from src.states.BaseState import BaseState
from src.HitBox import Hitbox
import pygame
from src.recourses import *

class PlayerThrowState(BaseState):
    def __init__(self, player, dungeon=None):
        self.player = player
        self.dungeon = dungeon

        self.player.curr_animation.Refresh()
        self.player.ChangeAnimation("throw_"+self.player.direction)


    def Enter(self, params):
        #sounds
        self.player.offset_x = 0
        self.player.offset_y = 15
        self.power = params['power']

        direction = self.player.direction
        self.player.curr_animation.Refresh()
        gSounds['carry'].play()
        print("Throw")
        self.player.ChangeAnimation("throw_"+self.player.direction)

    def Exit(self):
        pass

    def update(self, dt, events):
        if self.player.curr_animation.times_played > 0:
            self.player.curr_animation.times_played = 0
            #Check
            self.player.state_machine.Change('idle', {
                'power':self.power,
            })
    def render(self, screen):
        animation = self.player.curr_animation.image
        screen.blit(animation, (math.floor(self.player.x - self.player.offset_x), math.floor(self.player.y - self.player.offset_y)))