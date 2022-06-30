import pygame
from button import Button
from constants import GREEN_COLOR

from renderer import Renderer

class Menu: 
    def __init__(self) -> None:
        self.surf = pygame.Surface(Renderer.SURFACE_SIZE)
        self.bigSnakeFont = pygame.font.Font('./res/SnakeFont.ttf', 72)
        self.smolSnakeFont = pygame.font.Font('./res/SnakeFont.ttf', 24)
        self.extraSmolSnakeFont = pygame.font.Font('./res/SnakeFont.ttf', 12)
        self.playButton = Button(Renderer.WIDTH /2 - 75, Renderer.HEIGHT / 2 + 150, (150, 50), (255,0,0), (0,255,0), (0,0,255), self.extraSmolSnakeFont, "press to start")

    def drawSurface(self) -> pygame.Surface:
        self.playButton.Draw(self.surf, Utils.getMousePos())
        self.surf.blit(self.bigSnakeFont.render("Schhhnake", True, GREEN_COLOR), (150, 150))
        self.surf.blit(self.smolSnakeFont.render("A game where a snake eats balls", True, GREEN_COLOR), (150, 350))
        self.surf.blit(self.smolSnakeFont.render("Centering text is hard", True, GREEN_COLOR), (Renderer.WIDTH-450, Renderer.HEIGHT-250))
        return self.surf

class Utils:
    def getMousePos():
        mousePos = pygame.mouse.get_pos()
        windowSize = pygame.display.get_window_size()
        print(windowSize)

        return (Utils.regleDeTroisLol(mousePos[0], windowSize[0], Renderer.WIDTH), Utils.regleDeTroisLol(mousePos[1], windowSize[1], Renderer.HEIGHT))

    def regleDeTroisLol(currentValue, currentScreenMax, rendererScreenMax):
        return currentValue*currentScreenMax/rendererScreenMax
