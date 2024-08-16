import pygame

from constants import SCREEN_SIZE


class ButtonStyle:
    DEFAULT_FONT = './res/SnakeFont.ttf'
    DEFAULT_FONT_SIZE = 12

    def __init__(self, textColor: tuple[int, int, int] = None, bgColor: tuple[int, int, int] = None, hoverColor: tuple[int, int, int] = None, font: pygame.font.Font = None):
        self.textColor = textColor if textColor != None else HONEYDEW
        self.bgColor = bgColor if bgColor != None else ZOMP
        self.hoverColor = hoverColor if hoverColor != None else EMERALD
        self.font = font if font != None else pygame.font.Font(ButtonStyle.DEFAULT_FONT, ButtonStyle.DEFAULT_FONT_SIZE)


class Button:
    def __init__(self, rectangle: pygame.Rect, text: str, clickAction: callable, style: ButtonStyle = None):
        self.rect = rectangle
        self.text = text
        self.clickAction = clickAction
        self.style = style if style != None else ButtonStyle()

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.style.textColor, self.rect)
        if (self.isMouseOver()):
            pygame.draw.rect(screen, self.style.hoverColor, self.rect.inflate(-5, -5))
        else:
            pygame.draw.rect(screen, self.style.bgColor, self.rect.inflate(-5, -5))

        text = self.style.font.render(self.text, 1, self.style.textColor)
        textRect = text.get_rect()
        textRect.center = self.rect.center
        screen.blit(text, textRect)

    def isMouseOver(self):
        return self.rect.collidepoint(self.getMousePos())

    def update(self):
        if (self.checkClicked(self.rect)):
            self.clickAction()

    def getMousePos(self) -> tuple[int, int]:
        mousePos = pygame.mouse.get_pos()
        windowSize = pygame.display.get_window_size()
        return (self.regleDeTroisLol(mousePos[0], windowSize[0], SCREEN_SIZE[0]), self.regleDeTroisLol(mousePos[1], windowSize[1], SCREEN_SIZE[1]))

    # Returns a rule of three for the mouse position
    def regleDeTroisLol(self, currentValue, currentScreenMax, rendererScreenMax) -> int:
        return currentValue*rendererScreenMax/currentScreenMax

    def checkClicked(self, rectangle: pygame.Rect):
        if rectangle.collidepoint(self.getMousePos()) and pygame.event.peek(pygame.MOUSEBUTTONDOWN):
            pygame.event.get(pygame.MOUSEBUTTONDOWN)
            return True
        return False
