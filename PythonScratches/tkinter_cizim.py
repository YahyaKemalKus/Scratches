from tkinter import *
from tkinter import messagebox
import turtle as tt
bilgilendirme="""Koordinat istenilen yerlere (x,y) seklinde girdi verilmelidir\n
Ornek:\t35,55\nCokgen cizimi yapilirken cokgen tamamlanana kadar(ilk kenarin baslangic\
 koordinati ve son kenarin bitis koordinati ayni olana kadar) cokgenin cizim turunu degistirmeyin.
 \nCokgen tamamlandiginda ilk basta sectiginiz cokgen turune gore(orn. doldur) otomatik olarak\
  kendisi icini dolduracaktir.\nYeni bir cokgen cizmek icin cokgen cizim penceresini kapatip yeniden acin.
  \nNokta boyutu girerken de tam sayi girilmelidir.(Orn. 4)\nOrtadaki mavi nokta (0,0) baslangic koordinati\
  olarak kabul edilmelidir."""
kalem=tt.Turtle()
kalem.hideturtle()
kalem.fillcolor("blue")
kalem.begin_fill()
kalem.circle(3)
kalem.end_fill()
x_,y_=0,0
def cokgen():
    kalem.begin_fill()
    bsl_pl=""
    kenar_noktalari=[]

    def ciz():
        try:
            global x_, y_
            assert -(x_ / 2) < int(pl_kord1.get().split(",")[0]) < x_ / 2 and \
                   -(y_ / 2) < int(pl_kord1.get().split(",")[1]) < y_ / 2 and \
                   -(x_ / 2) < int(pl_kord2.get().split(",")[0]) < x_ / 2 and \
                   -(y_ / 2) < int(pl_kord2.get().split(",")[1]) < y_ / 2
            global bsl_pl
            if degisken.get()==secimler[2]:
                kalem.pensize(8)
            err_lb["text"] = ""
            kalem.penup()
            x0=int(pl_kord1.get().split(",")[0])
            y0=int(pl_kord1.get().split(",")[1])

            if cizgi_isim["text"][0]=="1":
                bsl_pl=(x0,y0)
            kalem.setpos(x0,y0)
            kalem.pendown()
            x1 = int(pl_kord2.get().split(",")[0])
            y1 = int(pl_kord2.get().split(",")[1])
            kalem.goto(x1,y1)
            kenar_noktalari.insert(0,[x1,y1])
            cizgi_isim["text"]=str(int(cizgi_isim["text"][0])+1)+cizgi_isim["text"][1:]
            pl_kord1.delete(0,END)
            pl_kord1.insert(0,pl_kord2.get())

            if bsl_pl == (x1,y1) and int(cizgi_isim["text"][0])>3:
                if degisken.get()==secimler[0]:
                    kalem.end_fill()
                pencere_pl.quit()
                kenar_noktalari.clear()

            pl_kord2.delete(0,END)
            print(kenar_noktalari)
        except AssertionError:
            err_lb["text"]="Nesne alan disinda!"
            print("nesneee")
            err_lb.place(relx=0,rely=0.3)
        except Exception as e:
            print(e)
            err_lb.place(relx=0.0,rely=0.3)
            cizgi_isim["text"] = str(int(cizgi_isim["text"][0]) - 1) + cizgi_isim["text"][1:]
            print("ff")


    def geri_al():
        if not kenar_noktalari:
            kenar_noktalari.append([0,0])

        else:
            try:
                kalem.undo()
                kalem.undo()
                kalem.undo()
                pl_kord1.delete(0,END)
                pl_kord1.insert(0,str(kenar_noktalari[1])[1:-1])
                kenar_noktalari.remove(kenar_noktalari[0])
                cizgi_isim["text"] = str(int(cizgi_isim["text"][0]) -1) + cizgi_isim["text"][1:]
            except IndexError:
                pass

    pencere_pl = Tk()
    pencere_pl.title("Cokgen")
    pencere_pl.geometry("300x400+1200+300")
    err_lb = Label(pencere_pl, text="Gecersiz koordinat.")
    pencere_pl.resizable(width=False,height=False)
    cizgi_isim = Label(pencere_pl, text="1.kenar")
    bsl = Label(pencere_pl, text="Baslangic")
    bsl.place(relx=0.17, rely=0.0)
    bts = Label(pencere_pl, text="Bitis")
    bts.place(relx=0.42, rely=0.0)
    sekil = Label(pencere_pl, text="Sekil")
    sekil.place(relx=0.69, rely=0.0)
    cizgi_isim.place(relx=0.0, rely=0.07)
    pl_kord1 = Entry(pencere_pl, width=10)
    pl_kord1.place(relx=0.17, rely=0.08)
    pl_kord2 = Entry(pencere_pl, width=10)
    pl_kord2.place(relx=0.42, rely=0.08)
    secimler = ["ici dolu", "ici bos", "kenarlari kalin"]
    degisken = StringVar(pencere_pl)
    degisken.set(secimler[0])
    secim_menu = OptionMenu(pencere_pl, degisken, *secimler)
    secim_menu.place(relx=0.67, rely=0.06)
    ciz_buton = Button(pencere_pl, command=ciz, text="ciz".center(15))
    ciz_buton.place(relx=0.67, rely=0.17)
    geri_al_bt=Button(pencere_pl,text="Geri al",command=geri_al)
    geri_al_bt.place(relx=0.67,rely=0.27)
    mainloop()


