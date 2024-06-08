from enum import Enum

class Colors(str, Enum):
    BACKGROUND = '#153448'
    MAIN_COLOR = '#3C5B6F'
    SECOND_COLOR = '#29485C'
    ACCENT_COLOR = '#948979'
    ACCENT_COLOR_2 = '#DFD0B8'
    RED = '#DD403A'
    RED_HOVER = '#8E3B3D'
    TEXT_COLOR = '#FFFCE8'

class Window(int, Enum):
    WIDTH = 820
    HEIGHT = 520
    SIZE_x32 = 32
    PAD_X = 10
    PAD_Y = 10

class Window_(float, Enum):
    REL_PAD_X = 0.95
    REL_PAD_Y = 0.93

class Paths(str, Enum):
    EVENTS = '\\data\\user_events.txt'
