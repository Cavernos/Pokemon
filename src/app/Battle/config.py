from app.Battle import Battle
from app.Battle.views.BattleView import BattleView

config = {
    Battle.__name__: Battle(),
    "views": {
        BattleView.__name__: BattleView

    },
}