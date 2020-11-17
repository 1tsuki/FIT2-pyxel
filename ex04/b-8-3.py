import pyxel
import math

pyxel.init(200,200)

ballx = 100
bally = 0
angle = math.radians(30)
vx = math.cos(angle)
vy = math.sin(angle)
padx = 100
speed = 1.01
score = 0

def update():
    global ballx, bally, angle, vx, vy, padx, score
    vx = vx * speed
    vy = vy * speed

    ballx += vx
    bally += vy
    if ballx < 0 or 200 < ballx:
        vx = -vx
    padx = pyxel.mouse_x

    if 195 <= bally and padx - 20 < ballx and ballx < padx + 20:
        score += 100
        ballx = 0
        bally = 0
    else:
        if bally >= 200:
            ballx = 0
            bally = 0

def draw():
    global ballx, bally, angle, vx, vy, padx, score
    pyxel.cls(7)
    pyxel.circ(ballx, bally, 10, 6)
    pyxel.rect(padx-20, 195, 40, 5, 14)
    pyxel.text(0, 0, str(score), 0)

pyxel.run(update, draw)