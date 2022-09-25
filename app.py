import json
import pyxel as px
import pyxelUI as pu

import game
import title
import result

json_file = open("config.json", "r")
js_config = json.load(json_file)

WIDTH = js_config["WIDTH"]
HEIGHT = js_config["HEIGHT"]

TITLE_SCENE = js_config["TITLE_SCENE"]
GAME_SCENE = js_config["GAME_SCENE"]
RESULT_SCENE = js_config["RESULT_SCENE"]

font_size = []

class App:
    def __init__(self):

        font_size = [8, 10, 12, 14, 16, 18, 20, 24, 32, 48, 64]

        self.font = pu.font_init(font_size)
        self.scene = TITLE_SCENE
        self.mode=0

        px.init(WIDTH, HEIGHT,fps=30)
        px.mouse(True)
        title.init(self=self)
        px.run(self.update, self.draw)

    def update(self):

        if self.scene == TITLE_SCENE:
            title.update(self=self)
        if self.scene == GAME_SCENE:
            game.update(self=self)
        if self.scene == RESULT_SCENE:
            result.update(self=self)

    def draw(self):

        px.cls(0)
        if self.scene == TITLE_SCENE:
            title.draw(self=self)
        if self.scene == GAME_SCENE:
            game.draw(self=self)
        if self.scene == RESULT_SCENE:
            result.draw(self=self)

App()
