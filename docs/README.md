# 🔴 Pokémon RPG ⚪
## Folders & Files
Folders and files names in snake_case.
```
/Pokemon
    ∟ /config
        ∟ config.py
    ∟ /docs
        ∟ README.md
        ∟ issues.md
    ∟ /src
        ∟ /tests
            ∟ /lib
            ∟ /app
        ∟ /lib
            ∟ /utilities
            ∟ /helpers
        ∟ /app
            ∟ /assets
                ∟ /images
            ∟ /modules
            ∟ main.py
            
```

## Code
### Variables
Variables names in snake_case and the type.
```python
my_string: str = ''
my_integer: int = 0
my_float: float = 0.0
my_list: list = []
my_dict: dict = {}
my_set: set = {}
```
### Functions
Functions names in snake_case, docstring and what they return.
```python
def countdown(number: int) -> None:
    """
        Description: Simple countdown from number to 0.
        Atributs:
            number: int: Counter start number.
    """
    for i in range(number+1):
        print(number - i)
```
### Class
Functions names in PascalCase and docstring.
```python
class Player():
    """
        Description: Object that represents the player.
    """
    def __init__(self) -> None:
        pass
```