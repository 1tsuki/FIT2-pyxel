import pyxel

pyxel.init(200, 200)

a = 0
reverse = False


def update():
    global a, reverse

    if 200 < a:
        reverse = True
    if a < 0:
        reverse = False

    if pyxel.btn(pyxel.KEY_SPACE):
        reverse = not reverse

    if reverse:
        a -= 1
    else:
        a += 1


def draw():
    global a
    pyxel.cls(7)
    pyxel.circ(a, a, 10, 0)


pyxel.run(update, draw)
