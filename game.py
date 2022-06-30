import pygame
from constants import TARGET_FPS

from renderer import Renderer
from states.gameState import GameState
from states.menuState import MenuState

class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()

        self.renderer = Renderer()

        self.dicStates = {
            "game": GameState(self, self.renderer),
            "menu": MenuState(self, self.renderer)
        }
        self.curState = "menu"

        self.clock = pygame.time.Clock()


    def gameLoop(self) -> None:
        while True:
            self.renderer.clear()

            self.dicStates[self.curState].update()
            self.dicStates[self.curState].draw()

            self.renderer.render()
            self.clock.tick(TARGET_FPS)


    def switchState(self, newState: str) -> None:
        self.dicStates[self.curState].onExitState()
        self.curState = newState
        self.dicStates[self.curState].onEnterState()
        print(self.curState)


if __name__ == "__main__":
    Game().gameLoop()
