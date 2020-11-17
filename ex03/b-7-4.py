import pyxel

pyxel.init(200, 200)
pyxel.mouse(True)
pyxel.cls(7)

start_x, start_y = 0, 0
end_x, end_y = 0, 0
pressed = 0


def update():
    global start_x, start_y, end_x, end_y, pressed
    if pyxel.btnp(pyxel.KEY_SPACE):
        pressed += 1
        if 2 < pressed:
            pressed = 1

        if pressed == 1:
            start_x, start_y = pyxel.mouse_x, pyxel.mouse_y

        if pressed == 2:
            end_x, end_y = pyxel.mouse_x, pyxel.mouse_y


def draw():
    global start_x, start_y, end_x, end_y, pressed
    pyxel.cls(7)

    if pressed == 1:
        pyxel.line(start_x, start_y, pyxel.mouse_x, pyxel.mouse_y, 0)

    if pressed == 2:
        pyxel.line(start_x, start_y, end_x, end_y, 0)


pyxel.run(update, draw)
