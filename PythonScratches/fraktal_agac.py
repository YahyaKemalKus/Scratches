import turtle


class FraktalAgac(turtle.Turtle):
    def __init__(self, kalem_rengi:str="cyan",
                 kalem_kalinligi:int=16,
                 baslangic_konumu:tuple=(0, -300),
                 baslangic_acisi:int=90,
                 govde_uzunlugu:int=150,
                 dal_acisi:int=30,
                 bslngc_dal_uzunlugu:int=100,
                 katman_sayisi:int=8):

        super().__init__()
        self.ekran_ayarla()
        self.pencolor(kalem_rengi)
        self.pensize(kalem_kalinligi)
        self.penup()
        self.setposition(baslangic_konumu)
        self.setheading(baslangic_acisi)
        self.pendown()
        self.forward(govde_uzunlugu)
        self.konum = self.pos()
        self.yon = self.heading()
        self.dal_acisi = dal_acisi
        self.kalem_rengi = kalem_rengi
        self.kalem_kalinligi = kalem_kalinligi
        self.bslngc_dal_uzunlugu = bslngc_dal_uzunlugu
        self.__sonuncu_dal_numarasi = 0
        self.__katman_bitis_noktalari = self.katman_bitis_noktasi(katman_sayisi+1)
        self.__konumlar = [[self.pos(), self.yon]]
        self.__kalem_hizi = 100
        self.ciz()

    @staticmethod
    def katman_bitis_noktasi(sayi:int) -> list:
        sayii = 0
        liste = []
        for _sayi in range(1, sayi):
            sayii = 2 ** _sayi - 1
            liste.append(sayii)
        return liste

    def fraktal(self,konum, yon):
        if self.__sonuncu_dal_numarasi == self.__katman_bitis_noktalari[-1]:
            turtle.done()
            return
        self.__sonuncu_dal_numarasi += 1

        kalem2 = turtle.Turtle()
        kalem2.hideturtle()
        kalem2.pensize(self.kalem_kalinligi)
        kalem2.pencolor(self.kalem_rengi)
        kalem2.speed(self.__kalem_hizi)
        kalem2.penup()
        kalem2.setposition(konum)
        kalem2.setheading(yon + self.dal_acisi)
        kalem2.pendown()
        kalem2.forward(self.bslngc_dal_uzunlugu)
        kalem2.hideturtle()

        kalem3 = turtle.Turtle()
        kalem3.hideturtle()
        kalem3.pensize(self.kalem_kalinligi)
        kalem3.pencolor(self.kalem_rengi)
        kalem3.speed(100)
        kalem3.penup()
        kalem3.setposition(konum)
        kalem3.setheading(yon - self.dal_acisi)
        kalem3.pendown()
        kalem3.forward(self.bslngc_dal_uzunlugu)
        kalem3.hideturtle()


        self.__konumlar.append([kalem2.pos(), int(kalem2.heading())])
        self.__konumlar.append([kalem3.pos(), int(kalem3.heading())])
        if self.__sonuncu_dal_numarasi in self.__katman_bitis_noktalari:
            self.kalem_kalinligi -= 2 if self.kalem_kalinligi > 2 else 0
            self.bslngc_dal_uzunlugu *= 0.8
        pos, aci = self.__konumlar[self.__sonuncu_dal_numarasi]
        x, y = pos[0], pos[1]
        return self.fraktal(pos, aci)

    @staticmethod
    def ekran_ayarla():
        ekran = turtle.Screen()
        ekran.tracer(1, 0)
        ekran.bgcolor("black")

    def ciz(self):
        pos, aci = self.__konumlar[0]
        self.fraktal(pos, aci)


FraktalAgac()