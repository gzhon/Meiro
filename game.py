import json
import time
import math
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
scene_sec = 0
play_time = ""
start_time = 0
finsh_time = 0

scene_frame_count = 0


def update(self):

    global scene_frame_count, is_start, scene_sec, start_time
    scene_frame_count += 1
    scene_sec = scene_frame_count // 30
    if scene_sec >= 3:
        if is_finsh == False:
            is_start = True
            self.player.update()
            for i in range(len(enemy_obj)):
                enemy_obj[i].update()
    if is_finsh == True or is_game_over == True:
        if px.btnp(px.KEY_SPACE):
            self.scene = TITLE_SCENE
    if scene_sec == 4:
        start_time = time.perf_counter()


def draw(self):

    drawing_map(self)
    if is_start == False:
        pu.rect(
            MAP_WIDTH / 2 * TILE_SIZE - 30,
            MAP_HEIGHT / 2 * TILE_SIZE - 20,
            80,
            100,
        )
        pu.text(
            MAP_WIDTH / 2 * TILE_SIZE,
            MAP_HEIGHT / 2 * TILE_SIZE,
            7,
            str(3 - scene_frame_count // 30),
            64,
        )
    if scene_sec == 3:
        pu.rect(
            MAP_WIDTH / 2 * TILE_SIZE - 120,
            MAP_HEIGHT / 2 * TILE_SIZE - 20,
            220,
            100,
        )
        pu.text(
            MAP_WIDTH / 2 * TILE_SIZE - 100,
            MAP_HEIGHT / 2 * TILE_SIZE,
            7,
            "Start!",
            64,
        )
    if scene_sec <= 2:
        pu.text(
            WIDTH - 170,
            HEIGHT / 2 + 40,
            7,
            "Time:0:00",
            32,
        )
    else:
        if is_finsh == False:
            now_time = str(time_to_ms(scene_sec - 3))
        else:
            now_time = play_time
        pu.text(
            WIDTH - 170,
            HEIGHT / 2 + 40,
            7,
            "Time:" + now_time,
            32,
        )
    if is_finsh == True:
        if is_game_over == False:
            pu.rect(
                MAP_WIDTH / 2 * TILE_SIZE - 140,
                MAP_HEIGHT / 2 * TILE_SIZE - 100,
                320,
                220,
            )
            pu.text(
                MAP_WIDTH / 2 * TILE_SIZE - 60,
                MAP_HEIGHT / 2 * TILE_SIZE - 60,
                7,
                "Finsh!",
                64,
            )
            pu.text(
                MAP_WIDTH / 2 * TILE_SIZE - 100,
                MAP_HEIGHT / 2 * TILE_SIZE + 60,
                7,
                "Finsh Time:" + play_time,
                32,
            )
        else:
            pu.rect(
                MAP_WIDTH / 2 * TILE_SIZE - 100,
                MAP_HEIGHT / 2 * TILE_SIZE - 100,
                320,
                200,
            )
            pu.text(
                MAP_WIDTH / 2 * TILE_SIZE - 80,
                MAP_HEIGHT / 2 * TILE_SIZE - 65,
                7,
                "Game Over",
                64,
            )
    pu.text(
        WIDTH - 170,
        HEIGHT / 2,
        7,
        "Score:" + str(self.player.score).zfill(3),
        32,
    )
    self.player.draw()
    for i in range(len(enemy_obj)):
        enemy_obj[i].draw()


def drawing_map(self):

    global map_tips, is_start
    for i in range(MAP_HEIGHT):
        for j in range(MAP_WIDTH):
            # 得点 小(ピクセル)
            if map_tips[i][j] == 1:
                px.rect(i * TILE_SIZE + 12, j * TILE_SIZE + 10, 5, 5, 5)
            # スタート地点
            if map_tips[i][j] == 6:
                px.rect(i * TILE_SIZE, j * TILE_SIZE, TILE_SIZE, TILE_SIZE, 10)
            # ゴール地点
            if map_tips[i][j] == 7:
                px.rect(i * TILE_SIZE, j * TILE_SIZE, TILE_SIZE, TILE_SIZE, 8)
            # 壁(レンガ)
            if map_tips[i][j] == 9:
                px.blt(i * TILE_SIZE, j * TILE_SIZE, 2, 96, 0, 32, 32, 0)
            # 得点 大(カボチャ)
            if map_tips[i][j] == 5:
                px.blt(i * TILE_SIZE, j * TILE_SIZE + 2, 2, 0, 0, 32, 24, 7)
            # クリスタル
            if map_tips[i][j] == 8:
                px.blt(i * TILE_SIZE, j * TILE_SIZE, 2, 96, 32, 32, 32, 0)


def get_play_time(start, end):

    run_time = math.floor(end - start)
    m = run_time // 60
    s = run_time % 60
    return f"{m:-01}:{s:-02}"


def time_to_ms(time):

    m = time // 60
    s = time % 60
    return f"{m:-01}:{s:-02}"


def init(self):

    global map_tips, is_start, is_finsh, enemy_obj, is_game_over
    global scene_sec,play_time,start_time,finsh_time,scene_frame_count

    is_start = False
    is_finsh = False
    is_game_over = False
    px.load("game.pyxres")
    scene_sec = 0
    play_time = ""
    start_time = 0
    finsh_time = 0
    scene_frame_count = 0
    self.player = Player()
    map_dates = json.load(open("map_tips.json", "r"))
    map_tips = map_dates["map_tips"]
    map_tips = np.array(map_tips)
    map_tips = np.rot90(map_tips, -3)
    map_tips = np.flipud(map_tips)
    enemy_obj = []
    enemt_pos = [[1, 1], [23, 1]]
    for i in range(len(enemt_pos)):
        enemy_obj.append(Enemy(enemt_pos[i][0], enemt_pos[i][1]))


class Player:
    def __init__(self) -> None:
        self.x = 12
        self.y = 24
        self.score = 0
        self.nx = self.x
        self.ny = self.y
        self.hp = PLAYER_HP
        self.player_facing = 3

    def update(self) -> None:

        global map_tips
        if px.btnp(px.KEY_UP, btnp_frame, btnp_frame) or px.btnp(
            px.KEY_W, btnp_frame, btnp_frame
        ):
            self.ny -= 1
            if self.can_move() == False:
                return
            self.player_facing = 3
        elif px.btnp(px.KEY_DOWN, btnp_frame, btnp_frame) or px.btnp(
            px.KEY_S, btnp_frame, btnp_frame
        ):
            self.ny += 1
            if self.can_move() == False:
                return
            self.player_facing = 0
        elif px.btnp(px.KEY_LEFT, btnp_frame, btnp_frame) or px.btnp(
            px.KEY_A, btnp_frame, btnp_frame
        ):
            self.nx -= 1
            if self.can_move() == False:
                return
            self.player_facing = 1
        elif px.btnp(px.KEY_RIGHT, btnp_frame, btnp_frame) or px.btnp(
            px.KEY_D, btnp_frame, btnp_frame
        ):
            self.nx += 1
            if self.can_move() == False:
                return
            self.player_facing = 2

    def can_move(self):

        global is_finsh, finsh_time, play_time, is_game_over
        if self.nx >= MAP_WIDTH or self.ny >= MAP_HEIGHT:
            self.nx = self.x
            self.ny = self.y
            return False

        # 壁
        if map_tips[self.nx][self.ny] == 9:
            self.nx = self.x
            self.ny = self.y
            return False

        # ゴール地点
        if map_tips[self.nx][self.ny] == 7:
            finsh_time = time.perf_counter()
            play_time = get_play_time(start_time, finsh_time)
            is_finsh = True

        # 敵に捕まる
        for i in range(len(enemy_obj)):
            ex = enemy_obj[i].x
            ey = enemy_obj[i].y
            if ex == self.nx and ey == self.ny:
                finsh_time = time.perf_counter()
                play_time = get_play_time(start_time, finsh_time)
                is_finsh = True
                is_game_over = True

        self.x = self.nx
        self.y = self.ny
        if map_tips[self.x][self.y] == 1:
            self.score += 1
        if map_tips[self.x][self.y] == 5:
            self.score += 5
        if map_tips[self.x][self.y] == 8:
            self.score += 50
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


class Enemy:
    def __init__(self, x, y) -> None:

        self.x = x
        self.y = y
        self.player_facing = 0

    def update(self):

        pass

    def draw(self):

        px.blt(
            self.x * TILE_SIZE,
            self.y * TILE_SIZE,
            1,
            0,
            self.player_facing * 32,
            32,
            32,
            1,
        )
