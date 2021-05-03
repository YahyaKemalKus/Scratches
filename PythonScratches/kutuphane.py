def hexstr_to_int(hex_string):
    assert len(hex_string)%2==0,"Verilen hex dizisini tam girdiginize emin olun"

    ints=(int(hex_string[x:x+2],16) for x in range(0,len(hex_string),2))
    return [*ints]



def str_to_list(string,uzunluk):
    assert isinstance(string,str) and isinstance(uzunluk,int),"Parametre degerleri yanlis"

    liste=(string[x:x+uzunluk] for x in range(0,len(string),uzunluk))
    return [*liste]



class Kombinasyon:

    @staticmethod
    def taban(sayi, sistem):
        ust = 0
        basamaklar = []
        basamak_degerleri = []
        while sayi:

            if pow(sistem, ust) > sayi:
                en_buyuk_ust = ust - 1
                en_buyuk_ustlu_sayi = pow(sistem, en_buyuk_ust)
                basamak_degeri = int(sayi / en_buyuk_ustlu_sayi)
                sayi -= basamak_degeri * en_buyuk_ustlu_sayi
                basamaklar.append(en_buyuk_ust)
                basamak_degerleri.append(basamak_degeri)
                ust = 0
            else:
                ust += 1

        taban_cikti = [0 for t in range(sistem + 1)]
        for basamak, deger in zip(basamaklar, basamak_degerleri):
            taban_cikti[basamak] = deger

        return taban_cikti[::-1]


    @staticmethod
    def max_taban(sistem, basamak_say):
        max_sayi = 0
        for ust in range(basamak_say):
            max_sayi += pow(sistem, ust) * (sistem - 1)

        return max_sayi


    @staticmethod
    def kombinasyon(liste, komb_el_say): #alt alta for atmadan listedeki butun elemanlarin verilen uzunluktaki
        el_say = len(liste)              #kombinasyonlarini donduruyor.yield sayesinde anlik islemden gecebiliyor.
        cikti = ""                       #[print(komb) for komb in kombinasyon(array,eleman_sayisi)] gibi
        range_ = Kombinasyon.max_taban(el_say, komb_el_say) + 1
        taban_ = Kombinasyon.taban
        for sayi_ in range(range_):
            for index in taban_(sayi_, el_say)[el_say - komb_el_say+1:]:
                cikti += str(liste[index])+","
            yield cikti
            cikti = ""