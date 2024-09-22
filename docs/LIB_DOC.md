# How to Use lib
## Principale Structure
First of all you need to create a module in app python package like that
```cmd
MainMenuModule/
│   config.py
│   MainMenuModule.py
│   __init__.py
│
├───actions/
│       MainMenuModuleAction.py
│       __init__.py
│
└───views
        HomeView.py
        __init__.py
```

After you made this you had to modify your module config. <br/>
In ``config.py``
```python
from app.MainMenuModule import MainMenuModule
from app.MainMenuModule.views import HomeView

config = {
    MainMenuModule.__name__: MainMenuModule(),
    "views": {
        HomeView.__name__: HomeView
    }
}
```
This is an example of config. This is for the container to get instance wherever you want.

After you write your config, you have to write your module to load all datas
<br/> In ``MainMenuModuleAction`` you have:
```python
import os
from app.MainMenuModule.actions import MainMenuModuleAction
from lib import Module


class MainMenuModule(Module):
    definitions = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.py")

    def __init__(self):
        MainMenuModuleActions()

```
You can add also some params in MainMenuModuleActions. It's just an example.

These are the principal things to add in your module. After you can append optional directories.

## Optional directories
- ```views/```
- ``entity/``
- ``table/``

The ``entity/`` folder contains all the models, for example, Your pokemons will be in this folder. <br/>
The ``views/`` folder contains al views like the mainmenuview or the map. <br/>
The ``table/`` folder is only if you use a database. In this folder, there are all class that represents a table in database.