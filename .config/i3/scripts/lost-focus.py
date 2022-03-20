from time import sleep
from i3ipc import Connection, Event
from itertools import chain
import subprocess as proc
import fontawesome as fa
import logging
import signal
import sys
import re

i3 = Connection()

def getNotFocused():
    return [w.name for w in i3.get_workspaces() if not w.focused]

def lostFocus():
    i3.command(f"workspace {getNotFocused()[0]}")

def eventHandler(i3, e):
    lostFocus()

i3.on(Event.WINDOW_CLOSE, eventHandler)

i3.main()