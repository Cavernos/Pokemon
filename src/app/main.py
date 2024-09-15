import os.path
from pathlib import Path

from app import Game
from app.module import ModuleClass


def main() -> int:
    g = Game(os.path.join(Path(os.path.dirname(__file__)).parent.parent, "config", "config.py")).add_module(ModuleClass)
    # LoaderFactory()()
    g.run("")
    return 0


if __name__ == "__main__":
    main()
