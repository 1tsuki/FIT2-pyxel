import pyxel
import math
import random

pyxel.init(200, 200)

ballx = []
bally = []
angle = []
vx = []
vy = []
padx = 100
speed = 1.05
score = 0
failure = 0
success = 0
gameover = False

pyxel.sound(0).set(note='C3', tone='T', volume='3', effect='N', speed=30)
pyxel.sound(1).set(note='C1', tone='T', volume='3', effect='N', speed=30)

def reset_ball(num):
    global ballx, bally, angle, vx, vy
    ballx[num] = random.randint(0, 199)
    bally[num] = 0
    angle[num] = math.radians(random.randint(30, 150))
    vx[num] = math.cos(angle[num])
    vy[num] = math.sin(angle[num])

def add_ball():
    global ballx, bally, angle, vx, vy
    ballx.append(random.randint(0, 199))
    bally.append(0)
    tmp = math.radians(random.randint(30, 150))
    angle.append(tmp)
    vx.append(math.cos(tmp))
    vy.append(math.sin(tmp))

add_ball()

def update():
    global ballx, bally, angle, vx, vy, padx, score, failure, success, gameover
    padx = pyxel.mouse_x

    for i in range(len(ballx)):
        vx[i] = vx[i] * speed
        vy[i] = vy[i] * speed

        ballx[i] += vx[i]
        bally[i] += vy[i]
        if ballx[i] < 0 or 200 < ballx[i]:
            vx[i] = -vx[i]


        if 195 <= bally[i]:
            if padx - 20 <= ballx[i] and ballx[i] <= padx + 20:
                score += 100
                pyxel.play(0, 0)
                success = success + 1
                if success >= 10:
                    success = 0
                    add_ball()
            else:
                pyxel.play(0, 1)
                failure = failure + 1
                if failure > 10:
                    gameover = True
            reset_ball(i)


def draw():
    global ballx, bally, angle, vx, vy, padx, score, failure, gameover
    pyxel.cls(7)
    if gameover:
        pyxel.text(0, 0, "GAME OVER...", 0)
    else:
        for i in range(len(ballx)):
            pyxel.circ(ballx[i], bally[i], 10, 6)
        pyxel.rect(padx - 20, 195, 40, 5, 14)
        pyxel.text(0, 0, str(score), 0)
        pyxel.text(150, 0, str(failure), 0)


pyxel.run(update, draw)