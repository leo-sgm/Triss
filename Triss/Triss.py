#!/usr/bin/env python3

import curses
import curses.textpad
import locale
import os
import subprocess
import time
from curses import wrapper

# from . import config as tc
from Triss.config import PATH_TO_SCRIPTS
from Triss.config import BaseConfig

from Triss.helper import list_available_commands

locale.setlocale(locale.LC_ALL, '')
code = locale.getpreferredencoding()
cmds = list_available_commands(PATH_TO_SCRIPTS)
icmd = -404


def main(stdscr, config=BaseConfig()):
    curses.noecho()
    curses.curs_set(0)  # turn of the cursor
    height, width = stdscr.getmaxyx()
    startCMD = 0  # the seq. num. of the 1st command displayed on the screen
    ncmd = min(8, height - 4)  # number of commands displayed

    def debug():
        '''Debug output at scr'''
        # stdscr.addstr(height - 1, 0, "w = %d, h = % d".encode(code) % (width, height))

    def draw():
        '''Drawing menu and main screen'''
        stdscr.clear()
        debug()
        stdscr.addstr(0, 0, "Hello. I'm Triss and I will help you. What do you want?".encode(code))
        stdscr.addstr(height - 3, 0, "%d-%d from %d" % (startCMD, min(startCMD + ncmd, len(cmds)), len(cmds)))
        for i in range(startCMD, min(len(cmds), startCMD + ncmd)):
            stdscr.addstr(i - startCMD + 2, 0, ('%d) %s' % (i - startCMD, cmds[i])).encode(code))
        stdscr.refresh()

    def handler():
        '''Обработчик событий | Handler of actions'''
        nonlocal startCMD
        global icmd
        while True:
            time.sleep(0.1)
            draw()
            key = stdscr.getkey()
            # stdscr.addstr(height - 2, 0, "Pressed key: ".encode(code) + str(key).encode(code))
            if key == 'q':
                return
            elif key == 'a':
                2 + 2
            elif key == 'KEY_RIGHT' or 'r' == key:
                startCMD += ncmd if startCMD + ncmd < len(cmds) else 0
            elif key == 'KEY_LEFT' or 'l' == key:
                startCMD -= ncmd if startCMD - ncmd >= 0 else 0
            for i in range(len(cmds)):
                if str(i - startCMD) == key and (i - startCMD) < ncmd:
                    stdscr.refresh()
                    icmd = i
                    curses.endwin()
                    return

    draw()
    handler()


def run():
    config = BaseConfig()
    wrapper(main, config)

    if icmd != -404:
        cmd = str(PATH_TO_SCRIPTS + cmds[icmd])
        subprocess.call(cmd)
