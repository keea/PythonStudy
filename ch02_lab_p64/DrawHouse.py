# 집그리기

import turtle

size = int(input("집의 크기는 얼마로 할까요?"))


t = turtle.Turtle()
t.forward(size)
t.right(90)
t.forward(size)
t.right(90)
t.forward(size)
t.right(90)
t.forward(size)

t.right(30)
t.forward(size)
t.right(120)
t.forward(size)
