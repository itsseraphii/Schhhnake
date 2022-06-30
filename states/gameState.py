import pygame

from display import Renderer
from sprites import Ball

from .state import State

class GameState(State):
    def __init__(self, game, renderer: Renderer):
        super().__init__(game, renderer)

        ball = pygame.image.load("res/intro_ball.gif")
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(Ball(ball))


    def update(self) -> None:
        self.all_sprites.update()


    def draw(self) -> None:
        self.renderer.drawSpriteGroup(self.all_sprites)
