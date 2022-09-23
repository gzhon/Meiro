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

btnp_frame = 5

def update(self):

    self.player.update()


def draw(self):

    drawing_map(self)
    self.player.draw()


def drawing_map(self):

    global map_tips
    for i in range(MAP_HEIGHT):
        for j in range(MAP_WIDTH):
            # 得点 小(ピクセル)
            if map_tips[i][j] == 1:
                px.rect(i * TILE_SIZE + 12, j * TILE_SIZE + 10, 5, 5, 5)
            # 壁(レンガ)
            if map_tips[i][j] == 9:
                px.blt(i * TILE_SIZE, j * TILE_SIZE, 2, 96, 0, 32, 32, 0)
            # 得点 大(カボチャ)
            if map_tips[i][j] == 5:
                px.blt(i * TILE_SIZE, j * TILE_SIZE + 2, 2, 0, 0, 32, 24, 7)


def init(self):

    global map_tips

    px.load("game.pyxres")
    self.player = Player()
    map_dates = json.load(open("map_tips.json", "r"))
    map_tips = map_dates["map_tips"]
    map_tips = np.array(map_tips)
    map_tips = np.rot90(map_tips, -3)
    map_tips = np.flipud(map_tips)


class Player:
    def __init__(self) -> None:

        self.x = 15
        self.y = 15
        self.score = 0
        self.nx = self.x
        self.ny = self.y
        self.hp = PLAYER_HP
        self.is_move = True
        self.is_alive = True
        self.player_facing = 0

    def update(self) -> None:

        global map_tips
        if px.btnp(px.KEY_UP,btnp_frame,btnp_frame) or px.btnp(px.KEY_W,btnp_frame,btnp_frame):
            self.ny -= 1
            if self.can_move() == False:
                return
            self.player_facing = 3
        elif px.btnp(px.KEY_DOWN,btnp_frame,btnp_frame) or px.btnp(px.KEY_S,btnp_frame,btnp_frame):
            self.ny += 1
            if self.can_move() == False:
                return
            self.player_facing = 0
        elif px.btnp(px.KEY_LEFT,btnp_frame,btnp_frame) or px.btnp(px.KEY_A,btnp_frame,btnp_frame):
            self.nx -= 1
            if self.can_move() == False:
                return
            self.player_facing = 1
        elif px.btnp(px.KEY_RIGHT,btnp_frame,btnp_frame) or px.btnp(px.KEY_D,btnp_frame,btnp_frame):
            self.nx += 1
            if self.can_move() == False:
                return
            self.player_facing = 2
        print(self.score)

    def can_move(self):

        if map_tips[self.nx][self.ny] == 9:
            self.nx = self.x
            self.ny = self.y
            return False

        self.x = self.nx
        self.y = self.ny
        self.score += map_tips[self.x][self.y]
        map_tips[self.x][self.y] = 0
        return True

    def draw(self) -> None:

        px.blt(
            self.x * TILE_SIZE,
            self.y * TILE_SIZE,
            0,
            0,
            self.player_facing * 32,
            32,
            32,
            5,
        )
