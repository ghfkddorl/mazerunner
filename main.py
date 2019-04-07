#!/usr/bin/python3

import os
import sys
MAIN_PATH = os.path.abspath(__file__)
MAIN_DIR  = os.path.dirname(MAIN_PATH)
sys.path.append(MAIN_DIR)
print("[ START PROGRAM ]")
print("start main file : "+MAIN_PATH)
print("sys append path : "+MAIN_DIR)

from gui.app import *
app = Application(MAIN_DIR)
app.mainloop()
