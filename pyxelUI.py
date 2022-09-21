import math
import pyxel as px
from pyxelunicode import PyxelUnicode

TAIL_SPEED = 10
MISAKI_FONT_PATH = "misaki_font\misaki_gothic_2nd.ttf"

puf_m = []
font_size = []


def text(x: int, y: int, c: int, txt: str, size: int = 10, back: int = 0):

    puf_size = -1
    global font_size
    for i in range(len(font_size)):
        if font_size[i] == size:
            puf_size = i
            break
    if puf_size != -1:
        puf_m[puf_size].text(x, y, txt, c)


def font_index(size):

    puf_size = -1
    global font_size
    for i in range(len(font_size)):
        if font_size[i] == size:
            puf_size = i
            break
    return puf_size


def font_init(size: list):

    global font_size, puf_m
    puf_m = []
    for i in range(0, len(size)):
        font_size.append(size[i])
        puf_m.append(PyxelUnicode(MISAKI_FONT_PATH, original_size=size[i]))

    return puf_m


def rect(x: int, y: int, w: int, h: int, col: int = 7, back: int = 0):

    px.rect(x, y, w, h, back)
    px.rectb(x, y, w, h, col)


def roteto_x(w, r):

    x1 = w / 2 + (w) * math.cos(1.57 + r)
    return x1


def roteto_y(h, r):

    y1 = h / 2 + (h) * math.sin(1.57 + r)
    return y1

def mouse_in(ax, ay, bx, by) -> bool:

    if (
        px.mouse_x >= ax
        and px.mouse_x <= bx
        and px.mouse_y >= ay
        and px.mouse_y <= by
    ):
        return True
    return False

def mouse_rectin(ax, ay, bx, by) -> bool:

    bx = ax + bx
    by = ay + by
    print(ax,ay,bx,by)
    if (
        px.mouse_x >= ax
        and px.mouse_x <= bx
        and px.mouse_y >= ay
        and px.mouse_y <= by
    ):
        return True
    return False