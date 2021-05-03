print(*enumerate("yahya"))#yahya'nin her bir harfini numaralar.
liste=[3,5,6,7,8]
def tek(sayı):
    return sayı%2==1
print(*filter(tek,liste))#Listeyi tek fonksiyonuna göre filtreler.


def en_yüksek_rütbe(rütbe):
    rütbeler = {'er'        : 0,
                'onbaşı'    : 1,
                'çavuş'     : 2,
                'asteğmen'  : 3,
                'teğmen'    : 4,
                'üsteğmen'  : 5,
                'yüzbaşı'   : 6,
                'binbaşı'   : 7,
                'yarbay'    : 8,
                'albay'     : 9}

    return rütbeler[rütbe]

askerler = {'ahmet': 'onbaşı',
            'mehmet': 'teğmen',
            'ali': 'yüzbaşı',
            'cevat': 'albay',
            'berkay': 'üsteğmen',
            'mahmut': 'binbaşı'}
for k, v in askerler.items():
    if askerler[k] in max(askerler.values(), key=en_yüksek_rütbe):#En yüksek rütbeyi verir.
        print(k,v )

for  k,v in askerler.items():
    if askerler[k]==min(askerler.values(),key=en_yüksek_rütbe):#En düşük rütbeyi bulur.
        print(k,v)
print(open("dene.mp3").fileno())#dosyanın tanımlayıcı bilgisini verir

print(pow(2,5))#ilk sayı üstü alınacak sayıdır.ikincci sayı ise kuvvetidir.

print("yahya","kemal",file=open("boolean.txt","a"),flush=True,sep="aa",end="yeaa")#ilk başa yazılacaklar yazılır.file komutu nereye
#yazılacağını belirler.flush değeri ise önce bilgilerin önce tampona alınıp sonra mı yazılacağını yoksa direk mi yazılac
#ağını belirler flush değeri True ise direk yazar.False ise önce tampona alır.Sep ise değerlerin arasına yazılacak şeyi seçer.end ise
#en sona ne yazılacağını belirler
isimler=["yahya","kemal","kus"]
print(list(range(1,10)))#liste halinde aralıktaki sayıları yazar.
print(tuple(range(1,10)))#demet halinde aralıktaki sayıları yazar.
print(set(range(1,10)))#küme halinde aralıktaki sayıları yazar.
print(frozenset(range(1,10)))#dondurulmuş küme halinde aralıktaki sayıları yazar.
for i in range(0,10,2):#0'dan başlayıp 2şer artarak aralıktaki sayıları yazar.
    print(i)
print(list(range(0,10,2)))#liste halinde 2şer  artan sayilari yazar.
print(*reversed(isimler))#listeyi tersten yazar.
print(isimler[::-1])#liste halinde listeyi tersten yazar.
print(list(reversed(isimler)))#liste halinde listeyi tersten yazar.
print(sorted("yahya"))#alfabe sırasına göre liste halinde yazar.sorted'in başına * koyarsak listedeki elemanları yazar.
import locale
locale.setlocale(locale.LC_ALL,"Turkish_Turkey.1254")#Türkçe modülü aktif eder.
print(*sorted([6,3,8,1,10]))#küçükten büyüğe sıralar.
print(*reversed(sorted([6,3,8,1,10])))#reserved ile büyükten küçüğe sıralar.
print(isimler[::2])#listeyi 2 şer atlayarak yazar.
print(*zip(isimler,[1,2,3,4]))#liste elemanlarını birbiriyle eşleştirir.
print(*map(lambda sayi:sayi**2,[2,3,4]))#lambda def gibidir ama olduğu yerde tanımlanabilir.
birlestir = lambda ifade, birlestirici: birlestirici.join(ifade.split())
print(birlestir("yahya kemal kuş","+"))
import random
liste1=[random.randint(1,10000) for i in range(1,10)]#1-10000 aralığında 9 sayı seçtik
print(liste1)
import os
print(os.name)#işletim sisteminin adını verir.nt ise windows kullanıcları içindir.posix ise mac kullanıcıları içindir.
print(os.getcwd())#bulunulan dizini verir.
#os.makedirs("deneme")#bulunulan dizine yeni klasör açar
#import modül adı as yeniadı komutu modüllerin ismini değiştirmemizi sağlar.
import webbrowser as web
#web.open("www.google.com.tr")#websitesini açmayı sağlar
import sys
print(sys.version)#kullanılan python sürüm bilgilerini verir.
print(random.__file__)#modülün kaynak dosyasının yerini gösterir.
print(sys.path)#modülleri nerelerde aradığını gösterir.
print(*map(lambda x : x**2,[3,5]))# for x in [3,5]: print(x**2)
print(*map(lambda x:x**2,[*range(3,5)]))


def azalt(n):# baştan 1 er harf silerek printler.
    if len(n)<1:
        print("bitti")
    else:
        print(n)
        return azalt(n[1:])
azalt("yahya")
#max icmp paketi yollama byte boyutu 1472

