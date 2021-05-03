import turtle as tt
from random import randint
from time import sleep
sc=tt.Screen()
sc.tracer(0, 0)
sc.bgcolor("white")

def spiral(pen,size,angle):
    tt.colormode(255)
    for i in range(size):
        #pen.pencolor(*[randint(0,255) for i in range(3)]) #random renkler icin
        pen.forward(i)
        pen.left(angle)

def tree(n,kalem,aci,uzunluk,doygunluk):
    kalem.hideturtle()
    if n==0:
        return
    kalem1,kalem2 = kalem.clone(),kalem.clone()
    kalem1.left(aci)
    kalem2.right(aci)
    kalem1.forward(uzunluk)
    kalem2.forward(uzunluk)
    if n < doygunluk:  # 3lu dal cikarma uclarda oluyor dolgunlastirmak icin
        kalem3 = kalem.clone()
        kalem3.forward(uzunluk)
        tree(n - 1, kalem3, aci, uzunluk - 1,doygunluk)
    tree(n - 1, kalem1,aci,uzunluk-1,doygunluk)
    tree(n - 1, kalem2,aci,uzunluk-1,doygunluk)
"""while True:agac buyume
    pen.reset()
    pen.left(90)
    pen.forward(150)
    for i in range(9):
        tree(i,pen,25,40,1)
        sc.update()
    sc.clear()
    sc.tracer(0,0)"""

pen=tt.Turtle()
def spin():
    while True:#spiral dondurme
        for i in range(360):
            spiral(pen,400,90+i)
            sc.update()
            pen.reset()
            pen.right(i)

spin()
