from lib.views import TiledView


class BattleView(TiledView):
    def __init__(self, screen):
        super().__init__(screen)

    def update(self):
        ...

    def render(self):
        super().render()


