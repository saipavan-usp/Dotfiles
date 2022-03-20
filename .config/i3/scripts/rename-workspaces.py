from i3ipc import Connection, Event
from itertools import chain
import subprocess as proc
import fontawesome as fa
import logging
import signal
import sys
import re

i3 = Connection()
logging.basicConfig(level=logging.INFO)
DEFAULT_ICON = ""

wm_icons = {
    "nightly": fa.icons["firefox"],
    # "firefox": fa.icons["firefox"],
    "code": fa.icons["code"],
    "transmission-gtk": fa.icons["download"],
    "kitty": fa.icons["terminal"],
    "thunar": fa.icons["folder-open"],
    "vlc": fa.icons["film"],
    "telegramdesktop": fa.icons["telegram-plane"],
    # "discord": fa.icons["discord"],
    "google-chrome": fa.icons["chrome"],
    "qpdfview": fa.icons["file-pdf"],
}

def getFocused():
    return [w for w in i3.get_workspaces() if w.focused]

def getWindows(_id, prop):
    prop = proc.check_output(
            ['xprop', '-id', str(_id), prop], stderr=proc.DEVNULL)
    prop = prop.decode('utf-8')
    return re.findall('"([^"]*)"', prop)

def constructIcons(names):
    icons = ""
    for i in names:
        if i in wm_icons.keys():
            icons += wm_icons[i] + " "
        elif i in fa.icons:
            icons += fa.icons[i] + " "
        # else:
        #     icons += DEFAULT_ICON + "  "
    icons = icons.strip()
    if len(icons) > 1:
        return "( " + icons + " )"
    return icons


def renameIcons():
    for i in i3.get_tree().workspaces():
        names = [set(str(w).lower() for w in getWindows(j.window, "WM_CLASS")) for j in i.leaves()]
        names = set(chain.from_iterable(names))
        names =  constructIcons(names)
        logging.info(f'rename workspace "{i.name}" to "{names}"')
        i3.command(f'rename workspace "{i.name}" to "{names}"')

def eventHandler(i3, e):
    renameIcons()

def resetIcons(signum, frame):
    for i in i3.get_workspaces():
        logging.info(f'rename workspace "{i.name}" to "{i.num}"')
        i3.command(f'rename workspace "{i.name}" to "{i.num}"')
    i3.main_quit()
    sys.exit(0)

renameIcons()

signal.signal(signal.SIGINT, resetIcons)

i3.on(Event.WINDOW_MOVE, eventHandler)
i3.on(Event.WINDOW_NEW, eventHandler)
i3.on(Event.WINDOW_CLOSE, eventHandler)

i3.main()