import pygame
from menus import Button
from constants import EMERALD, GREEN_COLOR, HONEYDEW, ZOMP

from display import Renderer

from .payloads import InGameStatePayload
from .state import State

class MenuState (State): 
    def __init__(self, game, renderer: Renderer):
        super().__init__(game, renderer)
        self.surf = pygame.Surface(Renderer.SURFACE_SIZE)
        self.bigSnakeFont = pygame.font.Font('./res/SnakeFont.ttf', 72)
        self.smolSnakeFont = pygame.font.Font('./res/SnakeFont.ttf', 24)
        self.extraSmolSnakeFont = pygame.font.Font('./res/SnakeFont.ttf', 12)
        playButtonRect = pygame.Rect(0, 0, 150, 50)
        playButtonRect.center = (Renderer.WIDTH/2, Renderer.HEIGHT/2 + 150)
        self.playButton = Button(playButtonRect, "press to start", self.menuAction)

    def draw(self) -> None:
        self.playButton.draw(self.surf)
        self.surf.blit(self.bigSnakeFont.render("Schhhnake", True, GREEN_COLOR), (150, 150))
        self.surf.blit(self.smolSnakeFont.render("A game where a snake eats balls", True, GREEN_COLOR), (150, 350))
        self.surf.blit(self.smolSnakeFont.render("Centering text is hard", True, GREEN_COLOR), (Renderer.WIDTH-450, Renderer.HEIGHT-250))
        self.renderer.drawSurface(self.surf)


    def update(self) -> None:
        self.playButton.update()


    def menuAction(self) -> None:
        self.game.switchState("InGameState", InGameStatePayload(17, 17, 1, 8, 2))
        
