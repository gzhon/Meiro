import json
from turtle import down
import pyxel as px
import pyxelUI as pu

json_file = open("config.json", "r")
js_config = json.load(json_file)

WIDTH = js_config["WIDTH"]
HEIGHT = js_config["HEIGHT"]

TITLE_SCENE = js_config["TITLE_SCENE"]

PLAYER_HP = js_config["PLAYER"]["hp"]
PLAYER_DISTANCE = js_config["PLAYER"]["moving_distance"]

def update(self):

    self.player.update()

def draw(self):

    self.player.draw()

def init(self):

    px.load("game.pyxres")
    self.player = Player()
    self.map_date = js_config["Map_Date"]

class Player:

    def __init__(self) -> None:

        self.x = WIDTH/2
        self.y = HEIGHT/2
        self.hp = PLAYER_HP
        self.is_alive = True
        self.is_walking = False
        self.player_facing = 0
        self.moving_distance = PLAYER_DISTANCE

    def update(self) -> None:

        if px.btnp(px.KEY_UP) or px.btnp(px.KEY_W):
            self.player_facing = 3
        elif px.btnp(px.KEY_DOWN) or px.btnp(px.KEY_S):
            self.player_facing = 0
        elif px.btnp(px.KEY_LEFT) or px.btnp(px.KEY_A):
            self.player_facing = 1
        elif px.btnp(px.KEY_RIGHT) or px.btnp(px.KEY_D):
            self.player_facing = 2
        print(self.player_facing)

    def draw(self) -> None:

        px.blt(
            self.x,self.y,0,0,self.player_facing*32,32,32,0
        )