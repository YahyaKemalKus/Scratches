import numpy as np
def max_matris(matris_,n):
    try:
        matris_ = [int(i) for i in matris_.split(",")]
        print("\nMatrisin goruntusu\n", np.array(matris_).reshape(n, n))
        matris_ = [matris_[x:x + n] for x in range(0, len(matris_), n)]
        caprazlar=[[] for i in range(n*2-1)]#her bir capraz icin liste icine listeler olusturuluyor.
        toplamlar=[]#
        for x in range(n):#her bir x ve y koordinati aliniyor
            for y in range(n):
                caprazlar[x+y].append(matris_[x][y])#x ve y koordinatlari toplamindaki indexe (x,y) koordinatindaki sayi ekleniyor.(capraz sayilarin x+y'leri esit oluyor)
        for sayilar in caprazlar:#capraz sayilarin toplamlari bulunuyor.
            toplam=0
            for sayi in sayilar:
                toplam+=sayi
            toplamlar.append(toplam)
        return "\n\nCapraz en buyuk toplam:"+str(max(toplamlar)) #en yuksek deger donduruluyor

    except Exception:
        print("Lutfen NxN bir matris girin!")

N=int(input("N degerini girin:"))
matris=input("Matrisi girin:")#matris 5,7,1,3,4.... seklinde giriliyor.
print(max_matris(matris,N))

"""
N degerini girin:2
Matrisi girin:2,2,2,2

Matrisin goruntusu
 [[2 2]
 [2 2]]


Capraz en buyuk toplam:4
"""