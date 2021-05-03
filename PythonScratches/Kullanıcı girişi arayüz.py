from tkinter import *
import math
import matplotlib.pyplot as plt
from random import randint
"""cok onceden yazdigim bir kod"""
admin=open("admin.txt","r").read().split()
adminsif=open("adminsifre.txt","r").read().split()
yoneticii=open("yonetici.txt","r").read().split()
yoneticisifre=open("yoneticisifre.txt","r").read().split()
users=open("users.txt","r").read().split()
passwords=open("passwords.txt","r").read().split()
pencere1=Tk()
pencere1.geometry("250x120+600+250")
pencere1.resizable(height=False,width=False)

def kayit():
    def  olustur():

     if kayit1.get() in users or kayit1.get() in admin or kayit1.get()=="YahyaKemal":
         pencere7=Toplevel()
         bilgi8=Label(pencere7,text="Lütfen başka bir kullanıcı adı seçiniz.")
         bilgi8.pack()
         buton9=Button(pencere7,text="Tamam",command=pencere7.destroy)
         buton9.pack()

     elif kayit2.get() == kayit3.get() and len(kayit2.get())>=6  and len(kayit1.get())>=6:
        pencere5 = Toplevel()
        pencere5.geometry("200x100")
        bilgi3 = Label(pencere5, text="Kayıt başarılı!")
        bilgi3.pack(side=TOP)
        bilgi4=Label(pencere5,text="Kullanıcı adınız:   {}".format(kayit1.get()))
        bilgi4.place(relx=0.05,rely=0.3)
        bilgi5=Label(pencere5,text="Şifreniz:  "+len(kayit2.get())*"*")
        bilgi5.place(relx=0.05,rely=0.55)
        buton7=Button(pencere5,text="Tamam",command= pencere5.destroy)
        buton8=Button(pencere4,text="Giriş Yap",command=pencere4.destroy)
        buton8.place(relx=0.71,rely=0.7)
        buton7.place(relx=0.6,rely=0.70)

        with open("users.txt","a+") as x:
            x.write(" "+kayit1.get())
            x.close()

        with open ("passwords.txt","a+") as y:
            y.write(" "+kayit2.get())
            y.close()
            return x,y

     elif kayit2.get()!=kayit3.get():
        kayit2.delete(0,END)
        kayit3.delete(0,END)
        pencere6=Toplevel()
        pencere6.resizable(height=False,width=False)
        pencere6.geometry("150x100+650+265")
        bilgi6=Label(pencere6,text="Şifreler aynı değil")
        bilgi6.pack()
        buton6=Button(pencere6,text="Tekrar Dene",command=pencere6.destroy)
        buton6.place(relx=0.26,rely=0.4)

     elif len (kayit2.get())<6 or len (kayit1.get())<6:
         bilgi7=Label(pencere4,text="""Kullanıcı adı ve Şifreniz en az
 6 harfli olmalıdır!!""")
         bilgi7.place(relx=0.0, rely=0.7)


    pencere4=Tk()
    pencere4.title("Yeni Kullanıcı")
    pencere4.geometry("250x120+600+250")
    metin3=Label(pencere4,text="Yeni Kullanıcı Adı:")
    metin3.place(relx=0.0,rely=0.0)
    metin4=Label(pencere4,text="Yeni Şifre:")
    metin4.place(relx=0.0,rely=0.25)
    metin5=Label(pencere4,text="Şifre Tekrar::")
    metin5.place(relx=0.0,rely=0.50)
    kayit1=Entry(pencere4,width=20)
    kayit1.place(relx=0.4,rely=0.02)
    kayit2=Entry(pencere4,width=20)
    kayit2.place(relx=0.4,rely=0.25)
    kayit3=Entry(pencere4,width=20)
    kayit3.place(relx=0.4,rely=0.5)
    buton5=Button(pencere4,text="Onayla",command=olustur)
    buton5.place(relx=0.71,rely=0.7)




