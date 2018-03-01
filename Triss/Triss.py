#!/usr/bin/env python3

import curses
import curses.textpad
import time
import os
import locale
from . import config as tc
import subprocess
from curses import wrapper

locale.setlocale(locale.LC_ALL, '')
code = locale.getpreferredencoding()
cmds = os.listdir(tc.PATH_TO_SCRIPTS)
icmd = -404


def main(stdscr):
	curses.noecho()
	curses.curs_set(0)  # отключение курсора
	height, width = stdscr.getmaxyx()
	startCMD = 0  # порядковый номер команды, первой отображаемой на экр.
	ncmd = min(8, height - 4)  # количество отображаемых команд

	def debug():
		'''Для отладки'''
		# stdscr.addstr(height - 1, 0, "w = %d, h = % d".encode(code) % (width, height))

	def draw():
		'''Отрисовка меню'''
		stdscr.clear()
		debug()
		stdscr.addstr(0, 0, "Hello. I'm Triss and I will help you. What do you want?".encode(code))
		stdscr.addstr(height - 3, 0, "%d-%d from %d" % (startCMD, min(startCMD + ncmd, len(cmds)), len(cmds)))
		for i in range(startCMD, min(len(cmds), startCMD + ncmd)):
			stdscr.addstr(i - startCMD + 2, 0, ('%d) %s' % (i - startCMD, cmds[i])).encode(code))
		stdscr.refresh()

	def handler():
		'''Обработчик событий'''
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
	wrapper(main)

	if icmd != -404:
		cmd = str(tc.PATH_TO_SCRIPTS + cmds[icmd])
		subprocess.call(cmd)
