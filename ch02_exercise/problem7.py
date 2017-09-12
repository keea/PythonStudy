# 작은 사각형의 한 변의 길이는 side 변수에 저장
# 작은 사각형의 각도는 angle 변수에 저장
# 사각형 그리기.

import turtle

side = 100
angle = 90

t = turtle.Turtle()
t.shape("turtle")

t.forward(side)
t.right(angle)
t.forward(side)
t.right(angle)
t.forward(side)
t.right(angle)
t.forward(side)

t.forward(side)
t.right(angle)
t.forward(side)
t.right(angle)
t.forward(side)

t.forward(side)
t.left(angle)
t.forward(side)
t.left(angle)
t.forward(side)
t.left(angle)
t.forward(side)

t.right(angle*2)

t.forward(side)
t.left(angle)
t.forward(side)
t.left(angle)
t.forward(side)
t.left(angle)
t.forward(side)