def grafik():
    pencere = Tk()
    pencere.title("Grafik Çizme")

    def ciz():
       try:

            x = []
            t = []
            a = 0
            while a < len(xeksendegeri.get().split(",")):
                print(len(xeksendegeri.get().split(",")))
                t.append(int(xeksendegeri.get().split(",")[a]))
                x.append(int(yeksendegeri.get().split(",")[a]))
                a += 1
            sonuc1, sonuc2, sonuc3 = 0, 0, 0
            for i, k in zip(x, t):
                sonuc1 += i * k
                sonuc2 += (i ** 2)
                sonuc3 += k ** 2
            R = ((sonuc1 ** 2) / (sonuc2 * sonuc3)) ** 0.5
            print("Doğruluk payı=", R)
            plt.plot(t, x, linewidth=4)
            plt.title("grafik")
            plt.ylabel(yeksenisim.get())
            plt.xlabel(xeksenisim.get())
            plt.show()

       except (ValueError,ZeroDivisionError):
           print("Lütfen Sayı Girin")

    pencere.geometry("300x130")
    pencere.resizable(width=False, height=False)
    label1 = Label(pencere, text="X Ekseni ismi")
    label1.grid(row=1, column=1)
    xeksenisim = Entry(pencere,width=40)
    xeksenisim.grid(row=1, column=2)
    label2 = Label(pencere, text="Y Ekseni ismi")
    label2.grid(row=2, column=1)
    yeksenisim = Entry(pencere,width=40)
    yeksenisim.grid(row=2, column=2)
    label3 = Label(pencere, text="X eksen değerleri")
    label3.grid(row=3, column=1)
    xeksendegeri = Entry(pencere, width=40)
    xeksendegeri.grid(row=3, column=2)
    label4 = Label(pencere, text="Y eksen değerleri")
    label4.grid(row=4, column=1)
    yeksendegeri = Entry(pencere, width=40)
    yeksendegeri.grid(row=4, column=2)
    buton = Button(pencere, text="Çiz", width=5, command=ciz)
    buton.place(relx=0.83, rely=0.7)

    mainloop()



