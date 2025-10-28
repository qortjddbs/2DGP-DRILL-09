from pico2d import load_image
import game_world

class Grass:
    def __init__(self, depth):
        self.image = load_image('grass.png')
        self.depth = depth

    def draw(self):
        if self.depth == 0:
            self.image.draw(400, 30)
        elif self.depth == 2:
            self.image.draw(400, 10)

    def update(self):
        pass

