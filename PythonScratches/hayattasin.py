from tkinter import Tk,Entry,Label,Button,mainloop
import tkinter.messagebox


def hayatta_kalma_suresi():
    pencere=Tk()
    pencere.geometry("250x100+630+300")
    pencere.resizable(0,0)
    gun_s=Label(text="Gün:")
    gun_s.grid(row=0,column=0)
    ay_s = Label(text="Ay:")
    ay_s.grid(row=0, column=2)
    yil_s=Label(text="Yıl:")
    yil_s.grid(row=0,column=4)
    gun=Entry(width=7)
    gun.grid(row=0,column=1)
    ay = Entry(width=7)
    ay.grid(row=0, column=3)
    yil=Entry(width=7)
    yil.grid(row=0,column=5)
    gunler={"Monday":"Pazartesi","Tuesday":"Salı","Wednesday":"Çarşamba",
            "Thursday":"Perşembe","Friday":"Cuma","Saturday":"Cumartesi",
            "Sunday":"Pazar"}


    def hesapla():
        from datetime import datetime
        try:

            yill,ayy,gunn=int(yil.get()),int(ay.get()),int(gun.get())
            sure=datetime.now()-datetime(yill,ayy,gunn)
            gun_adi=gunler[str(datetime(yill,ayy,gunn).strftime("%A"))]
            gun_say=str(sure.days)
            saat_say=str(int(gun_say)*24)
            dakika_say=str(int(saat_say)*60)
            saniye_say=str(int(dakika_say)*60)
            tkinter.messagebox.showinfo("Earth Survival","Doğum günün:"+gun_adi+"\n"
                                        "Hayatta olduğun gün sayısı:"+gun_say+"\n"+
                                        "Hayatta olduğun saat sayısı:"+saat_say+"\n"+
                                        "Hayatta olduğun dakika sayısı:"+dakika_say+"\n"+
                                        "Hayatta olduğun saniye sayısı:"+saniye_say+"\n"+
                                        "Tebrikler!,"+str(sure.days)+" gündür hayattasın."
                                        )

        except ValueError:
            tkinter.messagebox.showerror("Kullanım Hatası","Lutfen dogum tarihinizi dogru girin.")

    buton=Button(text="Hesapla",command=hesapla)
    buton.grid(row=2,column=3)
    mainloop()


if __name__ == '__main__':
    hayatta_kalma_suresi()