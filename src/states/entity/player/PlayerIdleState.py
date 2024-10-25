from src.states.entity.EntityIdleState import EntityIdleState
import pygame

class PlayerIdleState(EntityIdleState):
    def __init__(self, player,dungeon):
        super(PlayerIdleState, self).__init__(player,dungeon)
        self.dungeon = dungeon

    def Enter(self, params):
        self.entity.offset_y = 15
        self.entity.offset_x = 0
        super().Enter(params)

    def Exit(self):
        pass

    def update(self, dt, events):
        pressedKeys = pygame.key.get_pressed()
        if pressedKeys[pygame.K_LEFT] or pressedKeys [pygame.K_RIGHT] or pressedKeys [pygame.K_UP] or pressedKeys [pygame.K_DOWN]:
            self.entity.ChangeState('walk')

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.entity.ChangeState('swing_sword')
                # elif event.key == pygame.K_f:
                #     for object in self.dungeon.current_room.objects:
                #         if object.type == 'pot' and self.entity.Collides(object):
                #             if self.entity.curr_animation.times_played > 0:
                #                 self.entity.curr_animation.times_played = 0
                #                 self.entity.ChangeState("carry_pot")  #check