import pygame
from random import randint
import sys
"""cok onceden yazdigim bir kod ve tamamen bitmemis halde.Sadece pratik olsun diye eglenmelik kod"""
pygame.init()
pencere=pygame.display.set_mode((800,800))
V=1
carpisma=False

class oyun():
    def __init__(self):
        self.konum=pygame.Rect(0,580,20,20)
        self.zeminuzunluk=[]
        self.harekethizi=1
        self.ziplamahizi=17
        self.fps=300
        self.mapler=[]
        self.duvaruzuluklari=[]
        self.sayac=0
        self.zeminx=[]
        self.zeminy=[]
        self.mapolusturucu()

    def mapolusturucu(self):
        x=0
        y=600
        while True:
            x1 = randint(100, 250)
            self.mapler.append((x, y, x1, 40))
            self.zeminx.append([x, x + x1])
            self.zeminy.append(y - 20)
            x += x1 + randint(50, 100)
            y -= randint(50, 100)
            if x > 800:
                print(self.zeminx[len(self.zeminx) - 1][1])
                if not 800 in range(self.zeminx[len(self.zeminx) - 1][0], self.zeminx[len(self.zeminx) - 1][1]):
                    yeni = (self.mapler[len(self.mapler) - 1][0], self.mapler[len(self.mapler) - 1][1], 500, 40)
                    self.mapler.remove((self.mapler[len(self.mapler) - 1][0], self.mapler[len(self.mapler) - 1][1],
                                        self.mapler[len(self.mapler) - 1][2], 40))
                    self.mapler.append(yeni)
                    self.zeminx.append([self.zeminx[len(self.zeminx) - 1][0], self.zeminx[len(self.zeminx) - 1][0] + (
                                800 - self.zeminx[len(self.zeminx) - 1][0])])
                    self.zeminx.remove(self.zeminx[len(self.zeminx) - 2])

                break


        if not 800 in range(self.zeminx[len(self.zeminx)-1][0],self.zeminx[len(self.zeminx)-1][1]):
            yeni=(self.mapler[len(self.mapler)-1][0],self.mapler[len(self.mapler)-1][1],500,40)
            self.mapler.remove((self.mapler[len(self.mapler)-1][0],self.mapler[len(self.mapler)-1][1],self.mapler[len(self.mapler)-1][2],40))
            self.mapler.append(yeni)

        for i in self.mapler:
            pygame.draw.rect(pencere, (255, 255, 255), i)
            pygame.display.update()


    def yuru(self):
            global V
            if self.zeminkontrol1():
                pygame.draw.rect(pencere,(0,0,0),self.konum)
                self.konum=self.konum.move(self.harekethizi,0)
                pygame.draw.rect(pencere,(255,255,255),self.konum)
                pygame.display.update()
                saat.tick(self.fps)


            if not self.zeminkontrol1():#hata
               while True:
                pygame.draw.rect(pencere,(0,0,0),self.konum)
                self.konum=self.konum.move(self.harekethizi,V/15)
                pygame.draw.rect(pencere,(255,255,255),self.konum)
                pygame.display.update()
                saat.tick(self.fps)
                V+=1
                if self.konum.y>800:
                    pygame.draw.rect(pencere,(0,0,0),self.konum)
                    self.konum.x,self.konum.y=0,580
                    pygame.draw.rect(pencere,(255,255,255),self.konum)
                    pygame.display.update()
                    V=1
                    break



    def zipla(self):
        global carpisma
        while True:
            self.zeminkontrol()

            if carpisma:
                pygame.draw.rect(pencere, (0, 0, 0), (self.konum.x-10,self.konum.y-10,30,20))
                pygame.draw.rect(pencere,(0,0,0),(self.konum.x-20,self.konum.y-20,40,80))
                pygame.display.update()
                while True:

                    pygame.draw.rect(pencere,(0,0,0),self.konum)
                    self.konum=self.konum.move(-self.harekethizi-3,-self.ziplamahizi)
                    pygame.draw.rect(pencere,(255,255,255),self.konum)
                    self.ziplamahizi-=1/2
                    pygame.display.update()
                    saat.tick(60)

                    if self.konum.y > 800:
                        self.konum.x, self.konum.y = 0, 580
                        pygame.draw.rect(pencere, (255, 255, 255), self.konum)
                        pygame.display.update()
                        self.ziplamahizi = 17
                        carpisma=False
                        break
                break
            pygame.draw.rect(pencere,(0,0,0),self.konum)
            self.konum=self.konum.move(self.harekethizi+3,-self.ziplamahizi)
            pygame.draw.rect(pencere,(255,255,255),self.konum)
            self.ziplamahizi-=1
            pygame.display.update()
            saat.tick(60)





            if self.zeminkontrol():

                pygame.draw.rect(pencere,(0,0,0),(self.zeminkontrol()[2]-20,self.zeminkontrol()[1]-40,80,40))
                pygame.draw.rect(pencere,(0,0,0),(self.zeminkontrol()[2]-20,self.zeminkontrol()[1],20,40))
                pygame.draw.rect(pencere,(0,0,0),self.konum)
                self.konum.y=self.zeminkontrol()[1]
                pygame.draw.rect(pencere,(255,255,255),self.konum)
                pygame.display.update()
                self.ziplamahizi=17
                break


            if self.konum.y>800:
                    self.konum.x,self.konum.y=0,580
                    pygame.draw.rect(pencere,(255,255,255),self.konum)
                    pygame.display.update()
                    self.ziplamahizi=17
                    break








    def zeminkontrol(self):#hata
            sayac=0
            global carpisma
            for k in self.zeminx:
                if self.konum.x+20 in range(k[0],k[1]) and self.konum.y in range(self.zeminy[sayac]-5,self.zeminy[sayac]+17) or \
                        self.konum.x in range(k[0],k[1]) and self.konum.y in range(self.zeminy[sayac]-5,self.zeminy[sayac]+17):
                        self.konum.y=self.zeminy[sayac]
                        return True,self.zeminy[sayac],self.zeminx[sayac][0]

                if self.konum.x+20 in range (self.zeminx[sayac][0]-6,self.zeminx[sayac][0])  and self.konum.y-10 in range(self.zeminy[sayac]-19,self.zeminy[sayac]+40):

                        self.konum.x=self.zeminx[sayac][0]-20
                        print("carpisti,carpisma konumu {}".format(self.konum.x))

                        carpisma=True
                if self.konum.x + 20== self.zeminx[sayac][0] and self.konum.y - 10 in range(self.zeminy[sayac],
                                                                                                    self.zeminy[
                                                                                                        sayac] + 40):
                    self.konum.x = self.zeminx[sayac][0] - 20
                    print("carpisti,carpisma konumu {}".format(self.konum.x))

                    carpisma = True
                else:
                   sayac+=1

    def zeminkontrol1(self):#hata
        sayac1=0
        for k in self.zeminx:
            if self.konum.x+20  in range(k[0], k[1]) or self.konum.x  in range(k[0], k[1]):
                if self.konum.y in range (self.zeminy[sayac1]-5,self.zeminy[sayac1]+17):

                    return True
            else:
                sayac1 += 1

oyun1=oyun()
pygame.key.set_repeat(1,1)
saat=pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:

            if event.key==pygame.K_RIGHT:
                oyun1.yuru()

            if event.key==pygame.K_SPACE:
                oyun1.zipla()


        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()