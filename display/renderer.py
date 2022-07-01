import pygame

class Renderer:
    ASPECT_RATIO = (16, 9)
    WIDTH = 1280
    HEIGHT = 720
    SURFACE_SIZE = WIDTH, HEIGHT
    BACKGROUND_COLOR = (0, 0, 0)


    def __init__(self) -> None:
        self.screen = pygame.display.set_mode((Renderer.WIDTH, Renderer.HEIGHT), pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE)
        self.initialScreen = self.screen.copy()


    def resizeDisplay(self, newSize: tuple[int, int]) -> None:
        height = Renderer.ASPECT_RATIO[1] * newSize[0] // Renderer.ASPECT_RATIO[0]
        self.screen = pygame.display.set_mode((newSize[0], height), pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE)


    def clear(self):
        self.initialScreen.fill(Renderer.BACKGROUND_COLOR)


    def drawSpriteGroup(self, spriteGroup: pygame.sprite.Group) -> None:
        for sprite in spriteGroup.sprites():
            offsetRec = (sprite.rect[0], sprite.rect[1])
            self.initialScreen.blit(sprite.image, offsetRec)


    def drawSurface(self, surface: pygame.Surface, position: tuple[int, int] = (0, 0)) -> None:
        self.initialScreen.blit(surface, position)


    def render(self) -> None:
        scaledScreen = pygame.transform.scale(self.initialScreen, self.screen.get_size())
        self.screen.blit(scaledScreen, (0, 0))
        pygame.display.flip()