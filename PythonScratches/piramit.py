def kum_saati(yukseklik,klm):
    for i in range(-yukseklik,yukseklik+1):
        i=abs(i)
        print(f"{klm*i}".rjust(yukseklik*len(klm))+klm+klm*i)

def piramit(yukseklik,klm):
    print(klm.rjust((yukseklik+1)*len(klm)))
    for i in range(1,yukseklik):
        i=abs(i)
        print(f"{klm*i}".rjust(yukseklik*len(klm))+klm+klm*i)

kum_saati(20,"|")
