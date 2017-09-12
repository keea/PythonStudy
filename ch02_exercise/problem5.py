# side 변수의 초기값 100.
# side 변수를 이용하여 삼각형 그리기

import turtle

side = 100

t = turtle.Turtle()
t.shape("turtle")
t.forward(side)
t.left(120)
t.forward(side)
t.left(120)
t.forward(side)

