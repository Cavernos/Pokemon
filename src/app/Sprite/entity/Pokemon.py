from app.Sprite.entity import Entity


class Pokemon(Entity):
    def __init__(self, x, y, name, *groups):
        super().__init__(x, y, name, *groups)
