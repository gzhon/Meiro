import json
import numpy as np
import pyxel as px
import pyxelUI as pu

json_file = open("config.json", "r")
js_config = json.load(json_file)

WIDTH = js_config["WIDTH"]
HEIGHT = js_config["HEIGHT"]

TITLE_SCENE = js_config["TITLE_SCENE"]

MAP_WIDTH = js_config["MAP"]["WIDTH"]
MAP_HEIGHT = js_config["MAP"]["HEIGHT"]
TILE_SIZE = js_config["MAP"]["tile_size"]

PLAYER_HP = js_config["PLAYER"]["hp"]
PLAYER_DISTANCE = js_config["PLAYER"]["moving_distance"]


def update(self):

    self.player.update()


def draw(self):

    drawing_map(self)
    self.player.draw()


def drawing_map(self):

    for i in range(MAP_HEIGHT):
        for j in range(MAP_WIDTH):
            pu.rect(i * TILE_SIZE, j * TILE_SIZE, TILE_SIZE, TILE_SIZE, 7, 0)


def init(self):

    px.load("game.pyxres")
    self.player = Player()
    self.map_date = js_config["map_tips"]
    self.map_tips = np.zeros((MAP_WIDTH,MAP_HEIGHT))


class Player:
    def __init__(self) -> None:

        self.x = TILE_SIZE*15
        self.y = TILE_SIZE*15
        self.dx = 0
        self.dy = 0
        self.hp = PLAYER_HP
        self.is_alive = True
        self.is_walking = 0
        self.moveing_num = 0
        self.player_facing = 0
        self.moving_distance = PLAYER_DISTANCE

    def update(self) -> None:

        if px.btn(px.KEY_UP) or px.btnp(px.KEY_W):
            self.y -= self.moving_distance
            self.player_facing = 3
        elif px.btn(px.KEY_DOWN) or px.btnp(px.KEY_S):
            self.player_facing = 0
            self.y += self.moving_distance
        elif px.btn(px.KEY_LEFT) or px.btnp(px.KEY_A):
            self.player_facing = 1
            self.x -= self.moving_distance
        elif px.btn(px.KEY_RIGHT) or px.btnp(px.KEY_D):
            self.player_facing = 2
            self.x += self.moving_distance

    def draw(self) -> None:

        px.blt(self.x, self.y, 0, 0, self.player_facing * 32, 32, 32, 5)
