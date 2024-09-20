from app.MainMenuModule import MainMenuModule
from app.MainMenuModule.views import HomeView

config = {
    MainMenuModule.__name__: MainMenuModule(),
    "views": {
        HomeView.__name__: HomeView
    }
}