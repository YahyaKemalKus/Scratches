from itertools import combinations_with_replacement
from itertools import product

def XoR_DeCrypter(hex_str,key_size):#yuksek derece brute force icerir.Cok zorda kalmadikca kullanmamak daha iyi.Fazla yavas.
    crypted=bytes.fromhex(hex_str)
    for i in combinations_with_replacement([*range(256)], key_size):#anahtarlar verilen uzunluga gore uretiliyor.
        key=[*i * int(len(crypted)/key_size+1)]
        decrypted="".join([chr(x^y) for x,y in zip(key,crypted)]).split(" ")#sifreli metin anahtara gore cozuluyor.kelime kelime ayriliyor.
        sayac=0
        for k in decrypted:
            if all(map(lambda x:ord(x) in [*range(39,91),*range(97,123),10,33,34],k)):#ortaya cikan cozulmus metnin kelimeleri kontrolden geciriyor.
               sayac+=1
        if sayac==len(decrypted)and " ".join(decrypted).count("\n")<len(decrypted):#eger cozulmus metnin butun kelimeleri
            print(" ".join(decrypted),"Anahtar:" ,"".join(map(chr, i)))            #alfabetikse ve kelime basina asagi satira gecmiyorsa ekrana yaziyor.


def XoR_DeCrypter_Fast(hex_str,max_key_size):#Sonradan yazdigim bu algoritma sifre uzunluk tahmini yaparak daha hizli cozuyor.Teker teker sifredeki harfleri buluyor.
    """Asagadaki kodun calisma mantigi sifre uzunlugu uzerinden geliyor.1'den baslayarak verilen maximum uzunluga kadar teker teker deniyor.
       Aldigi sifre uzunlugunu 5 varsayalim.Sifrelenmis metinden sirasiyla 1-6-11-16... indexli karakterleri aliyor ve hepsini sirayla decrypt ediyor.
       (decryption degerlerinde aldigi aralik 0-255).Eger herhangi bir decryption degerinde alinan karakterler alfabetik hale geliyorsa
       decryption degerini olasilik listesinin ilk listesine ekliyor.Daha sonra sifrenin 2. harfine geciliyor.Bu sefer 2-7-12-17... indexli karakterleri aliyor.
       Ayni islemi yapiyor ve olasi degerleri olasilik listesinin 2.listesine ekliyor.Bu sekilde max_key_size parametresine verilen degere kadar deniyor.
       Olasilik listesinde sifre uzunlugu kadar liste bulunuyor.Her bir liste sifrenin bir indexini kapsiyor.Olasi butun decryption degerleri
       listelendikten sonra bu listelerin kombinasyonlari aliniyor.Muhtemel butun sifreler ekrana yazdiriliyor. """
    bulundu=False
    for key_size in range(1,max_key_size):
         olasilik=[[] for i in range(key_size)]
         for konum in range(key_size):
             crypted=bytes.fromhex(hex_str)[konum::key_size]
             for i in range(256):
                 decrypted = "".join([chr(x ^ i) for x in crypted])
                 if all(map(lambda x: ord(x) in [*range(39, 91), *range(97, 123), 10, 32,33, 34],[*decrypted])):
                        #if i in [*range(65, 91), *range(97, 123)]:#Sifrenin de alfabetik olup olmadigini kontrol ediyor.
                            olasilik[konum].append(chr(i))

         if not olasilik[key_size-1]:continue

         print(olasilik)
         for i in product(*olasilik):
            print("Bulunan Tahmini Anahtar:","".join(i))
            print("Anahatara gore cozulen veri:","".join(i))
            print("sifrelenmis hex string:",hex_str)
            print("Decryted mesaj: ", end="")
            for i in hex_to_str(hex_str):
                print(chr(ord(i)^ord('5')),end="")

            bulundu=True
         if bulundu:break

def XoR_Crypter(mesaj,key,crypted_type):
    key=[*key * int(len(mesaj)/len(key)+1)]#anahtar mesaj uzunluguyla ayni olana kadar tekrar ediliyor.
    crypted = "".join([chr(ord(x) ^ ord(y)) for x, y in zip(mesaj, key)])#verilen metin anahtara gore sifreleniyor ve string haline getiriliyor
    if crypted_type=="hex":
        hexa_str=[*map(lambda x:hex(ord(x))[2:] if len(hex(ord(x))[2:])==2 else "0"+hex(ord(x))[2:],crypted)]#hexadecimal metni haline getiriliyor
        return "".join(hexa_str)
    if crypted_type=="str":
        return crypted

def hex_to_str(hex):
    x = 0;y = 2
    kelime = ""
    while True:
        hexy = hex[x:y]
        kelime += chr(int(hexy, 16))
        if y == len(hex):break
        x += 2;y += 2
    return kelime