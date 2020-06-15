class Paddle:
    def __init__(self, x, y, w, h, col):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.col = col
        self.score = 0

    def draw(self, rect):
        rect(self.x, self.y, self.w, self.h, self.col)

    def control(self):
        pass

class Player(Paddle):
    def __init__(self, x, y, w, h, col):
        Paddle.__init__(self, x, y, w, h, col)

    def control(self, btnp, KEY_UP, KEY_DOWN):
        if (btnp(KEY_UP, 1, 1)):
            self.y -= 1

        if (btnp(KEY_DOWN, 1, 1)):
            self.y += 1

class AI(Paddle):
    def __init__(self, x, y, w, h, col):
        Paddle.__init__(self, x, y, w, h, col)

    def control(self, ballVel):
        self.y += ballVel

    def reset(self, height):
        self.y = height / 2 - self.h / 2