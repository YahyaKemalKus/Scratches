class Gemi:
    """Gemiler bu sinif kullanilarak uretilecek ve bu sinifin bir uyesi olucaktir."""
    def __init__(self,uzunluk:int,koordinat:tuple,yatay:bool):
            self.uzunluk=uzunluk
            self.koordinat = koordinat
            self.yatay = yatay
            self.bulunulan=self.bulunulan_noktalar()


    def bulunulan_noktalar(self):
        bas_x=self.koordinat[0]
        bas_y=self.koordinat[1]
        koords=[]
        if  not self.yatay:
            for y_nokta in range(bas_y, bas_y + self.uzunluk):
                koords.append((bas_x, y_nokta))
            return koords

        if self.yatay:
            for x_nokta in range(bas_x, bas_x + self.uzunluk):
                koords.append((x_nokta, bas_y))
            return koords


class Harita:
    """Haritanin uretilecegi siniftir."""
    def __init__(self,x_uzunlugu,y_uzunlugu,gizli_mod):
        self.x=x_uzunlugu
        self.y=y_uzunlugu
        self.gizli_mod = gizli_mod
        self.matrix=self.matrix_()


    def matrix_(self):#matrix listesini olusturma fonksiyonu.
        if self.gizli_mod:
            _matrix=[]
            for dikey in range(self.y):
                _matrix.append(["? " for a in range(self.x)])
            return _matrix

        if not self.gizli_mod:
            _matrix = []
            for dikey in range(self.y):
                _matrix.append(["* " for a in range(self.x)])
            return _matrix


class Isleme:
    """Oyunun isleyisini sagliycak fonksiyonlari iceren sinif."""
    def __init__(self,harita_:object,gemi_sayisi:int,gizli_mod:bool):
        self.atis_hakki=int(harita_.x**2/3)
        self.gizli_mod=gizli_mod
        self.matrix=harita_.matrix
        self.harita=harita_
        self.gemi_sayisi=gemi_sayisi
        self.gemiler = self.gemileri_uret()[0]
        self.gemi_noktalari=self.gemileri_uret()[1]
        self.atis_yapilmis_noktalar=[]


    def gemileri_uret(self):#istenilen sekilde gemileri ureten fonksiyon.
        from random import randint
        gemiler_=[]
        dolu_koords=[]
        for gemi_uzunluk in range(1,self.gemi_sayisi+1):#aritmatik uzunlukta gemi uretimi.(1-2-3-4... gibi)
            while 1:#random alinan koordinatlarin istege uymamasi uzerine surekli yenilerinin denenebilmesi icin while kullanildi.
                map_disi=False
                carpisma=False
                randkoord=(randint(1,self.harita.x),randint(1,self.harita.y))#rastgele koordinat uretimi
                randyon=randint(0,1)#rastgele yon(dikey veya yatay) uretimi
                y_gemi=Gemi(gemi_uzunluk,randkoord,randyon)
                for bulunulan_noktalar in y_gemi.bulunulan:#geminin bulundugu koordinatlarin map icinde olup olmadigini kontrol ediliyor.
                    korx=bulunulan_noktalar[0]
                    kory=bulunulan_noktalar[1]
                    if not korx in range(self.harita.x+1) or not kory in range(self.harita.y+1):
                        map_disi=True
                        break

                for bulunulan_nokta in y_gemi.bulunulan_noktalar():#baska bir gemiyle ust uste olup olmadigi kontrol ediliyor.
                    if (*bulunulan_nokta,0) in dolu_koords or (*bulunulan_nokta,1) in dolu_koords:
                        carpisma=True
                        break

                if not map_disi and not carpisma:#map icindeyse ve carpismiyorsa gemi listesine ekleniyor.
                    gemiler_.append(y_gemi)
                    [dolu_koords.append((*y_koord,randyon)) for y_koord in y_gemi.bulunulan]#dolu noktalara yeni eklenen geminin bulundugu noktalar ekleniyor.
                    break

        return gemiler_,dolu_koords


    def render_map(self):#oyunun ekran goruntusunu yenileme fonksiyonu.
        if  self.gizli_mod:
            for y_satir in reversed(self.matrix):
                print(*y_satir)

        if not self.gizli_mod:
            for koord in self.gemi_noktalari:
                korx,kory,yataylik=koord[0],koord[1],koord[2]
                if yataylik:#geminin yonu yataysa
                    self.matrix[kory - 1][korx - 1]="- "

                if not yataylik:#geminin yonu dikeyse
                    self.matrix[kory - 1][korx - 1] = "| "

            for y_satir in reversed(self.matrix):
                print(*y_satir)


    def ates(self,korx,kory):#istenilen koordinata ates edildiginde matrix uzerinde degisiklikler yapiliyor.
        if (korx,kory) in self.atis_yapilmis_noktalar:
            return "Buraya daha once top atisi yaptiniz!"

        elif (korx,kory,1) in self.gemi_noktalari:#eger ates edilen yerde bir gemi varsa
            self.matrix[kory-1][korx-1]="x "
            self.gemi_noktalari.remove((korx,kory,1))
            self.atis_hakki -= 1
            self.atis_yapilmis_noktalar.append((korx, kory))
            return "Tebrikler bir gemiyi vurdunuz!\nKalan atis hakkiniz:{}".format(self.atis_hakki)



        elif (korx,kory,0) in self.gemi_noktalari:
            self.matrix[kory - 1][korx - 1] = "x "
            self.gemi_noktalari.remove((korx, kory,0))
            self.atis_hakki -= 1
            self.atis_yapilmis_noktalar.append((korx,kory))
            return "Tebrikler bir gemiyi vurdunuz!\nKalan atis hakkiniz:{}".format(self.atis_hakki)


        else:
            self.matrix[kory-1][korx-1]="* "
            self.atis_hakki -= 1
            self.atis_yapilmis_noktalar.append((korx, kory))
            return "Opss..Attigin top mermisi suya dustu!\nKalan atis hakkiniz:{}".format(self.atis_hakki)


