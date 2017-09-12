# 반지름을 20씩 증가시켜 (0,0),(100,0),(200,0) 좌표에 원을 3개 그리기.

import turtle

rad = 50

t = turtle.Turtle()
t.shape("turtle")
t.circle(rad)

t.up()
t.goto(100,0)
rad = rad+20
t.down()
t.circle(rad)

t.up()
t.goto(200,0)
rad = rad+20
t.down()
t.circle(rad)
