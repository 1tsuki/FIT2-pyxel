import pyxel


class App:
    def __init__(self):
        pyxel.init(200, 150, caption='Pyxel Sample App')
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(1)
        pyxel.text(16, 17, "q: Quit App", 14)


App()
