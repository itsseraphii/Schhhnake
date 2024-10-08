from math import floor

import numpy
import pygame
import pygame_menu

from constants import BLACK, EMERALD, GREEN_COLOR, SCREEN_SIZE
from utils import resource_path

from .payloads import InGameStatePayload
from .state import State


class MenuState (State):

    def __init__(self, game):
        super().__init__(game)

        width, height = SCREEN_SIZE
        self.surf = pygame.Surface(SCREEN_SIZE)
        self.cool_snake = pygame.image.load(resource_path('./res/shnake.png'))
        self.bigSnakeFont = pygame.font.Font(resource_path('./res/SnakeFont.ttf'), 72)
        self.smolSnakeFont = pygame.font.Font(resource_path('./res/SnakeFont.ttf'), 24)
        self.rows = 17
        self.columns = 17
        self.appleSpawn = 1
        self.delay = 6

        self.setupMenu()

    def draw(self, screen) -> None:
        width, height = SCREEN_SIZE

        self.menu.draw(self.surf)
        self.surf.blit(self.bigSnakeFont.render(
            "Schhhnake", True, GREEN_COLOR), (150, 50))
        self.surf.blit(self.smolSnakeFont.render(
            "A game where a snake eats balls", True, GREEN_COLOR), (150, 125))
        self.surf.blit(self.smolSnakeFont.render("Centering text is hard",
                       True, GREEN_COLOR), (width-450, height-50))

        for i in range(5):
            leftScreenPosition = numpy.random.randint(
                1, width//2 - 300)
            rightScreenPosition = numpy.random.randint(
                width//2 + 200, width - 100)

            self.surf.blit(self.cool_snake, (leftScreenPosition,
                           numpy.random.randint(0, height - 100)))

            self.surf.blit(self.cool_snake, (rightScreenPosition,
                           numpy.random.randint(0, height - 100)))

        screen.blit(self.surf, (0, 0))

    def update(self) -> None:
        self.menu.update(self.game.events)

    def menuAction(self) -> None:
        self.game.switchState(
            "InGameState", InGameStatePayload(self.rows, self.columns, self.appleSpawn, self.delay, 2))

    def setupMenu(self) -> None:
        width, height = SCREEN_SIZE

        cool_theme = pygame_menu.themes.THEME_GREEN.copy()  # type: ignore
        cool_theme.background_color = BLACK
        cool_theme.widget_font = self.bigSnakeFont
        cool_theme.widget_font_color = EMERALD
        cool_theme.selection_color = GREEN_COLOR
        cool_theme.widget_offset = (0, 200)

        self.menu = pygame_menu.Menu(
            '', width, height, theme=cool_theme, center_content=False)
        self.menu.get_menubar().hide()

        self.menu.add.button('Play', self.menuAction)
        self.menu.add.range_slider(
            'Row', default=17, range_values=(5, 25), increment=1, onchange=self.setRow, range_text_value_enabled=False)
        self.menu.add.range_slider(
            'Column', default=17, range_values=(5, 25), increment=1, onchange=self.setColumn, range_text_value_enabled=False)
        self.menu.add.range_slider(
            'Nb Apple', default=1, range_values=(0, 25), increment=1, onchange=self.setAppleSpawn, range_text_value_enabled=False)
        self.menu.add.range_slider(
            'Delay', default=6, range_values=(6, 12), increment=1, onchange=self.setDelay, range_text_value_enabled=False)
        self.menu.add.button('Quit', pygame_menu.events.EXIT)  # type: ignore

    def setRow(self, value: int) -> None:
        self.rows = floor(value)

    def setColumn(self, value: int) -> None:
        self.columns = floor(value)

    def setAppleSpawn(self, value: int) -> None:
        self.appleSpawn = floor(value)

    def setDelay(self, value: int) -> None:
        self.delay = floor(value)
