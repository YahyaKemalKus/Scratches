from itertools import combinations
import numpy as np
def max_L(matris_,n,m):
    try:
        matris_=[int(i) for i in matris_.split(",")]
        print("\nMatrisin goruntusu\n",np.array(matris_).reshape(n,m))
        matris_=[matris_[x:x+m] for x in range(0,len(matris_),m)]#inputtan gelen string veri matris listesi haline donusturuluyor.
        uclu_kords=[]
        carpimlar=[]
        for x in range(n-1):
            for y in range(m-1):
                    dortlu_kords=combinations([[x,y],[x+1,y],[x,y+1],[x+1,y+1]],3)#2x2 seklinde 4 nokta aliniyor daha sonra 3lu kombinasyonlari aliniyor
                    uclu_kords.append([*dortlu_kords])                                          #bu sekilde 'L' sekli elde edilmis oluyor.

        for h in uclu_kords:#Alinan 3'lu koordinatlarin matrisdeki degerleri carpilip carpimlar listesine ekleniyor.
            for i in h:
                carpim=1
                for y in i:
                    carpim*=int(matris_[y[0]][y[1]])
                carpimlar.append(carpim)

        return "\n\nEn buyuk carpim:"+str(max(carpimlar))#carpimlar arasindan en yuksek olan deger donduruluyor

    except Exception:
        print("Lutfen matrisi ve boyutu dogru girin!")

N=int(input("N degerini girin:"))
M=int(input("M degerini girin:"))
matris=input("Matrisi girin:")#matris 5,7,1,3,4.... seklinde giriliyor.
print(max_L(matris, N, M))
