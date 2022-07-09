import pygame

from display import Renderer
from sprites import Player

from .state import State
from .payloads import InGameStatePayload

class InGameState(State):
    def __init__(self, game, renderer: Renderer):
        super().__init__(game, renderer)

        self.backgroundSurf = pygame.image.load("res/map.png")
        self.playerSurf = pygame.image.load("res/player.png")


    def update(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                self.game.switchState("InGameState", InGameStatePayload(f'Niveau {self.curLevel}', self.curLevel + 1))
            if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
                self.game.switchState("MenuState")

        self.player.update()


    def draw(self) -> None:
        self.renderer.drawSurface(self.backgroundSurf, (0, 0))
        self.renderer.drawSurface(self.player.image, self.player.rect.topleft)


    def onEnterState(self, payload: InGameStatePayload) -> None:
        self.curLevel = payload.level
        self.player = Player(self.playerSurf, center=(self.backgroundSurf.get_width()/2, self.backgroundSurf.get_height()/2))  
        self.renderer.target = self.player


    def onExitState(self) -> None:        
        self.target = None

