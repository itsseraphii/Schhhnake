import pygame
from display import Renderer

class Ball(pygame.sprite.Sprite):
    def __init__(self, image: pygame.Surface):
       pygame.sprite.Sprite.__init__(self)

       self.image = image
       self.rect = self.image.get_rect()
       self.rect.x += 0
       self.rect.y += 0
       self.speed = [5, 5]


    def update(self):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]

        if self.rect.left < 0 or self.rect.right > Renderer.WIDTH:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > Renderer.HEIGHT:
            self.speed[1] = -self.speed[1]