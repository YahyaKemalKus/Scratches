import re
#2 tas kacamayacak durumdaysa eklenicek--eklendi
#printlerde duzenleme yapilacak--yapildi
#Rakip 2 tasi ayni anda tehdit edebilecek hamle yapabiliyorsa ondecen bu ihtimal kaldirilicak
#en fazla goruste 2 tane en yuksek deger varsa siyahin gorusunun en az oldugu secilecek
#beyazin kacarken veya normal oynarken yapabilecegi karli hamle yoksa en fazla gorus aldigi ve tehlikeye girmedigi yere gidiyor.
#gorus almaya mantikli baska bir secicilik daha eklenecek.EKLENDI--gittigi yerde korunmasiz siyah tas tehdit edebiliyorsa
#ve gidince siyah tarafindan yenmiyorsa ilk o hamleyi tercih ediyor.en fazla tasi tehdit edebildigi yer oncelikli
#1.gun taslarin nerelere gidebilecegini bulan algoritma eklendi
#2.gun 3 hamle icindeki tum olasiliklari bulan algoritma eklendi
#3.gun 3 hamle icindeki tum olasiliklardan takas olasiliklari eklendi--Beyaz yer,Siyah yer,Beyaz yerse veya
#beyaz yiyemez,siyah yer,beyaz yerse veya beyaz yer,siyah yer,beyaz yiyemezse veya beyaz direk yer ve siyah yiyemezse.
#4.gun 3 hamle olasiliklarinda duzenleme yapildi.ard arda 3 tas yenirse 4. hamleye de bakiyor.0-b-s olasiligi kaldirildi.
#Yanlis hesaplamalar bulundu duzeltildi.3 hamle icinde karli cikilabilecek ihtimal yoksa ve kacacak tas yoksa
#takima en fazla gorus saglanan noktaya gitme eklendi.
#Kacmasi gereken tasin kactigi noktada guvende olmayan bir tasi tehdit edebilme algoritmasi eklendi.En fazla tasi tehdit edebildigi yeri seciyor.
#Kacmasi gereken tas tehdit edemiyorsa takimina en fazla gorus saglayabildigi noktaya gitmesini saglayan algoritma eklendi.
#Kacmasi gereken tas kacamiyorsa en fazla gorus saglanan baska bir tas oynama algoritmasi eklendi
#Guvende olmayan tas varsa onu yeme algoritmasi eklendi-(sadece ilk hamleye bakiyor)
#Piyon 2li giderken onundeki tasin ustunden atlamasi duzeltildi.
#5.gun kacmasi gereken tas varsa ve kacamiyorsa baska bir tasin en fazla gorusu alacak sekilde oynamasi yerine
#kacamayan tasi tehdit eden tasi yiyip degerli tasi kurtarabilecek fedakarlik algoritmasi eklendi.yani beyaz vezir karsi piyon tarafindan
#sikistirilmissa ve kacamiyorsa,bu piyonu yiyebilecek vezirden degersiz olan bir beyaz tas kendini feda edip veziri bu durumdan kurtariyor.
#Guvende olmayan tas yeme algoritmasinda duzenleme yapildi ve yedikten sonraki durumda herhangi bir tas onu yiyebiliyor mu ona bakiyor.(2hamle ilerisi)
#sadece ilk hamleye bakildiginda tas beles gibi algilaniyordu ve yedikten sonra yeni olusan durumda yenebiliyordu.Artik yedikten sonra ki
#duruma gore bakiliyor ve saglikli sekilde beles yeniyor mu kontrol ediyor.beles=kayip vermeden yeme
#Rakip piyonun duz gittigi yerlerin de tehlikeli konum olarak algilanmasi duzeltildi.Sadece capraz gittigi yerler tehlikeli olarak algilaniyor.
#Eger bir tas kacamiyorsa onune gecebilecek degersiz tas hamle algoritmasi eklendi-oncelikli hamle
#piyonun duz gittikten sonra tehdit olusturma algoritmasi eklendi
#kacmasi gereken tas kactigi yerde korunmasiz siyahi tehdit edebiliyorsa once oraya gitme algoritmasi eklendi.tehdit edemiyorsa en fazla gorus aldigi yere gidiyor.
#fedakarlik algortimasinda duzeltme yapildi-kacamayan tasi tehdit eden tas guvende degilse yiyebilen/fedakar bir tas tarafindan yeniyor

#TODO sah cekme algoritmasi eklenecek.Siyahlarin kazanma algoritmasi eklenecek.Beyazlarin sahi yense bile oyun devam ediyor!
Beyazlar={"b_kale1":[1,1],"b_at1":[2,1],"b_fil1":[3,1],"b_vezir1":[5,1],"b_SAH1":[4,1],
                 "b_fil2":[6,1],"b_at2":[7,1],"b_kale2":[8,1],"b_piyon1":[1,2],"b_piyon2":[2,2],
                 "b_piyon3":[3,2],"b_piyon4":[4,2],"b_piyon5":[5,2],"b_piyon6":[6,2],
                 "b_piyon7":[7,2],"b_piyon8":[8,2]}

Siyahlar={"s_kale1":[1,8],"s_at1":[2,8],"s_fil1":[3,8],"s_vezir1":[5,8],"s_SAH1":[4,8],
                 "s_fil2":[6,8],"s_at2":[7,8],"s_kale2":[8,8],"s_piyon1":[1,7],"s_piyon2":[2,7],
                 "s_piyon3":[3,7],"s_piyon4":[4,7],"s_piyon5":[5,7],"s_piyon6":[6,7],
                 "s_piyon7":[7,7],"s_piyon8":[8,7]}