def trigonometri():
    pencere20=Tk()
    pencere20.title("TRİGONOMETRİ")
    pencere20.geometry("300x300+400+300")
    pencere20.resizable(height=False,width=False)
    sin=Label(pencere20,text="Sinüs")
    sin.place(relx=0.0,rely=0.0)
    entry1=Entry(pencere20,width=5)
    entry1.place(relx=0.16,rely=0.0)
    esittir1=Label(pencere20,text="=")
    esittir1.place(relx=0.27,rely=0.0)
    entry2=Entry(pencere20,width=30)
    entry2.place(relx=0.31,rely=0.0)
    cos=Label(pencere20,text="Cosinüs")
    cos.place(relx=0.0,rely=0.1)
    entry3=Entry(pencere20,width=5)
    entry3.place(relx=0.16,rely=0.1)
    esittir2=Label(pencere20,text="=")
    esittir2.place(relx=0.27,rely=0.1)
    entry4=Entry(pencere20,width=30)
    entry4.place(relx=0.31,rely=0.1)
    tan=Label(pencere20,text="Tanjant")
    tan.place(relx=0.0,rely=0.20)
    entry5=Entry(pencere20,width=5)
    entry5.place(relx=0.16,rely=0.2)
    esittir3=Label(pencere20,text="=")
    esittir3.place(relx=0.27,rely=0.2)
    entry6=Entry(pencere20,width=30)
    entry6.place(relx=0.31,rely=0.2)
    cotanjant=Label(pencere20,text="Cotanjant")
    cotanjant.place(relx=0.0,rely=0.3)
    entry7=Entry(pencere20,width=5)
    entry7.place(relx=0.2,rely=0.3)
    esittir4=Label(pencere20,text="=")
    esittir4.place(relx=0.31,rely=0.3)
    entry8=Entry(pencere20,width=28)
    entry8.place(relx=0.35,rely=0.3)
    arcsin=Label(pencere20,text="Arcsin")
    arcsin.place(relx=0.0,rely=0.4)
    entry9=Entry(pencere20,width=5)
    entry9.place(relx=0.16,rely=0.4)
    esittir5=Label(pencere20,text="=")
    esittir5.place(relx=0.27,rely=0.4)
    entry10=Entry(pencere20,width=30)
    entry10.place(relx=0.31,rely=0.4)
    arccos=Label(pencere20,text="Arccos")
    arccos.place(relx=0.0,rely=0.5)
    entry11=Entry(pencere20,width=5)
    entry11.place(relx=0.16,rely=0.5)
    esittir6=Label(pencere20,text="=")
    esittir6.place(relx=0.27,rely=0.5)
    entry12=Entry(pencere20,width=30)
    entry12.place(relx=0.31,rely=0.5)
    arctan=Label(pencere20,text="Arctan")
    arctan.place(relx=0.0,rely=0.6)
    entry13=Entry(pencere20,width=5)
    entry13.place(relx=0.16,rely=0.6)
    esittir7=Label(pencere20,text="=")
    esittir7.place(relx=0.27,rely=0.6)
    entry14=Entry(pencere20,width=30)
    entry14.place(relx=0.31,rely=00.6)
    arccot=Label(pencere20,text="Arccot")
    arccot.place(relx=0.0,rely=0.7)
    entry15=Entry(pencere20,width=5)
    entry15.place(relx=0.16,rely=0.7)
    esittir8=Label(pencere20,text="=")
    esittir8.place(relx=0.27,rely=0.7)
    entry16=Entry(pencere20,width=30)
    entry16.place(relx=0.31,rely=0.7)
    print(entry2.get())
    def hesapla():

        try:
            entry2.delete(0, END)
            entry2.insert(0, math.sin(math.radians(entry1.getint(entry1.get()))))
        except ValueError:
            pass


        try:
            entry4.delete(0, END)
            entry4.insert(0, math.cos(math.radians(entry3.getint(entry3.get()))))
        except ValueError:
            pass


        try:
            entry6.delete(0,END)
            entry6.insert(0,math.tan(math.radians(entry5.getint(entry5.get()))))
        except ValueError:
            pass


        try:
            entry8.delete(0,END)
            entry8.insert(0,1/math.tan(math.radians(entry7.getint(entry7.get()))))
        except ValueError:
            pass

        try:
            entry10.delete(0,END)
            entry10.insert(0,math.asin(math.radians(entry9.getint(entry9.get()))))
        except ValueError:
            pass

        try:
            entry12.delete(0,END)
            entry12.insert(0,math.acos(math.radians(entry11.getint(entry11.get()))))
        except ValueError:
            pass

        try:
            entry14.delete(0,END)
            entry14.insert(0,math.atan(math.radians(entry13.getint(entry13.get()))))
        except ValueError:
            pass
        try:
            entry16.delete(0,END)
            entry16.insert(0,1/math.atan(math.radians(entry15.getint(entry15.get()))))
        except ValueError:
            pass
    buton13=Button(pencere20,text="Hesapla",command=hesapla)
    buton13.place(relx=0.6,rely=0.82)


    mainloop()



