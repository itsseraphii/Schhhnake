import pygame
from constants import TARGET_FPS

from renderer import Renderer
from states.gameState import GameState
from states.menuState import MenuState

class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()

        renderer = Renderer()

        self.dicStates = {
            "game": GameState(self, renderer),
            "menu": MenuState(self, renderer)
        }
        self.curState = "menu"

        self.clock = pygame.time.Clock()

    def gameLoop(self):
        while True:
            self.dicStates[self.curState].update()
            self.dicStates[self.curState].render()
            self.clock.tick(TARGET_FPS)


    def switchState(self, newState: str):
        self.dicStates[self.curState].onExitState()
        self.curState = newState
        self.dicStates[self.curState].onEnterState()


if __name__ == "__main__":
    Game().gameLoop()
