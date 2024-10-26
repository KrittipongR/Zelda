import math

from src.states.BaseState import BaseState
from src.HitBox import Hitbox
import pygame
from src.recourses import *

class PlayerAttackState(BaseState):
    def __init__(self, player, dungeon=None):
        self.player = player
        self.dungeon = dungeon

        self.player.curr_animation.Refresh()
        self.player.ChangeAnimation("attack_"+self.player.direction)

    def Enter(self, params):
        #sounds
        self.player.offset_x = 24
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

        self.sword_hitbox = Hitbox(hitbox_x, hitbox_y, hitbox_width, hitbox_height)

        self.player.curr_animation.Refresh()
        print("Attack")
        self.player.ChangeAnimation("attack_"+self.player.direction)

    def Exit(self):
        pass

    def update(self, dt, events):
        for entity in self.dungeon.current_room.entities:
            if entity.Collides(self.sword_hitbox) and not entity.invulnerable:
                entity.Damage(1)
                self.power += 1
                entity.SetInvulnerable(0.2)
                if self.power >= 3:
                    if self.player.health < 6:
                        self.player.health +=1
                        entity.Damage(2)
                        gSounds['vampStrike'].play()
                    print("Vampiric Strike!")
                    self.power = 0
                print("Current Power:",self.power)
                if self.player.direction == 'right':
                    entity.x += 30
                elif self.player.direction =='left':
                    entity.x -= 30
                elif self.player.direction =='up':
                    entity.y -= 30
                elif self.player.direction =='down':
                    entity.y += 30
                gSounds['hit_enemy'].play()

        if self.player.curr_animation.times_played > 0:
            self.player.curr_animation.times_played = 0
            self.player.state_machine.Change('idle', {
                'power':self.power,
            })

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.state_machine.Change('swing_sword', {
                        'power':self.power,
                    })


    def render(self, screen):
        animation = self.player.curr_animation.image
        screen.blit(animation, (math.floor(self.player.x - self.player.offset_x), math.floor(self.player.y - self.player.offset_y)))