def XOR():
    def sifrele():

       try:
        if "rastgele" in entry1.get():
            uzunluk=entry1.get()[len("rastgele")+1:]
            c=0
            sifre=""
            while c<int(uzunluk):
                sifre+=chr(randint(33,126))
                c+=1
            entry1.delete(0,END)
            entry1.insert(END,sifre)



        binaries = []
        anahtarbits = []
        textbits = []
        XOR = []
        kriptedbits = []
        with open(entry.get(), "r+") as m:
            for k in m.readlines():
                for t in k:
                    binaries.append(("0" * (8 - len(bin(ord(t))[2:])) + bin(ord(t))[2:]))
        anahtar = entry1.get()
        if len(anahtar) > len(open(entry.get(), "r+").read()):
            pass
        if len(anahtar) < len(open(entry.get(), "r+").read()):
            anahtar = anahtar * int(len(open(entry.get(), "r+").read()) / len(anahtar)) + anahtar[:len(
                open(entry.get(), "r+").read()) % len(anahtar)]

        sayac = 1
        for i, k in zip(anahtar, binaries):
            for m in ("0" * (8 - len(bin(ord(i))[2:])) + str(bin(ord(i))[2:])):
                anahtarbits.append(m)
                sayac += 1
            for t in k:
                textbits.append(t)
        for i, k in zip(anahtarbits, textbits):
            if i == k:
                XOR.append("0")
            else:
                XOR.append("1")
        a = 0
        b = 8
        while b < sayac:
            a += 8
            b += 8
        sayac1 = 0
        sifreli = ""
        for i in XOR:
            sifreli += i
            sayac1 += 1
            if sayac1 == 8:
                sayac1 = 0
                kriptedbits.append(sifreli)
                sifreli = ""

        sayac2 = 0
        x = 0
        open(entry.get(), "w")
        while x < len(kriptedbits):
            i = kriptedbits[x]
            i = int(i)
            char = 0
            y = 0
            while True:
                if i == 0:
                    open(entry.get(), "a").write(chr(char))
                    sayac2 += 1
                    break
                if i < 10 ** y:
                    i -= 10 ** (y - 1)
                    char += 2 ** (y - 1)
                    y = 0

                else:
                    y += 1
            x += 1

        labe4=Label(pencere13,text="Şifrelendi!                          ")
        labe4.place(relx=0.1,rely=0.2)
        sifrelistesi.delete(0,END)
        sifrelistesi.insert(END,entry1.get())
        entry1.delete(0, END)
       except FileNotFoundError:
           label5=Label(pencere13,text="Böyle Bir Dosya Yok!")
           label5.place(relx=0.1,rely=0.2)
           entry1.delete(0,END)
    pencere13 = Toplevel()
    pencere13.title("XOR Kripto")
    pencere13.geometry("300x300+650+265")
    pencere13.resizable(width=False,height=False)
    sifrelistesi=Listbox(pencere13,width=49,height=30)
    sifrelistesi.place(relx=0.0,rely=0.3)
    label2 = Label(pencere13, text="Şifrelenecek Dosya:")
    label2.grid(row=0, column=0)
    entry = Entry(pencere13, width=30)
    entry.grid(row=0, column=1)
    label3 = Label(pencere13, text="Şifreleme Anahtarı:")
    label3.place(relx=0, rely=0.1)
    entry1 = Entry(pencere13, width=30)
    entry1.place(relx=0.36, rely=0.1)
    buton15 = Button(pencere13, text="Sifrele", command=sifrele)
    buton15.place(relx=0.8, rely=0.2)



def tekrar():
    giris1.delete(0,END)
    giris2.delete(0,END)
    pencere2 = Toplevel()
    pencere2.geometry("150x60+670+300")
    pencere2.resizable(height=False,width=False)
    bilgi1 = Label(pencere2,text="Hatalı giriş!")
    bilgi1.pack()
    buton3 = Button(pencere2,text="tamam",command=pencere2.destroy)
    buton3.pack()



