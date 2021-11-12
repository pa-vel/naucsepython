from turtle import forward, left, right, speed, exitonclick

speed(0)

def kresli(delka, uhel):
    if delka < 20:
        forward(delka)
        left(180)
        forward(delka)
        left(180)
    else:
        forward(delka/2)
        right(uhel)
        kresli(delka/2, uhel*2/3)
        left(uhel)
        kresli(delka/2, uhel*2/3)
        left(uhel)
        kresli(delka/2, uhel*2/3)
        right(uhel)
        left(180)
        forward(delka/2)
        left(180)

left(90)
kresli(200, 60)
exitonclick()