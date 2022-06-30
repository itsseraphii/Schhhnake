import pygame

class Button:
    def __init__(self, x, y, size, bgColor, textColor, hoverColor, font, text):
        self.x = x
        self.y = y
        self.width = size[0]
        self.height = size[1]
        self.bgColor = bgColor
        self.textColor = textColor
        self.hoverColor = hoverColor
        self.font = font
        self.text = text

    def Draw(self, screen, mousePos):
        pygame.draw.rect(screen, self.textColor, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)
        if (self.IsMouseOver(mousePos)):
            pygame.draw.rect(screen, self.hoverColor, (self.x, self.y, self.width, self.height), 0)
        else:
            pygame.draw.rect(screen, self.bgColor, (self.x, self.y, self.width, self.height), 0)
        
        text = self.font.render(self.text, 1, self.textColor)
        screen.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def IsMouseOver(self, mousePos):
        if mousePos[0] > self.x and mousePos[0] < self.x + self.width:
            if mousePos[1] > self.y and mousePos[1] < self.y + self.height:
                return True

        return False