#Beyazlar={"b_kale1":[1,1],"b_SAH1":[5,1],"b_piyon1":[1,2],"b_vezir1":[7,1]}
#Siyahlar={"s_at1":[1,3],"s_SAH1":[8,8]}
Tas_degerleri={"piyon":1,"at":3,"fil":3,"kale":5,"vezir":9,"SAH":100}
def yol_kontrol1(tas,beyazlar,siyahlar):#Gorusler kendi taslarini da kapsar
    taslar=None
    vezir=[]
    yok_etme=False
    b=1
    Tum_taslar = siyahlar.copy()
    Tum_taslar.update(beyazlar)
    if re.search("b_", tas):
        taslar = beyazlar

    if re.search("s_",tas):
        taslar = siyahlar

    if re.search("kale",tas) or re.search("vezir",tas) :

        korx,kory=None,None
        for y in [0,1]:
            dolular = sorted([k[y] for i, k in Tum_taslar.items() if taslar[tas][b] == k[b]])
            liste_konum = dolular.index(taslar[tas][y])

            if len(dolular) == 1:#yatay-dikey koridorda kale tek ise
                gidilebilecek = [i for i in range(1, 9) if i != taslar[tas][y]]

            elif max(dolular) == taslar[tas][y]:#yatay-dikey koridorda en yuksek konumdaysa
                gidilebilecek = [i for i in range(dolular[liste_konum - 1] , 9) if i != taslar[tas][y]]

            elif min(dolular) == taslar[tas][y]:#yatay-dikey koridorda en dusuk konumdaysa
                gidilebilecek = [i for i in range(1, dolular[liste_konum + 1]+1) if i != taslar[tas][y]]

            else:#yatay-dikey koridorda 3 veya daha fazla tas var ise
                gidilebilecek = [i for i in range(dolular[liste_konum - 1] , dolular[liste_konum + 1]+1) if i!= taslar[tas][y]]



            if y==0:
                    korx = [[i,taslar[tas][b]] for i in gidilebilecek]
            if y==1:
                    kory = [[taslar[tas][b], i] for i in gidilebilecek]

            b =0
        if re.search("vezir",tas):
            vezir+=[*korx,*kory]

        if re.search("kale",tas):
            return [*korx,*kory]

    if re.search("fil",tas) or re.search("vezir",tas) :
        bosluk1,bosluk2,bosluk3,bosluk4=True,True,True,True
        tas_x,tas_y=taslar[tas]
        dolular=[[],[],[],[]]
        gidilebilecek=[]

        for y in range(1,8):
            if [tas_x+y,tas_y+y] in Tum_taslar.values() and len(dolular[0])==0:#sag ust dost tas varsa---
                if [tas_x+y,tas_y+y] in taslar.values():
                    belirtec1=1
                else:
                    belirtec1=1
                korx=[x for x in range(tas_x+1,tas_x+y+belirtec1)]
                kory=[a for a in range(tas_y+1,tas_y+y+belirtec1)]
                if korx:
                    dolular[0].append("belirlendi")
                    gidilebilecek.append([[a,b] for a,b in zip(korx,kory)])
                if not korx:
                    bosluk1=False
            if [tas_x+y,tas_y-y] in Tum_taslar.values() and len(dolular[1])==0:#sag altta dost tas varsa---
                if [tas_x+y,tas_y-y] in taslar.values():
                    belirtec1=0
                    belirtec2=1
                else:
                    belirtec1=0
                    belirtec2=1
                korx=[x for x in range(tas_x+1,tas_x+y+belirtec2)]
                kory=[y for y in range(tas_y-y+belirtec1,tas_y)]
                if korx:
                    dolular[1].append("belirlendi")
                    gidilebilecek.append([[a,b] for a,b in zip(korx,reversed(kory))])
                if not korx:
                    bosluk2=False

            if [tas_x-y,tas_y-y] in Tum_taslar.values() and len(dolular[2])==0: #sol altta tas varsa---
                if [tas_x - y, tas_y - y]  in taslar.values():
                    belirtec1=0
                else:
                    belirtec1=0
                korx=[x for x in range(tas_x-y+belirtec1,tas_x)]
                kory=[y for y in range(tas_y-y+belirtec1,tas_y)]
                if korx:
                    dolular[2].append("belirlendi")
                    gidilebilecek.append([[a,b] for a,b in zip(korx,kory)])
                if not korx:
                    bosluk3=False

            if [tas_x-y,tas_y+y] in Tum_taslar.values() and len(dolular[3])==0:#sol ustte tas varsa---
                if [tas_x - y, tas_y + y] in taslar.values():
                    belirtec1=0
                    belirtec2=1
                else:
                    belirtec1=0
                    belirtec2=1

                korx=[x for x in range(tas_x-y+belirtec1,tas_x)]
                kory=[y for y in range(tas_y+1,tas_y+y+belirtec2)]
                if korx:
                    dolular[3].append("belirlendi")
                    gidilebilecek.append([[a,b] for a,b in zip(korx,reversed(kory))])
                if not korx:
                    bosluk4=False


        if not dolular[0] and bosluk1:#sag ustte tas yok ve boslukvar ise
            korx_y=[[tas_x+i,tas_y+i] for i in range(1,8) if tas_x+i<=8 and tas_y+i<=8]
            if korx_y:
                gidilebilecek.append(korx_y)

        if not dolular[1] and bosluk2:#sag altta tas yok ve bosluk var ise
            korx_y=[[tas_x+i,tas_y-i] for i in range(1,8) if tas_x+i<=8 and tas_y-i>=1]
            if korx_y:
                gidilebilecek.append(korx_y)

        if not dolular[2] and bosluk3:#sol altta tas yok ve bosluk var ise
            korx_y=[[tas_x-i,tas_y-i] for i in range(1,8) if tas_x-i>=1 and tas_y-i>=1]
            if korx_y:
                gidilebilecek.append(korx_y)

        if not dolular[3] and bosluk4:#sol ustte tas yok ve bosluk var ise
            korx_y=[[tas_x-i,tas_y+i] for i in range(1,8) if tas_x-i>=1 and tas_y+i<=8]
            if korx_y:
                gidilebilecek.append(korx_y)
        gidilebilecek_liste=[]

        for i in gidilebilecek:
                gidilebilecek_liste+=i

        if re.search("vezir",tas):
            vezir+=gidilebilecek_liste
            return vezir

        if re.search("fil",tas):
            return gidilebilecek_liste

    if re.search("SAH",tas):
        korx,kory=taslar[tas]
        gidilebilecek=[]
        for i in range(-1,2):
            y_korx=korx+i
            if y_korx in range(1,9):
                for k in range(-1,2):
                    y_kory=kory+k
                    if y_kory in range(1,9) and [y_korx,y_kory]!=[korx,kory]:
                        gidilebilecek+=[[y_korx,y_kory]]

        return gidilebilecek

    if re.search("s_piyon",tas):
        korx,kory=taslar[tas]
        gidilebilecek=[]
        for i in range(-1,2,2):
            y_korx=korx+i
            if y_korx in range(1,9):
                    gidilebilecek.append([y_korx,kory-1])

        if [korx,kory-1] not in beyazlar.values() and [korx,kory-1] not in siyahlar.values() and kory in range(1,9):
            gidilebilecek.append([korx,kory-1])
            if kory==7 and [korx, kory - 2] not in beyazlar.values() and [korx, kory - 2] not in siyahlar.values() :
                gidilebilecek.append([korx,kory-2])

        return gidilebilecek

    if re.search("b_piyon",tas):

        korx, kory = Tum_taslar[tas]
        gidilebilecek = []
        for i in range(-1, 2,2):
            y_korx = korx + i
            if y_korx in range(1, 9):
                    gidilebilecek.append([y_korx, kory + 1])

        if [korx,kory+1] not in beyazlar.values() and [korx,kory+1] not in siyahlar.values() and kory in range(1,9):
            gidilebilecek.append([korx,kory+1])
            if  kory==2 and [korx, kory + 2] not in beyazlar.values() and [korx, kory + 2] not in siyahlar.values() :
                gidilebilecek.append([korx,kory+2])

        return gidilebilecek

    if re.search("at",tas):
        korx,kory=taslar[tas]
        gidilebilecek=[]
        for i in range(-2,3,4):
            y_korx=korx+i
            if y_korx in range(1,9):
                for k in range(-1,2,2):
                    y_kory=kory+k
                    if y_kory in range(1,9):
                        gidilebilecek.append([y_korx,y_kory])

        for i in range(-2,3,4):
            y_kory=kory+i
            if y_kory in range(1,9):
                for k in range(-1,2,2):
                    y_korx=korx+k
                    if y_korx in range(1,9):
                         gidilebilecek.append([y_korx,y_kory])

        return gidilebilecek


def konum_tas(konum,beyazlar,siyahlar):
    tum_taslar = beyazlar.copy()
    tum_taslar.update(siyahlar)
    tas_ismi = list(tum_taslar.keys())[list(tum_taslar.values()).index(konum)]
    return tas_ismi

def tas_degeri(tas):
    for i,k in Tas_degerleri.items():
        if re.search(i,tas):
            return k