def cizgi():
    def ciz():
        try:
            global x_,y_
            assert -(x_ / 2) < int(cizgi_kord1.get().split(",")[0]) < x_ / 2 and \
                   -(y_ / 2) < int(cizgi_kord1.get().split(",")[1]) < y_ / 2 and \
                   -(x_ / 2) < int(cizgi_kord2.get().split(",")[0]) < x_ / 2 and \
                   -(y_ / 2) < int(cizgi_kord2.get().split(",")[1]) < y_ / 2

            if degisken.get()==secimler[0]:
                kalem.penup()
                x0 = int(cizgi_kord1.get().split(",")[0])
                y0 = int(cizgi_kord1.get().split(",")[1])
                kalem.setpos(x0, y0)
                kalem.pendown()
                x1 = int(cizgi_kord2.get().split(",")[0])
                y1 = int(cizgi_kord2.get().split(",")[1])
                kalem.goto(x1, y1)

            if degisken.get()==secimler[1] or degisken.get()==secimler[2]:
                x0 = int(cizgi_kord1.get().split(",")[0])
                y0 = int(cizgi_kord1.get().split(",")[1])
                x1 = int(cizgi_kord2.get().split(",")[0])
                y1 = int(cizgi_kord2.get().split(",")[1])
                uzunluk=(abs(x1-x0)**2+abs(y1-y0)**2)**0.5
                uzunluk=int(uzunluk)
                print("uzunluk",uzunluk)
                el_atl=1
                if degisken.get()==secimler[1]:
                    kalem.pensize(2)
                    parca_uzunluk=7

                if degisken.get()==secimler[2]:
                    kalem.pensize(7)
                    parca_uzunluk=2
                    el_atl=8

                parca_sayisi=uzunluk/parca_uzunluk
                parca_sayisi=int(parca_sayisi)
                artis_miktari_x=int(abs(x1-x0)/parca_sayisi)
                artis_miktari_y=int(abs(y1-y0)/parca_sayisi)
                if artis_miktari_x!=0:
                    if x0>x1 and x1<0:
                        koords_x = [i for i in range(x1,x0+artis_miktari_x, artis_miktari_x)]
                        koords_x=[*reversed(koords_x)]

                    if x0>x1 and not x1<0:
                        koords_x = [i for i in range(-x0, -(x1 + artis_miktari_x), artis_miktari_x)]

                    if x0<x1 and x0<0:
                        koords_x = [i for i in range(x0, x1 + artis_miktari_x, artis_miktari_x)]

                    if x0<x1 and not x0<0:
                        koords_x = [i for i in range(abs(x0), abs(x1 + artis_miktari_x), artis_miktari_x)]

                if artis_miktari_y!=0:
                    if y0>y1 and y1<0:
                        koords_y = [i for i in range(y1,y0+artis_miktari_y, artis_miktari_y)]
                        koords_y=[*reversed(koords_y)]

                    if y0>y1 and not y1<0:
                        koords_y = [i for i in range(-y0, -(y1 + artis_miktari_y), artis_miktari_y)]

                    if y0<y1 and y0<0:
                        koords_y = [i for i in range(y0, y1 + artis_miktari_y, artis_miktari_y)]

                    if y0<y1 and not y0<0:
                        koords_y = [i for i in range(abs(y0), abs(y1 + artis_miktari_y), artis_miktari_y)]

                if artis_miktari_x==0:
                    koords_x = [x0 for i in range(parca_sayisi)]

                if artis_miktari_y==0:
                    koords_y = [y0 for i in range(parca_sayisi)]

                kalem.penup()
                kalem.goto(x0, y0)
                kalem.pendown()
                x=1;y=1
                while x<=len(koords_y)+el_atl:
                    try:
                        kalem.goto(koords_x[x],koords_y[y])
                        kalem.penup()
                        x += el_atl
                        y += el_atl
                        kalem.goto(koords_x[x],koords_y[y])
                        kalem.pendown()
                        x+=1;y+=1
                    except IndexError:
                        break

            err_lb["text"] = ""
            cizgi_kord1.delete(0, END)
            cizgi_kord1.insert(0, cizgi_kord2.get())
            cizgi_kord2.delete(0, END)

        except AssertionError:
            err_lb["text"]="Nesne alan disinda!"
            print("nesneee")
            err_lb.place(relx=0,rely=0.3)
        except Exception as e:
            err_lb["text"]="Gecersiz koordinat."
            err_lb.place(relx=0.0, rely=0.3)

    pencere=Tk()
    pencere.title("Cizgi Cizimi")
    pencere.geometry("300x400+1200+300")
    err_lb = Label(pencere, text="Gecersiz koordinat.")
    cizgi_isim=Label(pencere,text="Cizgi")
    bsl=Label(pencere,text="Baslangic")
    bsl.place(relx=0.17,rely=0.0)
    bts = Label(pencere, text="Bitis")
    bts.place(relx=0.42,rely=0.0)
    sekil = Label(pencere, text="Sekil")
    sekil.place(relx=0.69   ,rely=0.0)
    cizgi_isim.place(relx=0.0,rely=0.07)
    cizgi_kord1=Entry(pencere,width=10)
    cizgi_kord1.place(relx=0.17,rely=0.08)
    cizgi_kord2 = Entry(pencere, width=10)
    cizgi_kord2.place(relx=0.42, rely=0.08)
    secimler=["duz","kesikli cizgi","noktali cizgi"]
    degisken = StringVar(pencere)
    degisken.set(secimler[0])
    secim_menu = OptionMenu(pencere, degisken, *secimler)
    secim_menu.place(relx=0.67,rely=0.06)
    ciz_buton=Button(pencere,command=ciz,text="ciz".center(15))
    ciz_buton.place(relx=0.67,rely=0.17)
    mainloop()



