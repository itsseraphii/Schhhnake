import sys, pygame

pygame.init()

size = (1280, 720)
aspectRatio = (16, 9)

speed = [1, 1]

black = 0, 0, 0
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
gameSurface = screen.copy()

ball = pygame.image.load("res/intro_ball.gif")
ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.display.quit()
        elif event.type == pygame.VIDEORESIZE:
            height = aspectRatio[1] * event.size[0] // aspectRatio[0]
            screen = pygame.display.set_mode((event.size[0], height), pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE)

    ballrect = ballrect.move(speed)

    if ballrect.left < 0 or ballrect.right > size[0]:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > size[1]:
        speed[1] = -speed[1]

    gameSurface.fill(black)
    gameSurface.blit(ball, ballrect)
    screen.blit(pygame.transform.scale(gameSurface, screen.get_size()), (0, 0))

    pygame.display.flip()