def yonetkullanicilar():

    def sil():
        for g in isaretler:
            if g.get()==1:
                if users[isaretler.index(g)] in open("users.txt","r").readline():
                    with open("users.txt","r+") as w:
                        w.seek(open("users.txt", "r").readline().index(users[isaretler.index(g)]))
                        w.write(" "*len(users[isaretler.index(g)]))

                    with open("passwords.txt","r+") as p:
                        p.seek(open("passwords.txt","r").readline().index(passwords[isaretler.index(g)]))
                        p.write(" "*len(passwords[isaretler.index(g)]))


    def adminyap():
        for g in isaretler:
            if g.get()==1:
                with open("admin.txt","a") as ad:
                    ad.write(" "+open("users.txt","r").readline().split()[isaretler.index(g)])

                with open ("adminsifre.txt","a") as ads:
                    ads.write(" "+open("passwords.txt","r").readline().split()[isaretler.index(g)])

                with open("users.txt", "r+") as w:
                    w.seek(open("users.txt", "r").readline().index(users[isaretler.index(g)]))
                    w.write(" " * len(users[isaretler.index(g)]))

                with open("passwords.txt", "r+") as p:
                    p.seek(open("passwords.txt", "r").readline().index(passwords[isaretler.index(g)]))
                    p.write(" " * len(passwords[isaretler.index(g)]))



    pencere9=Toplevel()
    pencere9.geometry("300x250+400+250")

    bilgi10=Label(pencere9,text="Kullanıcı")
    bilgi11=Label(pencere9,text="Şifre")
    bilgi10.place(relx=0.005,rely=0.01)
    bilgi11.place(relx=0.32,rely=0.01)
    buton11=Button(pencere9,text="Sil",command=sil,width=10)
    buton11.place(relx=0.3,rely=0.8)
    buton12=Button(pencere9,text="Admin Yap",command=adminyap)
    buton12.place(relx=0.0,rely=0.8)
    a=0
    d=0.0
    isaretler=[]

    while a < len(users):

        b=IntVar()
        b.set(0)
        kontrol=Checkbutton(pencere9,text=users[a]+"------>"+(passwords[a]),variable=b)
        kontrol.place(relx=0.0,rely=d)
        isaretler+=[b]
        a+=1
        d+=0.1


def yonetadminler():
    def adminsil():
        with open("admin.txt", "r+") as ww:
            ww.seek(open("admin.txt", "r").readline().index(admin[isaretler2.index(u)]))
            ww.write(" " * len(admin[isaretler2.index(u)]))

        with open("adminsifre.txt", "r+") as pa:
            pa.seek(open("adminsifre.txt", "r").readline().index(adminsif[isaretler2.index(u)]))
            pa.write(" " * len(adminsif[isaretler2.index(u)]))

    def adminligial():
        for u in isaretler2:
            if u.get() == 1:
                with open("users.txt", "a") as aa:
                    aa.write(" " + open("admin.txt", "r").readline().split()[isaretler2.index(u)])

                with open("passwords.txt", "a") as aas:
                    aas.write(" " + open("adminsifre.txt", "r").readline().split()[isaretler2.index(u)])

                with open("admin.txt", "r+") as ww:
                    ww.seek(open("admin.txt", "r").readline().index(admin[isaretler2.index(u)]))
                    ww.write(" " * len(admin[isaretler2.index(u)]))

                with open("adminsifre.txt", "r+") as pa:
                    pa.seek(open("adminsifre.txt", "r").readline().index(adminsif[isaretler2.index(u)]))
                    pa.write(" " * len(adminsif[isaretler2.index(u)]))

    pencere12 = Toplevel()
    pencere12.geometry("300x250+400+250")
    pencere12.title("ADMİNLER")
    bilgi12 = Label(pencere12, text="Admin")
    bilgi13 = Label(pencere12, text="Şifre")
    bilgi12.place(relx=0.005, rely=0.01)
    bilgi13.place(relx=0.30, rely=0.01)
    buton14 = Button(pencere12, text="Sil", command=adminsil, width=10)
    buton14.place(relx=0.0, rely=0.8)
    buton15=Button(pencere12,text="Adminliği al",command=adminligial)
    buton15.place(relx=0.3,rely=0.8)
    a = 0
    h = 0.1
    isaretler2 = []

    while a < len(admin):
        u = IntVar()
        u.set(0)
        kontrol = Checkbutton(pencere12, text=open("admin.txt", "r").read().split()[a] + "------>" + "(" + open("adminsifre.txt", "r").read().split()[a] + ")", variable=u)
        kontrol.place(relx=0.0, rely=h)
        isaretler2 += [u]
        a += 1
        h += 0.1

