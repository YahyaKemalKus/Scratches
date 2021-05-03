from turtle import *
from tkinter import *

def arayuz():
    tk_ekran=Tk()
    tk_ekran.geometry("200x100+200+200")
    tk_ekran.resizable(0,0)
    kelime=Entry(width=12)
    kelime.place(relx=0,rely=0)
    def bak(klme):
        rely=0
        for bit in [bin(ord(harf))[2:] for harf in klme]:
            Label(text=bit,font=("Arial", 15, "italic bold")).place(relx=0.5,rely=rely)
            rely+=0.25

    def ciz(kelme):
        ekran=Screen()
        ekran.clear()
        ekran.bgcolor("black")
        ekran.tracer(5)
        harf_say=len(kelme)
        satir_yuks = 800 / harf_say
        harf_yuks = satir_yuks - 90
        aralik = harf_yuks / 2+18
        #tek_satir_bit_say = 1720 / aralik
        #tek_satir_harf_say = int(tek_satir_bit_say / 7)
        satir_yuks=800/harf_say#(harf_say/tek_satir_harf_say)
        kalem_kal=harf_yuks/8
        bsx, bsy = -700, 380-harf_yuks
        sayac = 0
        bins = "".join([bin(ord(harf))[2:] for harf in kelme])

        for boo in bins:
            sayac += 1
            if boo == "1":
                bsx +=aralik
                bir(bsx , bsy,harf_yuks,kalem_kal)
                print(bsx)

            if boo == "0":
                bsx += aralik
                sifir(bsx, bsy,harf_yuks,kalem_kal)
                print(bsx)
            if sayac % 7==0:#(tek_satir_harf_say*7) == 0:
                bsy -= int(satir_yuks)
                bsx = -700
                sayac=0

        done()

    def bir(x, y, yukseklik,kalem_kal):
        s = Screen()
        s.tracer(36, 0)
        kalem=Turtle()
        kalem.pensize(kalem_kal)
        kalem.pencolor(0.2,1,0.05)
        kalem.hideturtle()
        kalem.speed(100)
        kalem.penup()
        alt_cizgi = int(yukseklik / 7)
        boy = int(yukseklik / 2)
        kalem.setposition(x - alt_cizgi, y)
        kalem.setheading(0)
        kalem.pendown()

        for i in [*range(49, alt_cizgi + 49), *range(-alt_cizgi - 49, -48)]:
            c = abs(i / (alt_cizgi + 50))
            kalem.pencolor(c, c, c)
            kalem.forward(1)

        kalem.penup()
        kalem.setposition(x, y)
        kalem.pendown()
        kalem.left(90)
        for i in range(-boy, boy):
            kalem.pencolor(abs(i / (boy + 5)), abs(i / (boy + 5)), abs(i / (boy + 5)))
            kalem.forward(1)
        kalem.left(135)
        for i in range(-alt_cizgi - 49, -49):
            c = abs(i / (alt_cizgi + 56))
            kalem.pencolor(c, c, c)
            kalem.forward(1)

    def sifir(x, y, yukseklik,kalem_kal):
        s = Screen()
        s.tracer(36, 0)
        kalem2=Turtle()
        kalem2.pensize(kalem_kal)
        kalem2.hideturtle()
        kalem2.pencolor(0.2,1,0.05)
        kalem2.penup()
        kalem2.setposition(x, y)
        kalem2.setheading(0)
        kalem2.pendown()
        uzunluk1 = yukseklik / 4
        uzunluk2 = yukseklik * 3.21
        for i in range(85):
            c = abs(i / 84)
            kalem2.pencolor(c, c, c)
            kalem2.circle(uzunluk1, 1)
        for i in range(-86, 0, 2):
            c = abs(i / 86)
            kalem2.pencolor(c, c, c)
            kalem2.circle(uzunluk2, 10 / 85)
        for i in range(0, 86, 2):
            c = abs(i / 86)
            kalem2.pencolor(c, c, c)
            kalem2.circle(uzunluk2, 10 / 85)
        for i in range(-85, 0):
            c = abs(i / 85)
            kalem2.pencolor(c, c, c)
            kalem2.circle(uzunluk1, 1)
        for i in range(85):
            c = abs(i / 84)
            kalem2.pencolor(c, c, c)
            kalem2.circle(uzunluk1, 1)
        kalem2.penup()
        kalem2.setposition(x, y)
        kalem2.setheading(0)
        kalem2.left(180)
        kalem2.pendown()
        for i in range(85):
            c = abs(i / 84)
            kalem2.pencolor(c, c, c)
            kalem2.circle(-uzunluk1, 1)
        for i in range(-86, 0, 2):
            c = abs(i / 86)
            kalem2.pencolor(c, c, c)
            kalem2.circle(-uzunluk2, 10 / 85)
        for i in range(0, 86, 2):
            c = abs(i / 86)
            kalem2.pencolor(c, c, c)
            kalem2.circle(-uzunluk2, 10 / 85)

    Button(text="bak",width=4,command=lambda:bak(kelime.get())).place(relx=0,rely=0.2)
    Button(text="ciz",width=4,command=lambda :ciz(kelime.get())).place(relx=0.19,rely=0.2)
    mainloop()



if __name__ == '__main__':
    arayuz()

