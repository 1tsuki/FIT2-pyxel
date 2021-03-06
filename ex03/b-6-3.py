import pyxel

pyxel.init(200, 200)

a = 0
reverse = False


def update():
    global a, reverse
    if reverse:
        a -= 1
    else:
        a += 1

    if 200 < a:
        reverse = True
    if a < 0:
        reverse = False


def draw():
    global a
    pyxel.cls(7)
    pyxel.circ(a, a, 10, 0)


pyxel.run(update, draw)
