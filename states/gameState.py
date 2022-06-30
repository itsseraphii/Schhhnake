import pygame

from renderer import Renderer
from .state import State
from ball import Ball

class GameState(State):
    def __init__(self, game, renderer: Renderer):
        super().__init__(game, renderer)

        ball = pygame.image.load("res/intro_ball.gif")
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(Ball(ball))


    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.display.quit()
            elif event.type == pygame.VIDEORESIZE:
                self.renderer.resizeDisplay(event.size)

        self.all_sprites.update()


    def render(self):
        self.renderer.clear()
        self.renderer.drawSpriteGroup(self.all_sprites)
        self.renderer.render()