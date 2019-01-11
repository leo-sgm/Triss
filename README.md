# Triss
Alpha version of assistant. For quick access to scripts and etc. 


## Install & Usage:
```
git clone https://github.com/leo-sgm/Triss.git
cd Triss
pip install -e --user .
```

or (work now)
```
pip install -e .
```

> not work now:

or ```pip install --user .``` and etc...

edit config.py to provide path to your scripts

### Note: 
Add  `$HOME/.local/bin` to __$PATH__

---

> The Windows version of Python doesn’t include the curses module. A ported version called UniCurses is available. You could also try the Console module written by Fredrik Lundh, which doesn’t use the same API as curses but provides cursor-addressable text output and full support for mouse and keyboard input.

But try (seems to work):
```
pip install windows-curses
```
