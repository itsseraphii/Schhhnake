from renderer import Renderer

class State:
    def __init__(self, game, renderer: Renderer):
        self.renderer = renderer
        self.game = game

    def update(self):
        pass


    def render(self):
        pass


    def onExitState(self):
        pass


    def onEnterState(self):
        pass