#\r satır başı komutudur.Bulunduğu yerden sonrasını en başa alır.
#\v düşey sekme komutudur.Alt satıra geçip aynı konumdan yazar.
#\t tab tuşuna basılmış gibi 4 boşluk atıyor.
#\n alt satıra geçme komutu.
#\b bir birim sola kaydırma komutu.


if isinstance("3",str):# 1.parametreye girilen değer 2.parametrenin bir örneği mi diye kontrol eder .
    print("\"3\" bir str() uyesidir")

#os.system(komut) ile konsolda komut çalıştırılır.
s="adasd"
XOR=[chr(ord(i)^15) for i in s]#tek sayiya gore xor sifreleme.
isimler.append("kus")#listenin sonuna "kus" elemanini ekler.
isimler.insert(1,"developer")#listenin 1. indexine "developer" elemanini ekler.Index secme avantaji var.
kelime="asdasd"
[print("".join([chr(ord(x)^y) for x in kelime])) for y in range(128)]#kelimeyi 0-128 arasindaki sayilarla teker teker xorlayip yazdiriyor.


#########
class Bum:
    @classmethod
    def dnm(cls):print("Bum.dnm() yazilarak direk cagrilabilir")

    def dnm2(self):print("sinifin bir uyesinden cagirilabilir")
########


###########################################
def aralikr(rng):
    n=0
    liste=[]
    while n<=rng:
        liste.append(n)
        n+=1
    return liste


def araliky(rng):
    n=0
    while n<=rng:
        yield n
        n+=1


for sayi in aralikr(1000000000000):#aralikr fonksiyonu return kullandigi icin butun liste tamamlanana kadar for dongusune girilmez.
    # eger returnu while dongusunun icine yazarsam direk fonksiyon orada ciktilar ve durur.Yuksek sayili bir parametre verildiginde uzun sure beklemek gerekebilir.
    #hafizada fazla kullanim ve belli sure beklemeyi gerektirir.
    print(sayi)

for sayi in araliky(10e1000):#yield sayesinde deger geldikce onu disari aktarir.Hafizada yer kaplamaya yol acmaz.Biriktirme yapmaz,geleni disari aktarir.
                                            #yield bir generator expressions fonksiyonudur.
    print(sayi)

#############################################

kaynak = "şçöğüıŞÇÖĞÜİ"
hedef  = "scoguiSCOGUI"
silinecek="ABC"
ceviri_tablosu = str.maketrans(kaynak, hedef,silinecek)
print("şaAğBC".translate(ceviri_tablosu))#translate'e parametre olarak verilen tabloya gore ceviri yapiyor.


liste1=[1,2,3,4,5,6]
kume1=set(liste1)
liste2=[5,6,7,8,9]
kume2=set(liste2)
print("kumelerin kesisimi",kume1&kume2)
print("kume1-kume2",kume1-kume2)

a=[3,4,5,6,7,8]
for i in enumerate(a,0):
    a[i[0]]=0 if i[1]<=5 else 5  #kisa sekilde listede kosula gore deger degistirme



from collections import Counter,OrderedDict,defaultdict,ChainMap


Counter(['B', 'B', 'A', 'B', 'C', 'A', 'B','B', 'A', 'C'])#listenin eleman sayilarinin sozlugunu olusturma
Counter({'A': 3, 'B': 5, 'C': 2})
Counter(A=3, B=5, C=2)



coun = Counter()
coun.update([1, 2, 3, 1, 2, 1, 1, 2]) # coun isimli sayaca eleman ekleme
coun.update([1, 2, 4])



c1 = Counter(A=4, B=3, C=10)          #counter sozlugu olusturma
c2 = Counter(A=10, B=3, C=4)
c1.subtract(c2)                       #c1 sozlugunden c2'yi cikarma


z = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']
Counter(z) ##listenin eleman sayilarinin sozlugunu olusturma



od = OrderedDict() #sirali sozluk olusturma
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4



dc = defaultdict(int)    #degerleri(value) integerlardan olusan bos bir sozluk olusturma
L = [1, 2, 3, 4, 2, 4, 1, 2]
for i in L:             #listedeki anahtarlardan kacar tane oldugunu bulmak icin dongu
    dc[i] += 1           #sayilarin default value'leri 0 oldugundan direk ekleme yapabiliyoruz.



d = defaultdict(list)  #degerleri listelerden olusan bos bir sozluk olusturma
for i in range(5):
    d[i].append(i)
    d[i].append(i+1)
    d[i].append(i+2)



def def_value():
    return "Value is missing"

dct = defaultdict(lambda :"Value is missing") #__missing__ calistiginda calisacak fonksiyon/return degeri
#dct = defaultdict(def_value) #lambda ile ayni
dct["a"] = 1
#print(dct["b"])
#print(dct["c"])



dic1 = {'a': 1, 'b': 2}
dic2 = {'b': 3, 'c': 4}
dic3 = {'f': 5}


chain = ChainMap(dic1, dic2) #chainmap olusturma
chain1 = chain.new_child(dic3)#chainmape yeni sozluk ekleme
