import pyxel

pyxel.init(200, 200)
pyxel.cls(7)
for a in range(0, 201, 20):
    for b in range(0, 201, 20):
        pyxel.line(a, 0, b, 200, 0)
        pyxel.flip()
pyxel.show()
