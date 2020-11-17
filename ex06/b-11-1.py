import pyxel
import math
import random

pyxel.init(200, 200)

balls = []
padx = 100
score = 0
failure = 0
success = 0
gameover = False

pyxel.sound(0).set(note='C3', tone='T', volume='3', effect='N', speed=30)
pyxel.sound(1).set(note='C1', tone='T', volume='3', effect='N', speed=30)


class Ball:
    speed = 1.05

    def __init__(self):
        self.x = random.randint(0, 199)
        self.y = 0
        self.angle = math.radians(random.randint(30, 150))
        self.vx = math.cos(self.angle)
        self.vy = math.sin(self.angle)

    def reset(self):
        self.x = random.randint(0, 199)
        self.y = 0
        self.angle = math.radians(random.randint(30, 150))
        self.vx = math.cos(self.angle)
        self.vy = math.sin(self.angle)

    def update(self):
        self.vx = self.vx * Ball.speed
        self.vy = self.vy * Ball.speed
        self.x += self.vx
        self.y += self.vy
        if self.x <= 0 or 200 <= self.x:
            self.vx = -self.vx


balls.append(Ball())


def update():
    global balls, padx, score, failure, success, gameover
    padx = pyxel.mouse_x

    for ball in balls:
        ball.update()

        if 195 <= ball.y:
            if padx - 20 <= ball.x <= padx + 20:
                score += 100
                pyxel.play(0, 0)
                success += 1
                if success >= 10:
                    balls.append(Ball())
                    success = 0
            else:
                pyxel.play(0, 1)
                failure += 1
                if failure > 10:
                    gameover = True
            ball.reset()


def draw():
    global balls, padx, score, failure, gameover
    pyxel.cls(7)
    if gameover:
        pyxel.text(0, 0, "GAME OVER...", 0)
    else:
        for ball in balls:
            pyxel.circ(ball.x, ball.y, 10, 6)
        pyxel.rect(padx - 20, 195, 40, 5, 14)
        pyxel.text(0, 0, str(score), 0)
        pyxel.text(150, 0, str(failure), 0)


pyxel.run(update, draw)
