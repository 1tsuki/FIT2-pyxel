import pyxel
import math

pyxel.init(200, 200, scale=2)
pyxel.cls(7)
x = [120, 80, 80, 120]
y = [120, 120, 80, 80]
offset = [0, 90, 180, 270]

for r in range(0, 90, 1):
    for i in range(len(x)):
        pyxel.line(x[i], y[i], 100 + math.cos(math.radians(offset[i] + r)) * 100, 100 + math.sin(math.radians(offset[i] + r)) * 100, 0)

    pyxel.flip()
pyxel.show()
