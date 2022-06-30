import sys, pygame
from constants import TARGET_FPS

from renderer import Renderer
from ball import Ball

pygame.init()

ball = pygame.image.load("res/intro_ball.gif")
renderer = Renderer()

clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
all_sprites.add(Ball(ball))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.display.quit()
        elif event.type == pygame.VIDEORESIZE:
            renderer.resizeDisplay(event.size)

    renderer.clear()

    all_sprites.update()
    renderer.drawSpriteGroup(all_sprites)

    renderer.render()
    
    clock.tick(TARGET_FPS)
