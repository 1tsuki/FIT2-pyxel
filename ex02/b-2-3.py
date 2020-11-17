import pyxel
import math

pyxel.init(200, 200)
pyxel.cls(7)

# リサージュ図形のパラメタ
a = 3
b = 2

# 描画半径と起点
r = 100
dx = 100
dy = 100

# 何回に分割して描画するか
count = 360

for i in range(count):
    # 2π = 360度 を count回で分割して描画している
    t = 2 * math.pi * (i / count)
    x = r * math.sin(a * t)
    y = -r * math.sin(b * t)

    color = int(i / (count / 6))
    pyxel.line(dx, dy, dx + x, dy + y, color)
    pyxel.flip()
pyxel.show()
