class Ball:
    def __init__(self, x, y, r, col):
        self.x = x
        self.y = y
        self.r = r
        self.col = col
        self.velX = -2
        self.velY = 0

    def draw(self, circ):
        circ(self.x, self.y, self.r, self.col)

    def animate(self):
        self.x += self.velX
        self.y += self.velY

    def reset(self, center):
        self.x = center[0] / 2 - self.r / 2
        self.y = center[1] / 2 - self.r / 2
        self.velY = 0
        self.velX *= -1