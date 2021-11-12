from turtle import forward, left, right, penup, pendown, speed, exitonclick
from math import sqrt

speed(0)

def vykresli_domecek(velikost):
    for i in range(4):
        forward(velikost)
        left(90)
    left(45)
    forward(sqrt(2) * velikost)
    left(90)
    forward((sqrt(2) * velikost)/2)
    left(90)
    forward((sqrt(2) * velikost)/2)
    left(90)
    forward(sqrt(2) * velikost)
    left(45)
    forward(velikost)

vykresli_domecek(30)
vykresli_domecek(40)
vykresli_domecek(80)

exitonclick()