from src.states.entity.EntityIdleState import EntityIdleState
import pygame

class PlayerIdleState(EntityIdleState):
    def __init__(self, player,dungeon):
        super(PlayerIdleState, self).__init__(player,dungeon)
        self.dungeon = dungeon

    def Enter(self, params):
        self.entity.offset_y = 15
        self.entity.offset_x = 0
        self.power = params['power']
        super().Enter(params)

    def Exit(self):
        pass

    def update(self, dt, events):
        pressedKeys = pygame.key.get_pressed()
        if pressedKeys[pygame.K_LEFT] or pressedKeys [pygame.K_RIGHT] or pressedKeys [pygame.K_UP] or pressedKeys [pygame.K_DOWN]:
            self.entity.state_machine.Change('walk', {
                'power':self.power,
            })

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.entity.state_machine.Change('swing_sword', {
                        'power':self.power,
                    })