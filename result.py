import json
import pyxel as px
import pyxelUI as pu

json_file = open("config.json", "r")
js_config = json.load(json_file)

WIDTH = js_config["WIDTH"]
HEIGHT = js_config["HEIGHT"]

GAME_SCENE = js_config["GAME_SCENE"]

def update(self):

    pass

def draw(self):

    pass

def init(self):

    pass