def nokta():
    def ciz():
        global n_nokta
        try:
            global x_, y_
            assert -(x_ / 2)+int(nokta_boyut.get())*2 < int(nokta_kord.get().split(",")[0]) < x_ / 2-int(nokta_boyut.get())*2 and \
                   -(y_ / 2)+int(nokta_boyut.get())*2 < int(nokta_kord.get().split(",")[1]) < y_ / 2-int(nokta_boyut.get())*2

            x=int(nokta_kord.get().split(",")[0])
            y=int(nokta_kord.get().split(",")[1])
            boyut=int(nokta_boyut.get())

            if degisken.get()==secimler[0] or degisken.get()==secimler[1]:
                if degisken.get()==secimler[0]:
                    kalem.pencolor("black")
                    kalem.fillcolor("black")

                if degisken.get() == secimler[1]:
                    kalem.pencolor("red")
                    kalem.fillcolor("red")

                kalem.penup()
                kalem.goto(x, y)
                kalem.pendown()
                kalem.begin_fill()
                kalem.circle(boyut)
                kalem.end_fill()

            if degisken.get()==secimler[2]:
                kalem.pencolor("black")
                kalem.penup()
                kalem.goto(x, y)
                kalem.pendown()
                kalem.circle(boyut)
            err_lb["text"] = ""
        except AssertionError:
            err_lb["text"]="Nesne alan disinda!"
            print("nesneee")
            err_lb.place(relx=0,rely=0.3)
        except Exception as e:
            err_lb.place(relx=0.0, rely=0.3)

    pencere = Tk()
    pencere.title("Nokta Cizimi")
    pencere.geometry("330x400+1150+300")
    err_lb = Label(pencere, text="Gecersiz koordinat.")
    nokta_isim = Label(pencere, text="Nokta")
    bsl = Label(pencere, text="Koordinat")
    bsl.place(relx=0.17, rely=0.0)
    bts = Label(pencere, text="Boyut")
    bts.place(relx=0.42, rely=0.0)
    sekil = Label(pencere, text="Sekil")
    sekil.place(relx=0.69, rely=0.0)
    nokta_isim.place(relx=0.0, rely=0.07)
    nokta_kord = Entry(pencere, width=10)
    nokta_kord.place(relx=0.17, rely=0.08)
    nokta_boyut = Entry(pencere, width=10)
    nokta_boyut.place(relx=0.42, rely=0.08)
    secimler = ["siyah nokta", "kirmizi nokta", "ici bos nokta"]
    degisken = StringVar(pencere)
    degisken.set(secimler[0])
    secim_menu = OptionMenu(pencere, degisken, *secimler)
    secim_menu.place(relx=0.67, rely=0.06)
    ciz_buton = Button(pencere,command=ciz, text="ciz".center(15))
    ciz_buton.place(relx=0.67, rely=0.17)
    mainloop()


