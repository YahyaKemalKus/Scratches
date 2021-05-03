import struct
import sys
import pygame
#jpglerin renklendirme bytelari 54.byettan itibaren basliyor.
#jpgler okunurken en alt soldan basliyor.soldan saga dogru okuyor.eger yatay(x) 6 pixel varsayarsak her bir pixel renklendirmesi icin 3'er byte aliyor.
#6x3 yapildiginda 18 cikiyor ve 4'un kati degil.4'un kati yapmak icin o satirin byte dizisine 2 tane degeri 0(\x00) olan byte ekliyor ve 20'ye tamamliyor.
#4 un kati olmayan her yatay pixel sayisi icin bunu yapiyor.
#colors={"\x00\x00\x00":1} belki bi ara sozlugu buyutup ufak bi fotoshop programi yapabilirim.
class BmpReader:
    def __init__(self,path):
        with open(file=path,mode="rb") as f:
            self.veri=f.read()
            f.close()
        self.genislik_b=self.veri[18:22]# bu kisimlarin aciklamalari BMP_YAPISI.py icinde bulunmaktadir.
        self.genislik_i=struct.unpack("L",self.veri[18:22])[0]
        self.yukseklik_b=self.veri[22:26]
        self.yukseklik_i=struct.unpack("L",self.veri[22:26])[0]
        self.fotobytes=self.veri[54:]
        self.boyut=len(self.veri)
        self.keskinlik=128 #default degeri
        self.x=0
        self.mat=None
        self.matris()
        self.flag="BGR"
    def __str__(self):
        return "Bmp turundeki dosyalarla ilgili islem yapmak icin kullandigim sinif"


    def info(self):
        info=f"Resmin yuksekligi  {self.yukseklik_b}  -> {self.yukseklik_i}\n\
            Resmin genisligi   {self.genislik_b}  -> {self.genislik_i}\n\
            Resmin boyutu\t   {self.boyut} bytes"
        return info.replace(" "*4,"")


    """def make_it_sharp(self):#siyaha cok yakin tonlara sahip pixelleri listeye 0 digerlerini 1 olarak ekliyor.resmin matrisini cikartiyor.
        sifir_bir_matris=[]#sifir ve birlerden olusacak olan matris
        cop_bytes=4-(self.genislik_i*3)%4#bmp yapisiyla alakali gereksiz eklenen bytelari almamak icin
        index=0
        for i in range(self.yukseklik_i):
            baslangic=(self.genislik_i*3+cop_bytes)*i
            bitis=(self.genislik_i*3+cop_bytes)*(i+1)
            satir_bytes=self.fotobytes[baslangic:bitis]#her bir satirdaki pixellerin bytelari
            if cop_bytes!=0: #eger varsa 4 un katina tamamlamak icin eklenmis olan sondaki cop bytei (\x00) listeden kaldiriyoruz.
                satir_bytes=satir_bytes[0:-cop_bytes]
            satir_pixel_bytes=[satir_bytes[i:i+3] for i in range(0,self.genislik_i*3,3)]#her pixel 3 byte (RGB) buyuklugunde bu yuzden 3erli grupluyoruz.
            satir_sifir_bir=[]

            for pixel_bytes in satir_pixel_bytes:#3erli bytelar halinde gruplanmis listedeki gruplari sirayla donguye sokuyoruz. #
                if all([*map(lambda x:x in range(self.keskinlik),pixel_bytes)]):#eger siyah tonlariysa                           #
                    satir_sifir_bir.append(1)#matrisimize 1 ekliyoruz.                                                           #
                else:#degilse 0 ekliyoruz.                                                                                       #renklere gore matrise ekleme kismi
                    satir_sifir_bir.append(0)                                                                                    #sozluk eklenirse bu kisim degisecek
            sifir_bir_matris.append(satir_sifir_bir)                                                                             #
        self.mat=[*reversed(sifir_bir_matris)]
        return [*reversed(sifir_bir_matris)] #bytelar resmin sol altindan basladigi icin listeyi tersine dondurup resimle esliyoruz
                                             #ilk pixel resmin sol en ustundeki pixeli temsil etmis oluyor."""


    def matris(self):
        matris_ = []
        cop_bytes = 4 - (self.genislik_i * 3) % 4
        for i in range(self.yukseklik_i):
            baslangic = (self.genislik_i * 3 + cop_bytes) * i
            bitis = (self.genislik_i * 3 + cop_bytes) * (i + 1)
            satir_bytes = self.fotobytes[baslangic:bitis]
            if cop_bytes != 0:
                satir_bytes = satir_bytes[0:-cop_bytes]
            satir_pixel_bytes = [satir_bytes[i:i + 3] for i in range(0, self.genislik_i * 3, 3)]
            matris_.append(satir_pixel_bytes)
        self.mat=[*reversed(matris_)]
        return [*reversed(matris_)]

    @staticmethod
    def convert_bw(matris, keskinlik=128):
        new_matris = matris
        for row in enumerate(matris):
            for column in enumerate(row[1]):
                color = (column[1][0] + column[1][1] + column[1][2]) / 3
                if color >= keskinlik:
                    new_matris[row[0]][column[0]] = b"\xff\xff\xff"
                else:
                    new_matris[row[0]][column[0]] = b"\x00\x00\x00"
        return new_matris

    def convert_rgb2gray(self):
        assert self.flag=="RGB", "Given matris is not in RGB format"
        new_matris = self.matris()
        for row in enumerate(self.matris(), 0):
            for column in enumerate(row[1], 0):
                color = (column[1][0] + column[1][1] + column[1][2]) / 3
                new_matris[row[0]][column[0]] = [color, color, color]
        self.flag = "GRAY"
        self.mat = new_matris
        return new_matris

    def convert_bgr2gray(self):
        assert self.flag=="BGR", "Given matris is not in BGR format"
        new_matris = self.matris()
        for row in enumerate(self.matris(), 0):
            for column in enumerate(row[1], 0):
                color=int((column[1][0]+column[1][1]+column[1][2])/3)
                new_matris[row[0]][column[0]] =bytes([color,color,color])
        self.flag = "GRAY"
        self.mat=new_matris
        return new_matris

    def convert_bgr2rgb(self):
        assert self.flag=="BGR", "Given matris is not a BGR format"
        new_matris=self.matris()
        for row in enumerate(self.matris(),0):
            for column in enumerate(row[1],0):
                new_matris[row[0]][column[0]]=column[1][::-1]
        self.flag="RGB"
        self.mat=new_matris
        return new_matris

    @staticmethod
    def draw_matris(surface, matris, zoom=1):#pixellerin renk degerlerini iceren matrisi pygamede ciziyor,width 1 pixelin buyuklugu
        pygame.init()
        for row, y in zip(matris, range(len(matris))):
            for pixel, x in zip(row, range(len(row))):
                pygame.draw.rect(surface, pixel, (x*zoom, y*zoom, zoom, zoom))
        pygame.display.update()

    @staticmethod
    def add_matris(matris1, matris2, opacity):
        min_x = len(matris1[0]) if len(matris1[0]) <= len(matris2[0]) else len(matris2[0])
        min_y = len(matris1) if len(matris1) < len(matris2) else len(matris2)
        to_sum_matris = [[a[0:min_x], b[0:min_x]] for a, b in zip(matris1[0:min_y], matris2[0:min_y])]
        new_matris = []
        for i, y in to_sum_matris:
            sum_of_row = []
            for a, b in zip(i, y):
                R = int((a[0] + b[0] * opacity) / (2 + opacity))
                G = int((a[1] + b[1] * opacity) / (2 + opacity))
                B = int((a[2] + b[2] * opacity) / (2 + opacity))
                new_pixel = (R, G, B)
                sum_of_row.append(new_pixel)
            new_matris.append(sum_of_row)
        return new_matris

    def cizdir(self,width,three_d=False):
        pygame.init()
        pencere = pygame.display.set_mode((1500, 840),0,5)#cizim penceresi boyutunu ayarliyoruz
        matrix = self.make_it_sharp()#yukardaki fonksiyondan gelen 0 ve 1 iceren matrisi matrixe atiyoruz.
        satir_index = 0 #resimdeki satirlar sirayla alinacagindan index kullanarak teker teker aliyoruz.
        y = 0 #y koordinatinin baslangic noktasi
        #cut=False#kesim kontrolu
        while True:
            r=255
            g=255
            b=255
            #keys = pygame.key.get_pressed()
            x=self.x
            #if keys[pygame.K_DOWN]: # sag ok tusuna basili tuttukca cizim yapiyor
            if satir_index < len(matrix):
                satir = matrix[satir_index]#matristen sirayla yatay listeler aliniyor
                for pixel in satir:
                    if pixel == 1:
                        if three_d:
                            for i in range(5):#3 boyutun cizgi uzunluklari
                                pygame.draw.rect(pencere, (r,g,b), (x-i, y+i, width, width))# matriste degeri 1 olan elemanin konumu baz alinarak beyaz 1x1 kare ciziliyor
                        if not three_d:
                                pygame.draw.rect(pencere, (r, g, b), (x, y, width, width))
                    x += width
                    if r>0:
                        r-=1
                    if r==0 and g>0:
                        g-=1
                    if r==0 and g==0 and b>0:
                        b-=1
                if three_d:
                    self.x+=1
                y += width#matriste bir alt listeye gecildiginden cizimin y koordinati da bir asagi cekiliyor.
                satir_index += 1#matriste bir alttaki listeyi almak icin indexi 1 artiriyoruz.
                pygame.display.update()#cizim ekraninin guncelliyoruz.

            events=pygame.event.get()

            if events:
                for event in events:
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        start=pygame.mouse.get_pos()
                    if event.type==pygame.MOUSEBUTTONUP:
                        if event.__dict__.get('button')==1:
                            end=pygame.mouse.get_pos()
                            matrix=[satirr[start[0]-x:end[0]-x] for satirr in matrix[start[1]-y:end[1]-y]]
                            satir_index=0
                            y=0#start[1]
                            pencere.fill((0,0,0))
                    if event.type==pygame.MOUSEWHEEL:
                        if event.__dict__.get('y')==1:#ileri yuvarlama
                            satir_index=0
                            y=0
                            width+=1
                            pencere.fill((0, 0, 0))
                        if event.__dict__.get('y')==-1:#geri yuvarlama
                            satir_index = 0
                            y = 0
                            if width>1:
                                width -= 1
                            pencere.fill((0, 0, 0))
                    if event.type==pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                pygame.display.update()
#foto=BmpReader(r"C:\Users\yahyakemall\Desktop\labirent2.bmp")
#foto.make_it_sharp()
#foto.cizdir(1)