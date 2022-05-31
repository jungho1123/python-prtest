#오각형을 360도 회전해 마법진 같이 생긴 것을 그려라 

import turtle as t

for i in range(15):
    for i in range(5):
        t.forward(50)
        t.left(72)
    t.left(6)
    t.setheading(90)

    for i in range(5):
        t.forward(50)
        t.left(72)
    t.setheading(180)

    for i in range(5):
        t.forward(50)
        t.left(72)
    t.setheading(270)

    for i in range(5):
        t.forward(50)
        t.left(72)
    t.setheading(360)
