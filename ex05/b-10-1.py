import pyxel
import math
import random

pyxel.init(200, 200)

ballx = [0, 0, 0]
bally = [0, 0, 0]
angle = [0, 0, 0]
vx = [0, 0, 0]
vy = [0, 0, 0]
padx = 100
speed = 1.1
score = 0

pyxel.sound(0).set(note='C3', tone='T', volume='3', effect='N', speed=30)
pyxel.sound(1).set(note='C1', tone='T', volume='3', effect='N', speed=30)

def reset_ball(num):
    global ballx, bally, angle, vx, vy, padx, score
    ballx[num] = random.randint(0, 199)
    bally[num] = 0
    angle[num] = math.radians(random.randint(30, 150))
    vx[num] = math.cos(angle[num])
    vy[num] = math.sin(angle[num])


for i in range(len(ballx)):
    reset_ball(i)


def update():
    global ballx, bally, angle, vx, vy, padx, score
    padx = pyxel.mouse_x

    for i in range(len(ballx)):
        vx[i] = vx[i] * speed
        vy[i] = vy[i] * speed

        ballx[i] += vx[i]
        bally[i] += vy[i]
        if ballx[i] < 0 or 200 < ballx[i]:
            vx[i] = -vx[i]


        if 195 <= bally[i]:
            if padx - 20 < ballx[i] and ballx[i] < padx + 20:
                score += 100
                pyxel.play(0, 0)
            else:
                pyxel.play(0, 1)
            reset_ball(i)


def draw():
    global ballx, bally, angle, vx, vy, padx, score
    pyxel.cls(7)
    for i in range(len(ballx)):
        pyxel.circ(ballx[i], bally[i], 10, 6)
    pyxel.rect(padx - 20, 195, 40, 5, 14)
    pyxel.text(0, 0, str(score), 0)


pyxel.run(update, draw)