def kullanicilar():
    pencere11 = Toplevel()
    pencere11.geometry("300x250+400+250")
    bilgi10 = Label(pencere11, text="Kullanıcı")
    bilgi11 = Label(pencere11, text="Şifre")
    bilgi10.place(relx=0.005, rely=0.01)
    bilgi11.place(relx=0.32, rely=0.01)

    a = 0
    h=0

    while a < len(users):
        b = IntVar()
        b.set(0)
        kontrol = Checkbutton(pencere11, text=users[a] + "------>" + "(" + len(passwords[a]) * "*" + ")")
        kontrol.place(relx=0.0,rely=h)
        a += 1
        h+=0.1



def yonetici():
    pencere8 = Tk()
    baslik2 = pencere8.title("YÖNETİCİ:  " + giris1.get())
    pencere8.geometry("300x100+600+250")
    pencere8.resizable(width=False, height=False)
    menu1 = Menu(pencere8)
    pencere8.config(menu=menu1)
    menuDosya = Menu(menu1, tearoff=0)
    menu1.add_cascade(label="İçindekiler", menu=menuDosya)
    menuDosya.add_command(label="XOR Şifrele",command=XOR)
    menuDosya.add_command(label="Trigonometri",command=trigonometri)
    menuDosya.add_command(label="Grafik Çizme",command=grafik)
    menuDosya.add_command(label="Adminler",command=yonetadminler)
    menuDosya.add_command(label="Kullanıcılar", command=yonetkullanicilar)
    menuDosya.add_command(label="Çıkış", command=quit)



def admingirisi():
    pencere8=Tk()
    baslik2=pencere8.title("ADMİN:  "+giris1.get())
    pencere8.geometry("300x100+600+250")
    pencere8.resizable(width=False,height=False)
    menu1 = Menu(pencere8)
    pencere8.config(menu=menu1)
    menuDosya = Menu(menu1, tearoff=0)
    menu1.add_cascade(label="İçindekiler", menu=menuDosya)
    menuDosya.add_command(label="Trigonometri",command=trigonometri)
    menuDosya.add_command(label="Kullanıcılar",command=kullanicilar)
    menuDosya.add_command(label="Çıkış", command=quit)



def uyegirisi():
    pencere10=Tk()
    baslik2=pencere10.title("KULLANICI:  "+giris1.get())
    pencere10.geometry("300x100+600+250")
    pencere10.resizable(width=False,height=False)
    bilgi9=Label(pencere10,text="Hoşgeldiniz:  "+giris1.get())
    bilgi9.pack()
    buton10=Button(pencere10,text="Tamam",command=quit)
    buton10.pack()


def giris():
    if giris1.get() in yoneticii and giris2.get() in yoneticisifre:
        yonetici()

    elif giris1.get() in admin and giris2.get()==adminsif[admin.index(giris1.get())]:
        admingirisi()

    elif giris1.get() in users and giris2.get()==passwords[users.index(giris1.get())]:
        uyegirisi()

    else:
        tekrar()


baslik=pencere1.title("Kullanıcılar")
metin1=Label(text="Kullanıcı Adı:")
metin1.place(relx=0.0,rely=0.0)
metin2=Label(text="Şifre:")
metin2.place(relx=0.0,rely=0.25)
giris1=Entry(pencere1,width=20)
giris1.place(relx=0.3,rely=0.01)
giris2=Entry(pencere1,width=20)
giris2.place(relx=0.3,rely=0.25)
buton1=Button(text="Giriş",command=giris)
buton1.place(relx=0.67,rely=0.5)
buton2=Button(text="Kayıt Ol",command=kayit)
buton2.place(relx=0.29,rely=0.5)

mainloop()