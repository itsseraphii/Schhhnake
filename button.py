from pydoc import cli
import pygame

from utils import Utils

class Button:
    def __init__(self, rectangle: pygame.Rect, centerPos: tuple[int, int], bgColor: tuple[int, int, int], hoverColor: tuple[int, int, int], textColor: tuple[int, int, int], font: pygame.font.Font, text: str, clickAction):
        self.rect = rectangle
        self.rect.center = centerPos
        self.bgColor = bgColor
        self.textColor = textColor
        self.hoverColor = hoverColor
        self.font = font
        self.text = text
        self.clickAction = clickAction

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.textColor, self.rect)
        if (self.isMouseOver()):
            pygame.draw.rect(screen, self.hoverColor, self.rect.inflate(-5, -5))
        else:
            pygame.draw.rect(screen, self.bgColor, self.rect.inflate(-5, -5))
        
        text = self.font.render(self.text, 1, self.textColor)
        textRect = text.get_rect()
        textRect.center = self.rect.center
        screen.blit(text, textRect)

    def isMouseOver(self):
        return self.rect.collidepoint(Utils.getMousePos())

    def update(self):
        if (Utils.checkClicked(self.rect)):
            self.clickAction()