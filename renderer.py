import pygame

class Renderer:
    ASPECT_RATIO = (16, 9)
    WIDTH = 1280
    HEIGHT = 720
    BACKGROUND_COLOR = (0, 0, 0)


    def __init__(self) -> None:
        self.screen = pygame.display.set_mode((Renderer.WIDTH, Renderer.HEIGHT), pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE)
        self.gameSurface = self.screen.copy()


    def resizeDisplay(self, newSize: tuple[int, int]) -> None:
        height = Renderer.ASPECT_RATIO[1] * newSize[0] // Renderer.ASPECT_RATIO[0]
        self.screen = pygame.display.set_mode((newSize[0], height), pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE)


    def render(self, spriteGroup: pygame.sprite.Group) -> None:
        self.gameSurface.fill(Renderer.BACKGROUND_COLOR)

        for sprite in spriteGroup.sprites():
            offsetRec = (sprite.rect[0], sprite.rect[1])
            self.gameSurface.blit(sprite.image, offsetRec)

        scaledGameSurface = pygame.transform.scale(self.gameSurface, self.screen.get_size())
        self.screen.blit(scaledGameSurface, (0, 0))
        pygame.display.flip()