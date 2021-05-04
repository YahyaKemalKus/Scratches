def tabanx(sayi, taban, sonuc = None):
    p = 0
    while True:
        if taban ** p > sayi:
            katsayi = divmod(sayi, taban ** (p - 1))[0]
            sayi -= taban **( p-1) * katsayi
            if not sonuc:
                sonuc = [* "0" * p]
            sonuc[-p] = str(katsayi)
            if sayi == 0:
                return "".join(sonuc) #sonucu string olarak dondurur
            return tabanx(sayi, taban, sonuc)
        p += 1
