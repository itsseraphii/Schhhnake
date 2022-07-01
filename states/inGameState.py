from tempfile import NamedTemporaryFile
from typing import NamedTuple
import pygame

from display import Renderer
from sprites import Ball

from .state import State


class InGameStatePayload(NamedTuple):
    text: str
    level: int



class InGameState(State):
    def __init__(self, game, renderer: Renderer):
        super().__init__(game, renderer)
        self.ball_surf = pygame.image.load("res/intro_ball.gif")
        self.font = pygame.font.Font('./res/SnakeFont.ttf', 24)


    def update(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                self.game.switchState(InGameState, InGameStatePayload(f'Niveau {self.curLevel}', self.curLevel + 1))

        self.all_sprites.update()


    def draw(self) -> None:
        self.renderer.drawSpriteGroup(self.all_sprites)


    def onEnterState(self, payload: InGameStatePayload) -> None:
        self.curLevel = payload.level
        
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(Ball(self.ball_surf, [self.curLevel * 5, self.curLevel * 5]))
        


    def onExitState(self) -> None:
        for sprite in self.all_sprites:
            sprite.kill()

