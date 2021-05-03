from turtle import *
from threading import Thread

kalem=Turtle()
kalem1=Turtle()
kalem3=Turtle()
kalem4=Turtle()


def kalp1():
    kalem1.left(20)
    kalem1.circle(250, 50)
    kalem1.circle(82.5, 170)
    kalem1.setheading(120)
    kalem1.circle(85, 170)
    kalem1.circle(244, 52)
    kalem1.penup()
    kalem1.speed(100)
    kalem1.setposition(-1000,-1000)

def cicek1():
    kalem.left(90)
    kalem.forward(170)
    pos = kalem.pos()
    for i in range(1, 9):
        kalem.circle(60, 45)
        kalem.penup()
        kalem.setposition(pos)
        kalem.pendown()
    for i in range(1, 9):
        kalem.circle(-60, 45)
        kalem.penup()
        kalem.setposition(pos)
        kalem.pendown()
    kalem.left(20)
    for i in range(1, 9):
        kalem.circle(-45, 45)
        kalem.penup()
        kalem.setposition(pos)
        kalem.pendown()
    for i in range(1, 9):
        kalem.circle(45, 45)
        kalem.penup()
        kalem.setposition(pos)
        kalem.pendown()
    kalem.penup()
    kalem.speed(100)
    kalem.setposition(-1000,-1000)

def cicek2():
    kalem4.left(90)
    kalem4.forward(80)
    kalem4.right(60)
    kalem4.forward(70)
    pos1 = kalem4.pos()
    for i in range(1, 9):
        kalem4.circle(-40, 45)
        kalem4.penup()
        kalem4.setposition(pos1)
        kalem4.pendown()
    for i in range(1, 9):
        kalem4.circle(40, 45)
        kalem4.penup()
        kalem4.setposition(pos1)
        kalem4.pendown()
    kalem4.left(20)
    for i in range(1, 9):
        kalem4.circle(-30, 45)
        kalem4.penup()
        kalem4.setposition(pos1)
        kalem4.pendown()
    for i in range(1, 9):
        kalem4.circle(30, 45)
        kalem4.penup()
        kalem4.setposition(pos1)
        kalem4.pendown()
    kalem4.penup()
    kalem4.speed(100)
    kalem4.setposition(-1000,-1000)

def cicek3():
    kalem3.left(90)
    kalem3.forward(80)
    kalem3.left(60)
    kalem3.forward(70)
    pos2 = kalem3.pos()
    for i in range(1, 9):
        kalem3.circle(40, 45)
        kalem3.penup()
        kalem3.setposition(pos2)
        kalem3.pendown()
    for i in range(1, 9):
        kalem3.circle(-40, 45)
        kalem3.penup()
        kalem3.setposition(pos2)
        kalem3.pendown()
    kalem3.left(20)
    for i in range(1, 9):
        kalem3.circle(-30, 45)
        kalem3.penup()
        kalem3.setposition(pos2)
        kalem3.pendown()
    for i in range(1, 9):
        kalem3.circle(30, 45)
        kalem3.penup()
        kalem3.setposition(pos2)
        kalem3.pendown()
    kalem3.penup()
    kalem3.speed(100)
    kalem3.setposition(-1000,-1000)

if __name__ == '__main__':
    kalp1()
    cicek1()
    Thread(target=cicek2).start()
    Thread(target=cicek3).start()

done()