def main():
    dongu=True
    puan=0
    while dongu:
        def ayarlar():
            print("*" * 15 + "Amiral batti oyununa hosgeldiniz!" + "*" * 15 + "\n\n"
                  "2 cesit oyun modu mevcut.\n\nAcik mod-)Haritada gemilerin nerede oldugunu gorebilirsiniz."
                  "\nGizli mod-)Haritanin her yeri kapalidir ve gemilerin nerede oldugunu goremezsiniz.\n\n"
                  "Toplamda size haritanin 3'de 1'i kadar atis hakki verilecek." + "\n" +
                  "-" * 15 + "Hazirsan baslayalim!" + "-" * 15 + "\n\n\n")
            hazir=False
            while not hazir:
                try:
                    oyun_modu = int(input("Oyun modunuzu secme vakti geldi.Acik mod icin 0,Kapali mod icin 1 girin."))
                    harita_boy = int(input("Oynayacaginiz haritanin uzunlugunu tamsayi olarak girin:"))
                    gemi_say = int(input("Haritadaki gemi sayisini tamsayi olarak girin:"))
                    harita_ = Harita(harita_boy, harita_boy, oyun_modu)
                    oyun_ = Isleme(harita_=harita_, gemi_sayisi=gemi_say, gizli_mod=bool(oyun_modu))
                    hazir=True
                    return oyun_
                except Exception as e:
                    print("Lutfen degerleri olmasi gerektigi gibi girin!")


        oyun=ayarlar()
        oyun.render_map()
        devam=True
        cevap=False
        atisa_devam_mi=True
        while devam:  # Oyun dongusu
            if not oyun.gemi_noktalari:#butun gemiler batirildiysa
                puan+=oyun.atis_hakki
                cevap=False
                while True:
                    devam_mi=str(input("Tebrikler amiral tum gemileri batirdiniz!\nTekrar oynamak istiyor musunuz?(E/H)"))
                    if devam_mi.lower()=="e":
                        dongu=True
                        cevap=True
                        print(f"Yeni oyuna gecis yapiliyor...Kazandiginiz puan={puan}")
                        break

                    elif devam_mi.lower()=="h":
                        dongu=False
                        cevap=True
                        print(f"Oyundan cikis yapiliyor...Toplam puaniniz={puan}")
                        break

                    else:
                        print("Gecersiz bir cevap yolladiniz!Tekrar girin.")

            if cevap:
                break

            try:#ates etmenin gerceklestigi kisim
                ates_noktasi = str(input("Ates edeceginiz koordinat(x y):"))
                ates_x = int(ates_noktasi.split(" ")[0])
                ates_y = int(ates_noktasi.split(" ")[1])
                assert ates_x in range(11) and ates_y in range(11)
                if oyun.atis_hakki>0:
                    sonuc=oyun.ates(ates_x, ates_y)
                if oyun.atis_hakki<=0:
                    atisa_devam_mi=False
                print("\n"*50)
                oyun.render_map()
                print(sonuc)
            except AssertionError as e:
                print("Koordinatlar 1 ile 10 arasinda olmadilir!")

            except ValueError as e:
                print("Lutfen girdiginiz koordinatin sayi oldugundan emin olun!")

            except IndexError as e:
                print("Lutfen girdiginiz koordinatin ornekteki gibi oldugundan emin olun!"
                      "\nOrnekler:\n3 5\n4 7\n6 1")

            if not atisa_devam_mi:#atis hakki bittiginde islenecek kisim.
                while True:
                    print("Atis hakkiniz bitti amiral...\n")
                    devam_mi = str(input("Tekrar oynamak istiyor musunuz?(E/H)"))
                    if devam_mi.lower() == "e":
                        dongu = True
                        print(f"Yeni oyuna gecis yapiliyor...Kazandiginiz puan={puan}")
                        break

                    elif devam_mi.lower() == "h":
                        dongu = False
                        print(f"Oyundan cikis yapiliyor...Toplam puaniniz={puan}")
                        break

                    else:
                        print("Gecersiz bir cevap yolladiniz!Tekrar girin.")

            if not dongu:
                break

if __name__ == '__main__':
    main()