def en_iyi_uc_hamle_ilerisi(renk,beyazlar,siyahlar):

    y_Beyazlar=beyazlar.copy()
    y_Siyahlar=siyahlar.copy()

    if renk=="beyaz":

        def tehdit_et(tas_):#fonksiyona verilen tas oynayabildigi yerlerden savunmasiz tasi tehdit edebildigi yeri buluyor
            beless=[]
            tehlique=[]
            tehditler=[]
            for i in Siyahlar.keys():
                for k in yol_kontrol1(i, Beyazlar, Siyahlar):
                    if re.search("piyon", i):
                        if k[0] != Siyahlar[i][0]:
                            if k not in tehlique:
                                tehlique.append(k)
                    else:
                        if k not in tehlique:
                            tehlique.append(k)
            for knm in Siyahlar.values():
                if knm not in tehlique:
                    beless.append(knm)
            for yol in yol_kontrol1(tas_,Beyazlar,Siyahlar):
                tehdit_skoru=0
                neww_beyaz=Beyazlar.copy()
                if yol not in Siyahlar.values() and yol not in Beyazlar.values() and yol not in tehlique:#beles tasi tehdit edebilecegi yeri buluyor
                    neww_beyaz[tas_]=yol
                    for yeni in yol_kontrol1(tas_,neww_beyaz,Siyahlar):
                        if yeni in beless:
                            tehdit_skoru+=1

                    tehditler.append([tas_,yol,tehdit_skoru])
            if tehditler:
                ei=[yt[2] for yt in tehditler]
                oynanncak=tehditler[ei.index(max(ei))]
                if oynanncak[2]>0:
                    return oynanncak

        kacis = []
        kacacak_tas = []
        def tehlike():
            tehlikeli = []
            for i in Siyahlar.keys():
                for k in yol_kontrol1(i, Beyazlar, Siyahlar):
                    if re.search("piyon",i):
                        if k[0]!=Siyahlar[i][0]:
                            if k not in tehlikeli:
                                tehlikeli.append(k)
                    else:
                        if k not in tehlikeli:
                            tehlikeli.append(k)
            guvenli = []
            for i in Beyazlar.keys():
                for k in yol_kontrol1(i,Beyazlar,Siyahlar):
                    if k not in guvenli:
                        guvenli.append(k)
            for i, t in Beyazlar.items():
                if t in tehlikeli and t not in guvenli:#tas guvende degilse ve yenebilirse
                    if i not in kacacak_tas:
                        kacacak_tas.append(i)
                    for o in yol_kontrol1(i, Beyazlar, Siyahlar):
                        if o not in tehlikeli and o in guvenli and o not in Beyazlar.values() and o not in Siyahlar.values():
                            kacis.append([i, o])
            for q,w in Beyazlar.items():#beyaz tas yokedilebiliyorsa ve korumadaysa ancak takas durumunda zararli cikiliyorsa kacacak tas listesine eklenir
                for a,b in Siyahlar.items():
                    if w in yol_kontrol1(a,Beyazlar,Siyahlar):
                        if tas_degeri(q)>=tas_degeri(a):
                            kacacak_tas.append(q)

        tehlike()
        gorus_olasiligi = []
        tehditli_kacis = []  # yapilan hamlede korunmasiz tasi tehdit edilebilecek konumu bulur.En fazla korunmasiz tasi tehdit edebilecegi guvenli yere gider
        def korunmasiz_dusman_tas():
            tehdit_konum = []
            korumali = []
            beles_tas = []
            for i in Siyahlar.keys():
                for k in yol_kontrol1(i, Beyazlar, Siyahlar):
                    if re.search("piyon",i):
                        if k[0]!=Siyahlar[i][0]:
                            if k not in korumali:
                                korumali.append(k)
                    else:
                        if k not in korumali:
                            korumali.append(k)
            for z in Siyahlar.values():
                if not z in korumali:
                    beles_tas.append(z)
            konti_beyaz = Beyazlar.copy()
            for n in Beyazlar.keys():
                if re.search("piyon", n):
                    for g in yol_kontrol1(n, Beyazlar, Siyahlar):
                        tas_tehdit_skoru = 0
                        if g[0]==n[0]:
                            if g not in Beyazlar.values() and g not in korumali:
                                konti_beyaz[n] = g
                                for uu in yol_kontrol1(n, konti_beyaz, Siyahlar):
                                    if uu[0]!=g[0]:
                                        if uu in beles_tas:
                                            tas_tehdit_skoru += 1
                            if tas_tehdit_skoru > 0:
                                tehdit_konum.append([n, g, tas_tehdit_skoru])
                            konti_beyaz = Beyazlar.copy()
                else:
                 for g in yol_kontrol1(n, Beyazlar, Siyahlar):
                    tas_tehdit_skoru = 0
                    if g not in Beyazlar.values() and g not in korumali:
                        konti_beyaz[n] = g
                        for uu in yol_kontrol1(n, konti_beyaz, Siyahlar):
                            if uu in beles_tas:
                                tas_tehdit_skoru += 1
                    if tas_tehdit_skoru > 0:
                        tehdit_konum.append([n, g, tas_tehdit_skoru])
                    konti_beyaz = Beyazlar.copy()
            enn_iyi = [i[2] for i in tehdit_konum]
            if enn_iyi:
                tehditli_kacis.append(tehdit_konum[enn_iyi.index(max(enn_iyi))])


        korunmasiz_dusman_tas()
        def en_fazla_gorus():  # tehlike altina girmeden tasin gittigi yerde gordugu konum sayisi
            # hangi tas nereye giderse en fazla goruse sahip olur ve tehlikede olmaz
            tehlikeli = []
            for i in Siyahlar.keys():
                for k in yol_kontrol1(i, Beyazlar, Siyahlar):
                    if re.search("piyon",i):
                        if k[0]!=Siyahlar[i][0]:
                            if k not in tehlikeli:
                                tehlikeli.append(k)
                    else:
                        if k not in tehlikeli:
                            tehlikeli.append(k)
            kontrol_beyaz = Beyazlar.copy()
            kontrol_siyah = Siyahlar.copy()
            for i, k in Beyazlar.items():
                for t in yol_kontrol1(i, Beyazlar, Siyahlar):
                    if re.search("piyon",i) and k[0]!=t[0]:
                        continue
                    if t not in Beyazlar.values() and t not in Siyahlar.values() and t not in tehlikeli:
                        kontrol_beyaz[i] = t
                        gorus=0
                        for r in Beyazlar.keys():
                            gorus+=len(yol_kontrol1(r,kontrol_beyaz,kontrol_siyah))
                            gorus_olasiligi.append([gorus, i, t])
                kontrol_beyaz = Beyazlar.copy()
                kontrol_siyah = Siyahlar.copy()
            en_iyi = [i[0] for i in gorus_olasiligi]
            gidilecek = gorus_olasiligi[en_iyi.index(max(en_iyi))]
            Beyazlar[gidilecek[1]] = gidilecek[2]
            print(gidilecek[1], gidilecek[2], "noktasina giderek en fazla gorusu sagladi")

        fedakar_tas=[]
        yiyici_taslar=[]
        def fedakarlik(tas):#kacamayan tas icin kendini feda edebilecek daha degersiz taslardan en degersizini bulur
            tehdit_eden_tas = None
            tehdit_eden_tas_konumu = None
            tehdit_altindaki_tas = tas
            fedakar_taslar = []
            tehlikeli = []
            yeyeci_taslar=[]
            for i in Siyahlar.keys():
                for k in yol_kontrol1(i, Beyazlar, Siyahlar):
                    if re.search("piyon", i):
                        if k[0] != Siyahlar[i][0]:
                            if k not in tehlikeli:
                                tehlikeli.append(k)
                    else:
                        if k not in tehlikeli:
                            tehlikeli.append(k)
            for tas, konum in Siyahlar.items():
                for yu in yol_kontrol1(tas, Beyazlar, Siyahlar):
                    if Beyazlar[tehdit_altindaki_tas] == yu:
                        tehdit_eden_tas = tas
                        tehdit_eden_tas_konumu = konum
            for qw, rt in Beyazlar.items():
                for ye in yol_kontrol1(qw, Beyazlar, Siyahlar):
                    if ye == tehdit_eden_tas_konumu and tehdit_eden_tas_konumu not in tehlikeli:
                        yeyeci_taslar.append([qw,ye,tas_degeri(qw)])
                    if ye == tehdit_eden_tas_konumu and tas_degeri(qw) < tas_degeri(tehdit_altindaki_tas) and tehdit_eden_tas_konumu in tehlikeli:
                        fedakar_taslar.append([qw,ye,tas_degeri(qw)])
            if yeyeci_taslar:
                er_ii = [ik[len(ik) - 1] for ik in yeyeci_taslar]
                kendini_feda_eden = yeyeci_taslar[er_ii.index(min(er_ii))]  # kendini feda edebilecek taslardan en degersizi
                yiyici_taslar.append(kendini_feda_eden)

            if fedakar_taslar:
                enn_ii=[ik[len(ik)-1] for ik in fedakar_taslar]
                kendini_feda_eden=fedakar_taslar[enn_ii.index(min(enn_ii))]#kendini feda edebilecek taslardan en degersizi
                fedakar_tas.append(kendini_feda_eden)
            print(yiyici_taslar)
        def onune_gecme(tas):#2 tas da tehlikedeyse tehlikedekilerin birbirini savunmasi ilk oncelik,degersiz olan
                            #degerlinin onune geciyor.
            kacamayan_tas=tas
            tehdit_eden_tas=None
            guvenli = []
            one_gececek_tas = []
            one_gecicek_tas=None
            for i in Beyazlar.keys():
                for k in yol_kontrol1(i, Beyazlar, Siyahlar):
                    if re.search("piyon", i):
                        if i[0] != k[0]:
                            if k not in guvenli:
                                guvenli.append(k)
                    else:
                        if k not in guvenli:
                            guvenli.append(k)
            for tass in Beyazlar.keys():
                sahte_beyaz=Beyazlar.copy()
                sahte_siyah=Siyahlar.copy()
                if not tass==tas:
                 for konum in yol_kontrol1(tass,Beyazlar,Siyahlar):
                    if re.search("piyon",tass) and Beyazlar[tass][0]==konum[0]:
                        sahte_beyaz[tass]=konum
                        tehlikeli = []
                        for i in sahte_siyah.keys():
                            for k in yol_kontrol1(i, sahte_beyaz, sahte_siyah):
                                if re.search("piyon", i):
                                    if k[0] != sahte_siyah[i][0]:
                                        if k not in tehlikeli:
                                            tehlikeli.append(k)
                                else:
                                    if k not in tehlikeli:
                                        tehlikeli.append(k)
                        if sahte_beyaz[tas] not in tehlikeli:
                            if tas_degeri(tass) < tas_degeri(tas):
                                one_gececek_tas.append([tass,konum])
                    else:
                        sahte_beyaz[tass] = konum
                        tehlikeli = []
                        for i in sahte_siyah.keys():
                            for k in yol_kontrol1(i, sahte_beyaz, sahte_siyah):
                                if re.search("piyon", i):
                                    if k[0] != sahte_siyah[i][0]:
                                        if k not in tehlikeli:
                                            tehlikeli.append(k)
                                else:
                                    if k not in tehlikeli:
                                        tehlikeli.append(k)
                        if sahte_beyaz[tas] not in tehlikeli:
                            if tas_degeri(tass)<tas_degeri(tas):#one gecen tas korudugu tasdan degersiz olucak
                                one_gececek_tas.append([tass,konum,tas_degeri(tass)])

            if one_gececek_tas:
                for te in one_gececek_tas:
                    if te[0] in kacacak_tas:
                        one_gecicek_tas=te
                        break
                    else:
                        eiii = [ke[2] for ke in one_gececek_tas]
                        one_gecicek_tas = one_gececek_tas[eiii.index(min(eiii))]
                        break
            return one_gecicek_tas

        beles = []
        beles_kacis1 = []  # kacacak tas eger beles bir tasi yiyebiliyorsa

        def beles_tas():
            tehlique = []
            beless = []
            beles_kacis = []
            for i in Siyahlar.keys():
                for k in yol_kontrol1(i, Beyazlar, Siyahlar):
                    if re.search("piyon", i):
                        if k[0] != Siyahlar[i][0]:
                            if k not in tehlique:
                                tehlique.append(k)
                    else:
                        if k not in tehlique:
                            tehlique.append(k)
            new_beyaz = Beyazlar.copy()
            new_siyah = Siyahlar.copy()
            for you, me in Beyazlar.items():
                for us in Siyahlar.values():
                    if us in yol_kontrol1(you, Beyazlar, Siyahlar) and us not in tehlique:
                        new_siyah.pop(konum_tas(us, new_beyaz, new_siyah))
                        new_beyaz[you] = us
                        tehhlikke = []
                        for mo in new_siyah.keys():
                            for ko in yol_kontrol1(mo, new_beyaz, new_siyah):
                                if re.search("piyon", mo):
                                    if ko[0] != new_siyah[mo][0]:
                                        if ko not in tehhlikke:
                                            tehhlikke.append(ko)
                                else:
                                    if ko not in tehhlikke:
                                        tehhlikke.append(ko)

                        if us not in tehhlikke:
                            beless.append([you, us, tas_degeri(konum_tas(us, Beyazlar, Siyahlar))])
                    new_beyaz = Beyazlar.copy()
                    new_siyah = Siyahlar.copy()

            if beless:
                enniyi = [ki[2] for ki in beless]
                oynancakk = beless[enniyi.index(max(enniyi))]
                beles.append(
                    oynancakk)  # kacacak herhangi bir tas yoksa beles yenebilecek taslardan en degerlisi seciliyor.
                for yr in beless:  # beles tas yenecek tum ihtimaller
                    if kacacak_tas:
                        if yr[0] == kacacak_tas[
                            0]:  # eger beles tas yeme ihtimallerinden biri kacacak tasi iceriyorsa kacarken yeme olasiligina ekleniyor.
                            beles_kacis.append(yr)
                if beles_kacis:
                    enii = [ka[2] for ka in beles_kacis]
                    yapilcak = beles_kacis[enii.index(max(enii))]
                    beles_kacis1.append(yapilcak)

        beles_tas()
        oynanacakki=None
        def zorunlu_takas(tas):#eger tas sikismis ve hicbir sekilde kurtarilamiyorsa en degerli tasla 1-1 takasa giriyor
            takas=[]
            for yoll in yol_kontrol1(tas, Beyazlar, Siyahlar):
                if yoll in Siyahlar.values():
                    takas.append([yoll, tas_degeri(konum_tas(yoll, Beyazlar, Siyahlar))])
            if takas:
                eyy = [ih[1] for ih in takas]
                oynanacakki = takas[eyy.index(max(eyy))]





        def kacilan_en_iyi_gorus(tasss):#tehlikedeki tasin yapabilecegi en iyi mantikli haraket
            tehlikeli = []
            qorus_listesi=[]
            for i in Siyahlar.keys():
                for k in yol_kontrol1(i, Beyazlar, Siyahlar):
                    if re.search("piyon",i):
                        if k[0]!=Siyahlar[i][0]:
                            if k not in tehlikeli:
                                tehlikeli.append(k)
                    else:
                        if k not in tehlikeli:
                            tehlikeli.append(k)
            guvenli = []
            for i in Beyazlar.keys():
                for k in yol_kontrol1(i, Beyazlar, Siyahlar):
                    if re.search("piyon",i):
                        if i[0]!=k[0]:
                            if k not in guvenli:
                                guvenli.append(k)
                    else:
                        if k not in guvenli:
                            guvenli.append(k)
            kont_beyaz=Beyazlar.copy()
            ilk=Beyazlar[tasss]
            for v in yol_kontrol1(tasss,Beyazlar,Siyahlar):
                if re.search("piyon", tasss) and ilk[0] != v[0]:
                    continue
                gorus=0
                if v not in tehlikeli and v not in Siyahlar.values() and v not in Beyazlar.values():
                    kont_beyaz[tasss]=v
                    for m in kont_beyaz.keys():
                        gorus+=len(yol_kontrol1(m,kont_beyaz,Siyahlar))
                    qorus_listesi.append([gorus,v])

                kont_beyaz=Beyazlar.copy()
            en_eyi = [j[0] for j in qorus_listesi]
            if en_eyi:#eger tasin kacabilecegi yer varsa
                tehditli_kac=tehdit_et(tasss)
                fedakarlik(tasss)
                if yiyici_taslar:
                    yenen_tas13=konum_tas(yiyici_taslar[0][1],Beyazlar,Siyahlar)
                    Siyahlar.pop(konum_tas(yiyici_taslar[0][1],Beyazlar,Siyahlar))
                    Beyazlar[yiyici_taslar[0][0]]=yiyici_taslar[0][1]
                    print(yiyici_taslar[0][0],yenen_tas13,"tasini yiyerek tehlikedeki tasi kurtardi")

                elif tehditli_kac:#kactigi yerde korunmasiz bir siyahi tehdit edebiliyorsa
                    if tehditli_kac[1] in Siyahlar.values():#kactigi yerde tasi yiyorsa
                        Siyahlar.pop(konum_tas(tehditli_kac[1],Beyazlar,Siyahlar))
                    Beyazlar[tehditli_kac[0]]=tehditli_kac[1]
                    print(tehditli_kac[0],tehditli_kac[1],"noktasina kacip tehditte bulundu")

                else:
                    gidis=qorus_listesi[en_eyi.index(max(en_eyi))]
                    Beyazlar[tasss]=gidis[1]
                    print(tasss,gidis[1],"noktasina kacip en fazla gorusu sagladi")


            if not en_eyi:#eger beyaz tasin kacabilecegi yer yoksa baska tasla karsinin tehdit eden tasini yemeyi deniyor.O da olmazsa karsinin guvende olmayan
                            #bir tasini tehdit etmeyi deniyor,o da olmazsa en iyi gorusu alabildigi baska bir tasi oynuyor.

                fedakarlik(tasss)
                one_gecicek_tas=onune_gecme(tasss)
                if yiyici_taslar:
                    yenen_tas13=konum_tas(yiyici_taslar[0][1],Beyazlar,Siyahlar)
                    Siyahlar.pop(konum_tas(yiyici_taslar[0][1],Beyazlar,Siyahlar))
                    Beyazlar[yiyici_taslar[0][0]]=yiyici_taslar[0][1]
                    print(yiyici_taslar[0][0],yenen_tas13,"tasini yiyerek tehlikedeki tasi kurtardi")
                elif one_gecicek_tas:
                    Beyazlar[one_gecicek_tas[0]]=one_gecicek_tas[1]
                    print(one_gecicek_tas[0],one_gecicek_tas[1],"noktasina giderek tehlikedeki tasin onune gecti")

                elif fedakar_tas:#tehdit altindaki kacamayan tastan daha degersiz bir tas bu tasi kurtarabiliyorsa
                    Siyahlar.pop(konum_tas(fedakar_tas[0][1], Beyazlar, Siyahlar))
                    Beyazlar[fedakar_tas[0][0]] = fedakar_tas[0][1]
                    print(fedakar_tas[0][0],fedakar_tas[0][1],"noktasina giderek",tasss,"tasi icin kendini feda etti/kurtardi.")#huzunlu :(

                elif oynanacakki:#zorunlu takas varsa
                    yenen_tas12=konum_tas(oynanacakki[0],Beyazlar,Siyahlar)
                    Siyahlar.pop(konum_tas(oynanacakki[0],Beyazlar,Siyahlar))
                    Beyazlar[tasss]=oynanacakki[0]
                    print(tasss,"sikisti ve",Beyazlar[tasss],"noktasina gidip",yenen_tas12,"tasini yoketti")
                elif tehditli_kacis:#tehdit altindaki tas kacamiyorsa baska tasla dusmanin guvende olmayan tasi tehdit ediliyor
                    Beyazlar[tehditli_kacis[0][0]]=tehditli_kacis[0][1]
                    print(tehditli_kacis[0][0], tehditli_kacis[0][1], "noktasina kacip tehditte bulundu")

                elif not tehditli_kacis:#eger hicbir sekilde saldiri savusturulamiyorsa beyazlar en fazla gorus alabildigi tasi oynuyor
                    en_fazla_gorus()

        ikiliden_kacacak=[]
        def ikili_tehdit_noktalari():#rakibin oynayip 2 beyaz tasi tehdit edebilecegi noktalar.
            tehlikeli = []
            ikili_tehdit = []
            for i in Siyahlar.keys():
                for k in yol_kontrol1(i, Beyazlar, Siyahlar):
                    if re.search("piyon", i):
                        if k[0] != Siyahlar[i][0]:
                            if k not in tehlikeli:
                                tehlikeli.append(k)
            guvenli = []
            for i in Beyazlar.keys():
                for k in yol_kontrol1(i, Beyazlar, Siyahlar):
                    if re.search("piyon", i):
                        if i[0] != k[0]:
                            if k not in guvenli:
                                guvenli.append(k)
                    else:
                        if k not in guvenli:
                            guvenli.append(k)
            for tas in Siyahlar.keys():#siyahlarin 2 tasi tehdit edebildigi noktalar
                for yol in yol_kontrol1(tas,Beyazlar,Siyahlar):
                    yeni_siyah = Siyahlar.copy()
                    tehdit_skoru=0
                    if re.search("piyon",tas) and Siyahlar[tas][0]==yol[0]:
                        yeni_siyah[tas] = yol
                        for yeni_yol in yol_kontrol1(tas,Beyazlar,yeni_siyah):
                            if yeni_siyah[tas][0]!=yeni_yol[0] and yeni_yol in Beyazlar.values():
                                    tehdit_skoru+=1
                        if tehdit_skoru>=2:
                            ikili_tehdit.append([tas,yol,tehdit_skoru])
                    if not re.search("piyon",tas) and yol not in Siyahlar.values():
                        yeni_siyah[tas] = yol
                        for yeni_yol in yol_kontrol1(tas, Beyazlar, yeni_siyah):
                            if yeni_yol in Beyazlar.values():
                                    tehdit_skoru += 1
                        if tehdit_skoru >= 2:
                            ikili_tehdit.append([tas,yol,tehdit_skoru])
            if ikili_tehdit:
                for noktalar in ikili_tehdit:
                    if noktalar[1] not in guvenli and noktalar[1] not in tehlikeli:#2li tehdit cekilen nokta siyahlar tarafindan korunmuyorsa ve beyazlar
                                                                                    #tarafindan korunmuyorsa
                        yeni_siyah=Siyahlar.copy()
                        yeni_siyah[noktalar[0]]=noktalar[1]
                        for yoll in yol_kontrol1(noktalar[0],Beyazlar,yeni_siyah):#atin tehdit edecegi taslar.
                            if yoll in Beyazlar.values():
                                ikiliden_kacacak.append(konum_tas(yoll,Beyazlar,Siyahlar))
                                break

                    if noktalar[1] not in guvenli and noktalar[1] in tehlikeli:#eger gelicegi noktada beyaz yiyemiyorsa ve siyah baska tasla destekliyorsa.
                        yeni_siyah = Siyahlar.copy()
                        yeni_siyah[noktalar[0]] = noktalar[1]
                        for yoll in yol_kontrol1(noktalar[0], Beyazlar, yeni_siyah):  # atin tehdit edecegi taslar.
                            if yoll in Beyazlar.values():
                                ikiliden_kacacak.append(konum_tas(yoll, Beyazlar, Siyahlar))
                                break





        def yeni_fark(beyazlarr,siyahlarr):
            toplam_eskibeyaz=0
            toplam_eskisiyah=0
            toplam_yenibeyaz=0
            toplam_yenisiyah=0
            for i in Beyazlar.keys():
                toplam_eskibeyaz+=tas_degeri(i)
            for k in Siyahlar.keys():
                toplam_eskisiyah+=tas_degeri(k)
            for u in beyazlarr.keys():
                toplam_yenibeyaz+=tas_degeri(u)
            for t in siyahlarr.keys():
                toplam_yenisiyah+=tas_degeri(t)
            yennni=(toplam_yenibeyaz-toplam_yenisiyah)-(toplam_eskibeyaz-toplam_eskisiyah)
            return yennni

        olasii=[]
        olasii2=[]
        olass=[]
        b_s_b=[]
        y_s_b=[]
        b_y=[]
        b_s=[]
        yok_etme = False
        for i, k in y_Beyazlar.items():  # beyaz sirasi
            for a in yol_kontrol1(i, y_Beyazlar, y_Siyahlar):
                yok_etme1 = False  # tas gittigi konumda yokedebiliyor mu
                devam = True

                if re.search("piyon", i) and a[0] != k[
                    0] and a in y_Siyahlar.values():  # piyon capraz tas yiyebiliyorsa
                    yenen_tas1 = konum_tas(a, y_Beyazlar, y_Siyahlar)
                    y_Siyahlar.pop(yenen_tas1)
                    y_Beyazlar[i] = a
                    devam = False
                    yok_etme1, yok_etme = True, True

                if re.search("piyon", i) and a[0] == k[0]:  # duz gidebiliyorsa
                    y_Beyazlar[i] = a
                    devam = False

                if devam and re.search("piyon", i):  # capraz yiyemiyorsa-duz gidemiyorsa
                    continue

                if a in y_Siyahlar.values() and not re.search("piyon", i):
                    yenen_tas1 = konum_tas(a, y_Beyazlar, y_Siyahlar)
                    y_Siyahlar.pop(yenen_tas1)
                    y_Beyazlar[i] = a
                    devam = False
                    yok_etme1, yok_etme = True, True

                if a not in y_Beyazlar.values() and a not in y_Siyahlar.values() and not re.search("piyon", i):
                    y_Beyazlar[i] = a
                    devam = False
                if not re.search("piyon", i) and a in y_Beyazlar.values() and devam:
                    continue
                yeni_beyazlar = y_Beyazlar.copy()
                yeni_siyahlar = y_Siyahlar.copy()
                yok_etme4 = False
                for b, c in yeni_siyahlar.items():  # siyah sirasi
                    for d in yol_kontrol1(b, yeni_beyazlar, yeni_siyahlar):
                        yok_etme2 = False
                        devam1 = True

                        if re.search("piyon", b) and d[0] != c[0] and d in yeni_beyazlar.values():
                            yenen_tas2 = konum_tas(d, yeni_beyazlar, yeni_siyahlar)
                            yeni_beyazlar.pop(yenen_tas2)
                            yeni_siyahlar[b] = d
                            yok_etme2, yok_etme4 = True, True
                            devam1 = False

                        if re.search("piyon", b) and d[0] == c[0]:
                            yeni_siyahlar[b] = d
                            devam1 = False

                        if devam1 and re.search("piyon", b):
                            continue

                        if d in yeni_beyazlar.values() and not re.search("piyon", b):
                            yenen_tas2 = konum_tas(d, yeni_beyazlar, yeni_siyahlar)
                            yeni_beyazlar.pop(yenen_tas2)
                            yeni_siyahlar[b] = d
                            yok_etme2, yok_etme4 = True, True
                            devam1 = False

                        if d not in yeni_siyahlar.values() and d not in yeni_beyazlar.values() and not re.search("piyon", b):
                            yeni_siyahlar[b] = d
                            devam1 = False

                        if not re.search("piyon", b) and d in yeni_siyahlar.values() and devam1:
                            continue  # dost tas varsa gidilecek yerde altindaki islemi yapmiyor.

                        yeni2_beyazlar = yeni_beyazlar.copy()
                        yeni2_siyahlar = yeni_siyahlar.copy()
                        yok_etme5 = False
                        for e, f in yeni2_beyazlar.items():  # beyaz sirasi
                            for g in yol_kontrol1(e, yeni2_beyazlar, yeni2_siyahlar):
                                yok_etme3 = False  # gidilebilen yerde beyaz tas yiyor mu
                                devam2 = True
                                if re.search("piyon", e) and f[0] != g[0] and g in yeni2_siyahlar.values():
                                    yenen_tas3 = konum_tas(g, yeni2_beyazlar, yeni2_siyahlar)
                                    yeni2_siyahlar.pop(yenen_tas3)
                                    yeni2_beyazlar[e] = g
                                    yok_etme3, yok_etme5 = True, True
                                    devam2 = False
                                if re.search("piyon", e) and f[0] == g[0]:
                                    yeni2_beyazlar[e] = g
                                    devam2 = False

                                if devam2 and re.search("piyon", e):
                                    continue

                                if g in yeni2_siyahlar.values() and not re.search("piyon", e):
                                    yenen_tas3 = konum_tas(g, yeni2_beyazlar, yeni2_siyahlar)
                                    yeni2_siyahlar.pop(yenen_tas3)
                                    yeni2_beyazlar[e] = g
                                    yok_etme3, yok_etme5 = True, True
                                    devam2 = False

                                if g not in yeni2_beyazlar.values() and g not in yeni2_siyahlar.values() and not re.search(
                                        "piyon", e):
                                    yeni2_beyazlar[e] = g
                                    devam2 = False
                                if not re.search("piyon", e) and g in yeni2_beyazlar.values() and devam2:
                                    continue

                                if not yok_etme and yok_etme2:  # yeme olasiligi 0-siyah-beyaz,eger beyazin ilk hamlesinde
                                    # yiyebilecegi tas yok ise takasa veya takasli-tehdit olusturabilecegi yerler
                                    olasii.append([[i, a], [b, d], [e, g]])
                                    if yok_etme3:
                                        kontrol3 = False
                                        for t, y in yeni2_siyahlar.items():
                                            if g in yol_kontrol1(t, yeni2_beyazlar,
                                                                 yeni2_siyahlar):  # 4.hamlede siyah beyaz yiyorsa
                                                yenen_tas5 = konum_tas(g, yeni2_beyazlar, yeni2_siyahlar)
                                                if yeni_fark(yeni2_beyazlar, yeni2_siyahlar) - tas_degeri(
                                                        yenen_tas5) > 0:
                                                    olasii2.append([[i, a], [b, d], [e, g], [t, g],
                                                                    yeni_fark(yeni2_beyazlar,
                                                                              yeni2_siyahlar) - tas_degeri(yenen_tas5)])
                                                kontrol3 = True
                                        if not kontrol3:
                                            if yeni_fark(yeni2_beyazlar, yeni2_siyahlar) > 0:
                                                olasii2.append([[i, a], [b, d], [e, g],
                                                                yeni_fark(yeni2_beyazlar, yeni2_siyahlar)])

                                if yok_etme1 and yok_etme2:  # yeme olasiligi beyaz-siyah-beyaz, 2 siyah yenip 1-2 beyaz verilen takas-
                                    olass.append([[i, a], [b, d], [e, g]])
                                    if yok_etme3:
                                        kontrol4 = False
                                        for t, u in yeni2_siyahlar.items():
                                            if g in yol_kontrol1(t, yeni2_beyazlar, yeni2_siyahlar):
                                                yenen_tas4 = konum_tas(g, yeni2_beyazlar, yeni2_siyahlar)

                                                b_s_b.append([[i, a], [b, d], [e, g], [t, g],
                                                              yeni_fark(yeni2_beyazlar, yeni2_siyahlar) - tas_degeri(
                                                                  yenen_tas4)])
                                                kontrol4 = True
                                        if not kontrol4:
                                            b_s_b.append([[i, a], [b, d], [e, g],
                                                          yeni_fark(yeni2_beyazlar, yeni2_siyahlar)])

                                yeni2_beyazlar = yeni_beyazlar.copy()
                                yeni2_siyahlar = yeni_siyahlar.copy()

                        if yok_etme1 and yok_etme2 and not yok_etme5:  # yeme olasiligi beyaz-siyah, bire bir takas
                            olasilik = [i, a], [b, d], [e, g]
                            if yeni_fark(yeni2_beyazlar, yeni2_siyahlar) > 0:
                                b_s.append([[i, a], [b, d], [e, g], yeni_fark(yeni2_beyazlar, yeni2_siyahlar)])

                        yeni_beyazlar = y_Beyazlar.copy()
                        yeni_siyahlar = y_Siyahlar.copy()

                if yok_etme1 and not yok_etme4:  # yeme olasiligi beyaz, kayip vermeden siyah tas alma olasiligi
                    olasilik = [i, a], [b, d], [e, g]
                    b_y.append([[i, a], [b, d], [e, g], yeni_fark(yeni2_beyazlar, yeni2_siyahlar)])

                y_Siyahlar = Siyahlar.copy()
                y_Beyazlar = Beyazlar.copy()


        if b_s_b:  # beyaz-siyah-beyaz takasinda beyaz ilk hamleyi oynadiktan sonra
            # herhangi bir olasilikta zarar ediliyorsa
            # ilk hamleyle alakali butun olasiliklar kaldirilir.iyilestirme yapildi--
            b_s_b = [i for i in b_s_b if i[0][1]==i[1][1] and i[1][1]==i[2][1] and i[len(i)-1]>0]

        ikili_tehdit_noktalari()
        print(ikiliden_kacacak)
        if kacacak_tas:  # guvende olmayan tas varsa(siyah gelecek hamlede yiyebilir ve beyaz sonraki hamlede yiyemez)
            m_b_s = []  # kacmasi gereken tas beyaz-siyah olasiliklarindan hangisinde oynaniyorsa o olasiliklari birakiyor.
                        #yani tasin kacmasi gerekiyorsa,bu tasi oynayip karli cikabilecegi 1-1 takas hamlesini aliyor
            eii=[tas_degeri(o) for o in kacacak_tas]
            en_degerli_kacacak=kacacak_tas[eii.index(max(eii))]

            for i in b_s:
                if i[0][0]==en_degerli_kacacak:
                    m_b_s.append(i)
            m_b_s_b = []  # kacmasi gereken tas beyaz-siyah-beyaz olasiliklarindan hangisinde oynaniyorsa o olasiliklari birakiyor.
                          #yani tasin kacmasi gerekiyorsa ve bu tasla alakali  beyaz-siyah-beyaz-siyah takasi varsa onu aliyor
            for i in b_s_b:
                if i[0][0]==en_degerli_kacacak:
                    m_b_s_b.append(i)

            if beles_kacis1:#beyaz kacicaksa ve kacarken beles bir tasi yiyebiliyorsa

                yenen_tas9 = konum_tas(beles_kacis1[0][1], Beyazlar, Siyahlar)
                Siyahlar.pop(yenen_tas9)
                Beyazlar[beles_kacis1[0][0]] = beles_kacis1[0][1]
                print(beles[0][0], beles[0][1], "noktasina ilerledi ve", yenen_tas9, "tasini yoketti- kacis beles tas")



            elif m_b_s:#kacacak tas varsa karli-beyaz-siyah takasina giriyor
                en_iyi = [i[len(i) - 1] for i in m_b_s]
                oynanacak = m_b_s[en_iyi.index(max(en_iyi))][0]
                yenen_tas10 = konum_tas(oynanacak[1], Beyazlar, Siyahlar)
                Siyahlar.pop(yenen_tas10)
                Beyazlar[oynanacak[0]] = oynanacak[1]
                print(oynanacak[0], oynanacak[1], "noktasina ilerledi ve",yenen_tas10,"tasini yoketti- kacis 1-1 takas")

            elif m_b_s_b :#kacacak tas varsa beyaz-siyah-/beyaz-siyah takasina giriyor
                en_iyi = [i[len(i) - 1] for i in m_b_s_b]
                oynanacak = m_b_s_b[en_iyi.index(max(en_iyi))][0]
                yenen_tas11 = konum_tas(oynanacak[1], Beyazlar, Siyahlar)
                Siyahlar.pop(yenen_tas11)
                Beyazlar[oynanacak[0]] = oynanacak[1]
                print(oynanacak[0], oynanacak[1], "noktasina ilerledi ve",yenen_tas11,"tasini yoketti- kacis b-s-b-s")

            else:#eger kacmasi gereken tas kar edebilecegi bir hamle yapamiyorsa
                print(en_degerli_kacacak)
                kacilan_en_iyi_gorus(en_degerli_kacacak)#tehlikedeki tas takimina sonraki hamlede en fazla gorusu sagladigi konuma gidiyor
                                                    #eger hareket edemiyorsa degersiz tas tehlikedeki tasin onune gidiyor.gidecek tas da yoksa
                                                    #daha degersiz bir tas kendini  feda edip degerli tasi kurtariyor.
                                                    #o da yoksa en iyi gorus saglayan baska bir tas oynaniyor


        elif ikiliden_kacacak:
            kacilan_en_iyi_gorus(ikiliden_kacacak[0])

        elif beles:#eger tehlikede tas yoksa ve siyah tas yendikten sonra kayip verilmiyorsa--DUZENLEME GEREKLI-siyah tas verip baska tasi yiyebilir
            yenen_tas6 = konum_tas(beles[0][1], Beyazlar, Siyahlar)
            Siyahlar.pop(yenen_tas6)
            Beyazlar[beles[0][0]] = beles[0][1]
            print(beles[0][0], beles[0][1], "noktasina ilerledi ve", yenen_tas6, "tasini yoketti- beles tas")

        elif b_s:  # bire bir karli takas--
            en_iyi = [i[len(i) - 1] for i in b_s]
            oynanacak = b_s[en_iyi.index(max(en_iyi))][0]
            yenen_tas7 = konum_tas(oynanacak[1], Beyazlar, Siyahlar)
            Siyahlar.pop(yenen_tas7)
            Beyazlar[oynanacak[0]] = oynanacak[1]
            print(oynanacak[0], oynanacak[1], "noktasina ilerledi ve",yenen_tas7,"tasini yoketti --karli 1-1 takas")

        elif b_s_b:  # beyaz-siyah-beyaz veya beyaz-siyah-beyaz-siyah karli takas--
            en_iyi = [i[len(i) - 1] for i in b_s_b]
            oynanacak = b_s_b[en_iyi.index(max(en_iyi))][0]
            yenen_tas8 = konum_tas(oynanacak[1], Beyazlar, Siyahlar)
            Siyahlar.pop(yenen_tas8)
            Beyazlar[oynanacak[0]] = oynanacak[1]
            print(oynanacak[0], oynanacak[1], "noktasina ilerledi ve",yenen_tas8,"tasini yoketti- karli b-s-b-s")

        else:#Eger karli cikilabilecek ihtimal yoksa
            if tehditli_kacis:#gittigi yerde korunmasiz bir tasi tehdit edebilen tas varsa
                if tehditli_kacis[0][1] in Siyahlar.values():
                    Siyahlar.pop(konum_tas(tehditli_kacis[0][1], Beyazlar, Siyahlar))
                Beyazlar[tehditli_kacis[0][0]] = tehditli_kacis[0][1]
                print(tehditli_kacis[0][0],tehditli_kacis[0][1],"noktasina gidip tehditte bulundu")
            if not tehditli_kacis:#hicbir tas hicbir sekilde korunmasiz bir tasi tehdit edemiyorsa
                en_fazla_gorus()#beyazlar bir sonraki hamlede takimina en fazla gorus getiren hamleyi oynar
