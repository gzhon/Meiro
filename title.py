import json
import pyxel as px
import pyxelUI as pu

import game

json_file = open("config.json", "r")
js_config = json.load(json_file)

WIDTH = js_config["WIDTH"]
HEIGHT = js_config["HEIGHT"]

GAME_SCENE = js_config["GAME_SCENE"]
TILE_SIZE = js_config["MAP"]["tile_size"]

def update(self):

    if px.btnp(px.KEY_SPACE) or px.btnp(px.MOUSE_BUTTON_LEFT):
        game.init(self)
        self.scene = GAME_SCENE

def draw(self):

    px.blt(
        (WIDTH/2),(HEIGHT/2),0,0,0,32,32,5
    )
    px.blt(
        200,200, 2, 0, 0, 32, 24, 7
    )

def init(self):

    px.load("game.pyxres")