import pyxel

pyxel.init(200, 200)
pyxel.mouse(True)
pyxel.cls(7)

start_x, start_y = 0, 0
end_x, end_y = 0, 0


def update():
    global start_x, start_y, end_x, end_y
    if pyxel.btnp(pyxel.KEY_SPACE):
        start_x, start_y = pyxel.mouse_x, pyxel.mouse_y

    if pyxel.btn(pyxel.KEY_SPACE):
        end_x, end_y = pyxel.mouse_x, pyxel.mouse_y


def draw():
    global start_x, start_y, end_x, end_y
    pyxel.cls(7)

    pyxel.line(start_x, start_y, end_x, end_y, 0)


pyxel.run(update, draw)
