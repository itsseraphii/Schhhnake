import pygame

from display import Renderer
from sprites import Player, CameraGroup

from .state import State
from .payloads import InGameStatePayload

class InGameState(State):
    def __init__(self, game, renderer: Renderer):
        super().__init__(game, renderer)

        self.backgroundSurf = pygame.image.load("res/map.png")
        self.playerSurf = pygame.image.load("res/player.png")
        self.camGroup = None


    def update(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                self.game.switchState("InGameState", InGameStatePayload(f'Niveau {self.curLevel}', self.curLevel + 1))
            if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
                self.game.switchState("MenuState")

        self.player.update()


    def draw(self) -> None:
        self.renderer.drawCameraSurface(self.backgroundSurf, (0, 0))
        self.renderer.drawCameraGroup(self.camGroup)


    def onEnterState(self, payload: InGameStatePayload) -> None:
        self.curLevel = payload.level
        self.player = Player(self.playerSurf, center=(self.backgroundSurf.get_width()/2, self.backgroundSurf.get_height()/2))  
        self.renderer.setCameraTarget(self.player)
        self.camGroup = CameraGroup(self.player)



    def onExitState(self) -> None:        
        self.renderer.setCameraTarget(None)
        self.camGroup = None
        self.player = None
        self.curLevel = 1

