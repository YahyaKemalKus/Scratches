from urllib.request import *
import re
"""
Henuz bitmemis bir uygulama
"""
site=urlopen("https://www.sabah.com.tr/")
kod_satirlari=[]
linkler=[]
basliklar=[]
for kod in site :
    satir_string=kod.decode()
    eslesme2=re.findall("<a href=(.*?)target",satir_string)
    if  eslesme2 and re.search("title",eslesme2[0]) and not re.search("http",eslesme2[0]):
        if not eslesme2[0][1:len(eslesme2[0])-2] in kod_satirlari:
            kod_satirlari.append(eslesme2[0][1:len(eslesme2[0])-2])
for satir in kod_satirlari:
    linkler.append(satir.split("title=")[0][:len(satir.split("title=")[0])-2])
    basliklar.append(satir.split("title=")[1][1:])
from tkinter import *
pencere=Tk()
bolum1=Frame(pencere)
bolum1.place(relx=0,rely=0)
pencere.geometry("1680x830+0+0")
scroll_bar=Scrollbar(bolum1)
baslik_listesi=Listbox(bolum1,width=75,height=43,font=("arial",12))
scroll_bar.pack(fill=Y,side=RIGHT)
baslik_listesi.pack(side=LEFT,fill=Y)
scroll_bar.config(command=baslik_listesi.yview)
baslik_listesi.config(yscrollcommand=scroll_bar.set)
bolum2=LabelFrame(pencere,height=43)
bolum2.place(relx=0.47,rely=0.15)

for i in basliklar:
    baslik_listesi.insert(END,i)
    baslik_listesi.insert(END,"\n")
metinn=Label(text="asd")
buton2=Button()
icerik=""
basliklar_=[]
def link_ac(index):
    global metinn,icerik,buton2,basliklar_
    def onceki_sayfa(icerik):
        metinn['text'] = icerik[:2100]
        metinn.pack(side=TOP)
        buton2['text'] = "Sonraki Sayfa"
        buton2.place(relx=0.9)
        buton2['command'] = lambda: sonraki_sayfa(icerik)
    def sonraki_sayfa(icerik):
        metinn['text'] = icerik[2100:]
        metinn.pack(side=TOP)
        buton2['text'] = "Onceki Sayfa"
        buton2.place(relx=0.5)
        buton2['command']=lambda :onceki_sayfa(icerik)
    if index%2==0:
        if basliklar_:
            for baslk in basliklar_:
                baslk.destroy()
        baslik=basliklar[int(index/2)].title()
        if len(baslik)>64:
            duzenleme=[" ".join(baslik.split(" ")[t:t+6])for t in range(0,len(baslik.split(" ")),6)]
            y_=0
            for parca in duzenleme:
                baslik1_ = Label(pencere, text=parca, font=("Helvetica BOLD", 20))
                baslik1_.place(relx=0.47, rely=y_)
                basliklar_.append(baslik1_)
                y_+=0.04
        elif len(baslik)<=64:
            baslik1_ = Label(pencere, text=baslik, font=("Helvetica BOLD", 20))
            baslik1_.place(relx=0.47, rely=0)
            basliklar_.append(baslik1_)
        haber_link=urlopen("https://www.sabah.com.tr"+linkler[int(index/2)])
        metinn.destroy()
        for i in haber_link:
            if re.findall("articleBody(.*?)",i.decode()):
                metin=i.decode()[23:len(i.decode())-5]
                icerik=""
                for satirr in range(0,len(metin),80):
                    icerik+=metin[satirr:satirr+80]+"\n"
                if len(icerik)>2100:
                    metinn = Label(bolum2, text=icerik[:2100], font=("arial", 15))
                    metinn.pack(side=TOP)
                    buton2=Button(pencere,text="Sonraki Sayfa",command=lambda :sonraki_sayfa(icerik))
                    buton2.place(relx=0.9,rely=0.95)
                else:
                    metinn = Label(bolum2, text=icerik, font=("arial", 15))
                    metinn.pack(side=LEFT)
                    if buton2:
                        buton2.destroy()

buton=Button(pencere,text="haberi oku",command=lambda :link_ac(baslik_listesi.curselection()[0]))
buton.place(relx=0.455,rely=0.95)
pencere.mainloop()