def main():
    def alan_ciz():
        global x_,y_
        try:
            x_=int(genislik_e.get())
            y_=int(yukseklik_e.get())
            kalem.penup()
            kalem.setpos(-x_/2,-y_/2)
            kalem.pendown()
            for i in [x_,y_,x_,y_]:
                kalem.forward(i)
                kalem.left(90)
            boyut_popup.destroy()
            pencere = Tk()
            pencere.title("Cizim Nesneleri")
            pencere.geometry("280x50+100+25")
            pencere.resizable(height=False, width=False)
            nokta_bt=Button(pencere,text="Nokta",width=7,command=nokta)
            cizgi_bt=Button(pencere,text="Cizgi",width=7,command=cizgi)
            cokgen_bt=Button(pencere,text="Cokgen",width=7,command=cokgen)
            nokta_bt.place(relx=0.1,rely=0.2)
            cizgi_bt.place(relx=0.4,rely=0.2)
            cokgen_bt.place(relx=0.7,rely=0.2)
            mainloop()

        except ValueError:
            messagebox.showerror(message="Genislik ve Yukseklige tamsayi girin!!\n(Pixel x Pixel boyutudur)")
    messagebox.showinfo("Kullanim",message=bilgilendirme)
    boyut_popup = Tk()
    boyut_popup.title("Cizim Alani Boyutlari")
    boyut_popup.geometry("300x100+1200+300")
    boyut_popup.resizable(height=False, width=False)
    boyut_l=Label(boyut_popup,text="Boyut")
    genislik_l=Label(boyut_popup,text="Genislik")
    yukseklik_l=Label(boyut_popup,text="Yukseklik")
    x_l=Label(boyut_popup,text="x")
    genislik_e=Entry(boyut_popup,width=8)
    yukseklik_e=Entry(boyut_popup,width=8)
    btn=Button(boyut_popup,text="Onayla",command=alan_ciz)
    boyut_l.place(relx=0.05,rely=0.22)
    genislik_l.place(relx=0.23,rely=0.0)
    yukseklik_l.place(relx=0.48,rely=0.0)
    x_l.place(relx=0.43,rely=0.25)
    genislik_e.place(relx=0.23,rely=0.25)
    yukseklik_e.place(relx=0.48,rely=0.25)
    btn.place(relx=0.73,rely=0.21)
    mainloop()


if __name__ == '__main__':
    main()