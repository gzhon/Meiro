import json
import pyxel as px
import pyxelUI as pu

import game

json_file = open("config.json", "r")
js_config = json.load(json_file)

WIDTH = js_config["WIDTH"]
HEIGHT = js_config["HEIGHT"]

GAME_SCENE = js_config["GAME_SCENE"]

def update(self):

    if px.btnp(px.KEY_SPACE):
        game.init(self)
        self.scene = GAME_SCENE

def draw(self):

    pass

def init(self):

    pass