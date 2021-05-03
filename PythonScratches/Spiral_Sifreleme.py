import numpy  as np
from math import sqrt

def crypto(kelime,islem):#uzunlugu tamkare olan mesaji sifreler veya cozer.
    try:#eger mesajin uzunlugu tamkare olmazsa ekrana duzgun girilmesi icin print atiyor.
        taban=int(sqrt(len(kelime)))#girilen mesajin uzunlugunun taban degerinin degiskeni
        matris1 = np.array([*kelime]).reshape(taban, taban)#(taban,taban) buyuklugunde matris degiskeni
        matris2=np.arange(1,len(kelime)+1).reshape(taban,taban)#indexlerin alinmasi icin olusturulan sayilardan olusan NxN matris
        crypted = list()#matriste spiral atilarak elde edilen harflerin listesi
        decrypted_index=list()#spiral atildiginda olusan sayi sirasini iceren liste
        decrypted_char=[*range(len(kelime))]#indexlerine gore harflerin atilacagi liste


        if islem=="sifrele":
            while matris1.size:  # matrisde eleman oldukca donen dongu
                crypted.append(matris1.T[0])  # matris saat yonunde donduruldugunde elde edilen yeni matrisin ilk satiri sifre listesine ekleniyor
                matris1 = matris1.T[1:].T[::-1].T  # matrisi donguye tekrar girmeden once tekrar sekillendiriyor.(Spiralin devam satiri tekrar elde edilecek sekilde)

            return "".join(np.concatenate(crypted))#sifre harflerinin oldugu liste(numpy array tipinde veriler) normal liste haline getiriliyor ve  join fonksiyonu
                                                    #ile string halinde donduruluyor.

        if islem=="coz":
            while matris2.size:
                [decrypted_index.append(i-1) for i in [*matris2.T[0]]]#yukarda yapilan islem gibi ancak harfler yerine sayilar var.Spiral atildiginda ortaya cikan
                matris2 = matris2.T[1:].T[::-1].T                                                  #sayi duzenini listeliyor.Ortaya cikan liste indexlerin listesi oluyor.


            for index,harf in zip(decrypted_index,[*kelime]):#Sifrelenmis mesajdaki harfleri yukardan gelen index listesine gore indexlerine yerlestiriyor.
                decrypted_char[index]=harf

            return "".join(decrypted_char)#sifresi cozulmus(indexlerine gore listeye yerlestirilen harfler) join fonksiyonu ile string halinde donduruluyor.

    except Exception:
        print("Lutfen uzunlugu tam kare olan bir mesaj girin!")


mesaj=input("sifrelenecek mesaji girin:")
print("mesaj sifrelendi:",crypto(mesaj,"sifrele"))
sifreli=input("sifresi cozulecek mesaji girin:")
print("sifre cozuldu:",crypto(sifreli,"coz"))