import os
from pathlib import Path

from app import Game
from app.MainMenuModule import MainMenuModule
from app.Settings import Settings


def main() -> int:
    g = Game(os.path.join(Path(os.path.dirname(__file__)).parent.parent, "config", "config.py"))
    g.add_module(MainMenuModule)
    g.add_module(Settings)
    g.run()
    return 0


if __name__ == "__main__":
    main()
