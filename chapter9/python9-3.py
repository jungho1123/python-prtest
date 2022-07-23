import turtle as t

color=['yellow', 'red', 'blue']
t.setup(500,500)
t.bgcolor('black')

for i in range(200):
    t.speed(10)
    t.pencolor(color[i % len(color)])
    t.width(i/200+1)
    t.forward(i*2)
    t.left(119)
