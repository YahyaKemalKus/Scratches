while True:
    try:#yanlis sekilde girildiginde hata verip kapanmasi yerine uyari verip dongunun devam etmesini sagliyoruz.

        aralik=str(input("(orn:5-100)\nAralik giriniz:"))#kullanicidan aralik aliyoruz.
        baslangic=int(aralik.split("-")[0])#alinmis olan string halindeki araligi "-" isaretine gore boluyoruz
        bitis=int(aralik.split("-")[1])#bolundukten sonra ortaya cikan ilk sayi baslangic sayisi,ikinci sayi bitis sayisi olarak int halinde degiskenlere ataniyor.
        asal_sayi_sayisi=0
        for sayi in range(baslangic, bitis + 1):#verdigimiz araliktaki sayilar teker teker bu for dongusunden asagiya kontrole yollaniyor.

            bolen_sayisi = 0#burada bolen sayi sayisini 0'a esitlemezsek her yeni sayi geldiginde,onceden kalan bolen sayi sayilari da dahil olur ve calismaz.

            for bolen in range(2,sayi+1):#bu dongude yukardan yollanan sayinin kac tane boleni oldugu kontrol ediliyor.
                if sayi%bolen==0:# "%" isareti mod olarak kullaniliyor ve bize kalani veriyor.kalan 0 kosulu sayi tam bolunuyor demektir.
                    bolen_sayisi+=1#yukardaki kosul saglandiginda bolen sayisi bolen sayi sayisi 1 artiyor.

            if bolen_sayisi==1:#yukardaki kontrolden gectikten sonra sadece 1 adet boleni varsa(bu da kendisi oluyor) asal kosulu saglanmis oluyor.
                print("{} asaldir.".format(sayi))
                asal_sayi_sayisi+=1

        print("Aralikta toplam {} asal sayi vardir.".format(asal_sayi_sayisi))

    except ValueError:#try komutunun tamalayicisidir.ValueError(deger hatasi) alindiginda ne yapilacagini altina yaziyoruz.
        print("Lutfen ornekteki gibi giriniz!")

