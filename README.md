![License](https://img.shields.io/badge/license-MIT-green)
![Python Version](https://img.shields.io/badge/python_>%3D-3.6-green) ![PyPi](https://warehouse-camo.ingress.cmh1.psfhosted.org/cd7ef4975d71b4a87a35b3c01b5b1ec8481c4549/68747470733a2f2f696d672e736869656c64732e696f2f707970692f762f7069702e737667)

* ### Info
    This is simple Langton's ant simulation written by TheAmmiR and IceFox-L.
* ### Rules
    There is a grid. Each cell of The Grid can be filled in any color.
    The Grid is populated by ant. Ant is implemented as one cell of The Grid.
    Each move the ant fills the cell he's standing on with next declared color and turns left or right.
    If cell is filled with last set color, the ant fills it with default one.
* ### Running
    * First, you have to open `colors_config.txt` and fill it. The template is already in the file - it looks like
        ```fix
        COLOR - DIRECTION
        COLOR - DIRECTION
        COLOR
        COLOR
        ```
        If you do not set the direction, it is choosing randomly before starting each game.
        You can see list of possible colors in `colorreader.py`
        ___
    * Open `ants.py`. You can see some variables named in UPPER_SNAKE_CASE. You can freely edit it.
        ___
    * Run `ants.py`
