import sys, pygame

from renderer import Renderer
from ball import Ball

pygame.init()

ball = pygame.image.load("res/intro_ball.gif")
renderer = Renderer()

all_sprites = pygame.sprite.Group()
all_sprites.add(Ball(ball))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.display.quit()
        elif event.type == pygame.VIDEORESIZE:
            renderer.resizeDisplay(event.size)

    all_sprites.update()

    renderer.render([all_sprites])