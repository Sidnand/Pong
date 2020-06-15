import pyxel
from paddle import *
from ball import *

# constants

WIDTH = 250
HEIGHT = 200
TITLE = 'PONG'
COL = 7 # color white

PADDLE_MARGIN_FROM_LEFT = 10
PADDLE_WIDTH = 5
PADDLE_HEIGHT = 50
BALL_RADIUS = 2

player = Player( PADDLE_MARGIN_FROM_LEFT, HEIGHT / 2 - PADDLE_HEIGHT / 2, PADDLE_WIDTH, PADDLE_HEIGHT, COL )
ai = AI(  WIDTH - PADDLE_MARGIN_FROM_LEFT - 5, HEIGHT / 2 - PADDLE_HEIGHT / 2, PADDLE_WIDTH, PADDLE_HEIGHT, COL )
ball = Ball( WIDTH / 2 - BALL_RADIUS / 2, HEIGHT / 2 - BALL_RADIUS / 2, BALL_RADIUS, COL )

class App:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, caption=TITLE)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        ball.animate()
        player.control(pyxel.btnp, pyxel.KEY_UP, pyxel.KEY_DOWN)
        ai.control(ball.velY)
        self.checkCollision()

    def draw(self):
        pyxel.cls(0)
        player.draw(pyxel.rect)
        ai.draw(pyxel.rect)
        ball.draw(pyxel.circ)
        pyxel.text(30, 30, str(player.score), COL)
        pyxel.text(WIDTH - 30, 30, str(ai.score), COL)

    def checkCollision(self):
        # paddle collision
        if ( (ball.x - ball.r) <= (player.x + player.w) and
            (ball.y - ball.r) >= (player.y) and
            (ball.y + ball.r) <= (player.y + player.h) ):
            if ( ball.y < (player.y + player.h / 2) ):
                ball.velX *= -1
                ball.velY = 1

            elif ( ball.y >= (player.y + player.h / 2) ):
                ball.velX *= -1
                ball.velY = -1


        if ( (ball.x + ball.r) >= ai.x and
            (ball.y - ball.r) >= (ai.y) and
            (ball.y + ball.r) <= (ai.y + ai.h) ):
            if ( ball.y < (ai.y + ai.h / 2) ):
                ball.velX *= -1
                ball.velY = -1

            elif ( ball.y >= (ai.y + ai.h / 2) ):
                ball.velX *= -1
                ball.velY = 1

        # player wall collision
        if (ball.y <= 0 or
            (ball.y + ball.r) >= HEIGHT):
            ball.velY *= -1

        if (ball.x < 0): 
            ball.reset( (WIDTH, HEIGHT) )
            ai.score += 1
            ai.reset(HEIGHT)
            print(player.score)
        if (ball.x > WIDTH):
            ball.reset( (WIDTH, HEIGHT) )
            player.score += 1
            ai.reset(HEIGHT)
            print(ai.score)

App()