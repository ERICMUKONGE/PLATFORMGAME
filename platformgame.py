import arcade
import pathlib

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE ="Arcade Platformer"

ASSETS_PATH = pathlib.path(__file__).resolve().parent.parent / "assets"

class Platerformer(arcade.window):
    def __init__(self) -> None:
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.coins = None
        self.background = None
        self.walls = None
        self.ladders = None
        self.goals = None
        self.enemies = None

        self.player = None

        self.physics_engine = None

        self.score = 0

        self.level = 1

        self.coin_sound = arcade.load_sound(
            str(ASSETS_PATH/ "sounds" / "coin.wav")
        )
        self.jump_sound = arcade.load_sound(
            str(ASSET_PATH/ "sounds" / "jump.wav")
        )
        self.victory_sound = arcade.load_sound(
            str(ASSET_PATH/ "sounds" / "victory.wav")
        )

    def setup(self):
        pass

    def on_key_press(self, key:init, modifiers: int):


    def on_update(self, delta_time: float):
        pass

    def on_draw(self):
        pass

if __name__ == "__main__":
    window = Platformer()
    windows.setup()
    arcade.run()                            