import pygame,os

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
gorseller=["b_at.png","b_fil.png","b_kale.png","b_piyon.png",
                   "b_SAH.png","b_vezir.png"]
pencere=pygame.display.set_mode((850,850))
def gorsel():#siyah ve beyaz taslari konumlandirir.

    for i, k in Beyazlar.items():
        resim = i[:len(i) - 1] + ".png"
        pencere.blit(pygame.image.load(resim), (k[0] * 100-50, k[1] * 100 - 50))
    for i,k in Siyahlar.items():
        resim = i[:len(i) - 1] + ".png"
        pencere.blit(pygame.image.load(resim), (k[0] * 100 - 50, k[1] * 100 - 50))


def mouse_secilen():
    def tiklama_konum(konum):
        x = 0
        for xx in range(25, 825, 100):
            x += 1
            y = 0
            for yy in range(25, 825, 100):
                y += 1
                if konum[0] in range(xx, xx + 100) and konum[1] in range(yy, yy + 100):
                    return [x, y]
    x=0
    pencere.blit(pygame.transform.scale(pygame.image.load("tahta.png"), (850, 850)), (0, 0))
    event = pygame.event.wait()
    if event.type == pygame.MOUSEBUTTONDOWN:
        konum = pygame.mouse.get_pos()
        for xx in range(25,825,100):
         x+=1
         y=0
         for yy in range(25,825,100):
            y+=1
            if konum[0] in range(xx,xx+100) and konum[1] in range(yy,yy+100):
                if [x,y] in Siyahlar.values():
                    secilen_tas=konum_tas([x,y],Beyazlar,Siyahlar)
                    secim = []
                    for gidilebilen in yol_kontrol1(secilen_tas,Beyazlar,Siyahlar):
                        if re.search("s_piyon",secilen_tas):
                            if gidilebilen[0]==Siyahlar[secilen_tas][0]:
                                pygame.draw.rect(pencere, (0, 255, 255),(gidilebilen[0] * 100 - 74, gidilebilen[1] * 100 - 74, 99, 99))
                                secim.append(gidilebilen)
                            if gidilebilen[0]!=Siyahlar[secilen_tas][0] and gidilebilen in Beyazlar.values():
                                pygame.draw.rect(pencere, (255, 64, 64),(gidilebilen[0] * 100 - 74, gidilebilen[1] * 100 - 74, 99, 99))
                                secim.append(gidilebilen)
                        else:
                            if gidilebilen not in Siyahlar.values() and gidilebilen in Beyazlar.values():
                                pygame.draw.rect(pencere, (255, 64, 64),(gidilebilen[0] * 100 - 74, gidilebilen[1] * 100 - 74, 99, 99))
                                secim.append(gidilebilen)
                            if gidilebilen not in Siyahlar.values() and gidilebilen not in Beyazlar.values():
                                pygame.draw.rect(pencere, (0, 255, 255),(gidilebilen[0] * 100 - 74, gidilebilen[1] * 100 - 74, 99, 99))
                                secim.append(gidilebilen)
                    gorsel()
                    pygame.display.update()
                    if secim:
                        while True:
                            eventt = pygame.event.wait()
                            if eventt.type == pygame.MOUSEBUTTONDOWN:
                                pos1 = pygame.mouse.get_pos()
                                tiklanan_nokta=tiklama_konum(pos1)
                                if tiklanan_nokta in secim:
                                    if tiklanan_nokta in Beyazlar.values():
                                        Beyazlar.pop(konum_tas(tiklanan_nokta,Beyazlar,Siyahlar))
                                        Siyahlar[secilen_tas]=tiklanan_nokta
                                        pencere.blit(pygame.transform.scale(pygame.image.load("tahta.png"), (850, 850)),
                                                     (0, 0))
                                        gorsel()
                                        pygame.display.update()
                                        return True
                                    if tiklanan_nokta not in Beyazlar.values():
                                        Siyahlar[secilen_tas]=tiklanan_nokta
                                        pencere.blit(pygame.transform.scale(pygame.image.load("tahta.png"), (850, 850)),
                                                     (0, 0))
                                        gorsel()
                                        pygame.display.update()
                                        return True
                                if tiklanan_nokta==Siyahlar[secilen_tas]:
                                    continue

                                else:
                                    break

siyah_sirasi = False
while True:
    if "s_SAH1" not in Siyahlar.keys():
        print("Beyazlar kazandi")
        break

    if not siyah_sirasi:
        en_iyi_uc_hamle_ilerisi("beyaz",Beyazlar,Siyahlar)
        pencere.blit(pygame.transform.scale(pygame.image.load("tahta.png"), (850, 850)), (0, 0))
        gorsel()
        pygame.display.update()
        siyah_sirasi=True
    if siyah_sirasi:
        if mouse_secilen():
            siyah_sirasi=False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
