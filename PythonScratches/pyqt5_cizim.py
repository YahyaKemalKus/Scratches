from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import *
"""Cizgi cizmek icin ilk kutucuga baslangic koordinat(x,y),ikinci kutucuga varis koordinati(x,y) seklinde giriniz.
Cokgen cizmek icin oncelikle cokgen girdi kutucuguna kenar sayisini belirtin.Belirtilmezse default olarak 3 degerini
kabul edecektir.Kenar sayisini yazdiktan sonra ekle butonu ile kose koordinatlarini gireceginiz bir pencere acilacaktir.
Kose koordinatlari girdikten sonra onayla butonuna basiniz.Daha sonra ne sekilde cizmek istediginizi dropdown menulerden seciniz.
Ciz butonuna basarak ozelliklerini girdiginiz cokgeni cizebilirsiniz."""
import sys

class Cokgen_pencere(QMainWindow):
    def __init__(self,kenar_sayisi, parent=None):
        super(Cokgen_pencere, self).__init__(parent)
        self.kenar_sayisi=kenar_sayisi
        self.yukseklik =kenar_sayisi * 50+50
        self.girdi_list = []
        self.initUI()
        self.girdi_uretici()
        self.text_uretici()

    def initUI(self):
        self.setGeometry(800,300,265,self.yukseklik)
        self.setWindowTitle("Cokgen")

        onay_buton=QPushButton("Onayla",self)
        onay_buton.clicked.connect(lambda :self.get_koords())
        onay_buton.move(75,self.yukseklik-50)

    def get_koords(self):
        koords=[]
        try:
            for x,y in self.girdi_list:
                x0=int(x.text())
                y0=int(y.text())
                koords.insert(0,(x0,y0))
        except IndexError:
            pass
        except ValueError:
            pass
        return koords


    def girdi_uretici(self):
        for i in range(self.kenar_sayisi):
            tmp_girdi1 = QLineEdit(self)
            tmp_girdi1.setPlaceholderText("x")
            tmp_girdi1.resize(55,30)
            tmp_girdi1.move(110,i*50)
            tmp_girdi2 = QLineEdit(self)
            tmp_girdi2.setPlaceholderText("y")
            tmp_girdi2.resize(55,29)
            tmp_girdi2.move(175,i*50)
            self.girdi_list.insert(0,(tmp_girdi1,tmp_girdi2))


    def text_uretici(self):
        for i in range(1,self.kenar_sayisi+1):
            tmp_text=QLabel(f"{i}.kose noktasi:",self)
            tmp_text.move(10,(i-1)*50)


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.tuval=None
        self.tuval_genislik=None
        self.tuval_yukseklik=None
        self.merkez_x_fark=None
        self.merkez_y_fark=None
        self.initUI()
        self.tuval_boyut()
        self.noktalar = []
        self.cizgiler = []
        self.cokgen_wd=None
        self.cokgen_index=0
        self.cokgenler = []
        self.cokgen_kenar_koords=[]

    def tuval_boyut(self):
        while True:
            text, okPressed = QInputDialog.getText(self, "Tuval", "Tuval Boyutu", QLineEdit.Normal, "genislik,yukseklik")
            if okPressed :
                try:
                    self.tuval_genislik=int(text.split(",")[0])
                    self.tuval_yukseklik=int(text.split(",")[1])
                    self.tuval = Tuval(self.tuval_genislik,self.tuval_yukseklik)
                    self.merkez_x_fark=int((1920-self.tuval_genislik)/2)
                    self.merkez_y_fark=int((1080-self.tuval_yukseklik)/2)
                    self.tuval.show()
                    self.show()
                    break
                except ValueError:
                    pass
                except IndexError:
                    pass
            else:
                sys.exit()

    def tuvalde_mi(self,x,y):
        tuval_top = int((1080 - self.tuval_yukseklik) / 2)
        tuval_left = int((1920 - self.tuval_genislik) / 2)
        kosul1=x in range(tuval_left,tuval_left+self.tuval_genislik)
        kosul2=y in range(tuval_top,tuval_top+self.tuval_yukseklik)
        if kosul1 and kosul2:
            return True
        else:
            return False

    def initUI(self):
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle("sekiller")
        # self.setGeometry(self.left, self.top, self.width, self.height)
        self.nokta_buton = QPushButton('Ciz', self)  # selfye buton tanimlandi
        self.nokta_buton.clicked.connect(lambda: self.nokta_olusturucu())  # butona tiklandiginda calisacak fonksiyon tanimlandi.
        self.nokta_buton.move(375, 0)  # buton 300,0 noktasina yerlestirildi.

        self.nokta_isim = QLabel("Nokta", self)  # Nokta isimli bir yazi tanimlandi.
        self.nokta_isim.move(10, 0)  # selfye yerletirildi.

        self.nokta_boyut_menu = QComboBox(self)  # bir dropdown menu tanimlandi
        boyutlar = ["Kucuk Boy", "Orta Boy", "Buyuk Boy"]
        [self.nokta_boyut_menu.addItem(boyut) for boyut in boyutlar]
        self.nokta_boyut_menu.resize(90, 29)  # dropdown menunun boyutlari ayarlandi
        self.nokta_boyut_menu.move(275, 0)  # selfye yerlestirildi.

        renkler = ["Siyah", "Mavi", "Kirmizi"]
        self.nokta_renk_menu = QComboBox(self)
        [self.nokta_renk_menu.addItem(renk) for renk in renkler]
        self.nokta_renk_menu.resize(75, 29)
        self.nokta_renk_menu.move(185, 0)

        self.nokta_koord = QLineEdit(self)  # girdi alma kutusu tanimlandi.
        self.nokta_koord.setPlaceholderText("koord(x,y)")
        self.nokta_koord.resize(125, 29)
        self.nokta_koord.move(50, 0)  # selfye yerletirildi.

        self.cizgi_isim = QLabel("Cizgi", self)
        self.cizgi_isim.move(10, 100)

        self.cizgi_koord1 = QLineEdit(self)
        self.cizgi_koord1.setPlaceholderText("baslngc")
        self.cizgi_koord1.resize(55, 29)
        self.cizgi_koord1.move(50, 100)

        self.cizgi_koord2 = QLineEdit(self)
        self.cizgi_koord2.setPlaceholderText("bitis")
        self.cizgi_koord2.resize(60, 29)
        self.cizgi_koord2.move(112, 100)

        self.cizgi_renk_menu = QComboBox(self)
        [self.cizgi_renk_menu.addItem(renk) for renk in renkler]
        self.cizgi_renk_menu.resize(75, 29)
        self.cizgi_renk_menu.move(185, 100)

        sekiller = ["Duz", "Kesikli", "Noktali"]
        self.cizgi_sekil_menu = QComboBox(self)
        [self.cizgi_sekil_menu.addItem(sekil) for sekil in sekiller]
        self.cizgi_sekil_menu.resize(90, 29)
        self.cizgi_sekil_menu.move(275, 100)

        self.cizgi_buton = QPushButton('Ciz', self)
        self.cizgi_buton.clicked.connect(lambda: self.cizgi_olusturucu())
        self.cizgi_buton.move(375, 100)

        self.cokgen_isim = QLabel("cokgen", self)
        self.cokgen_isim.move(4, 200)

        self.cokgen_kenar_say = QLineEdit(self)
        self.cokgen_kenar_say.setPlaceholderText("Kenar Sayisi:3")
        self.cokgen_kenar_say.resize(125, 29)
        self.cokgen_kenar_say.move(50, 200)

        self.cokgen_renk_menu = QComboBox(self)
        [self.cokgen_renk_menu.addItem(renk) for renk in renkler]
        self.cokgen_renk_menu.resize(75, 29)
        self.cokgen_renk_menu.move(185, 200)

        stiller = ["Duz Kenar", "Cizgili Kenar", "Noktali Kenar"]
        self.cokgen_sekil_menu = QComboBox(self)
        [self.cokgen_sekil_menu.addItem(stil) for stil in stiller]
        self.cokgen_sekil_menu.resize(90, 29)
        self.cokgen_sekil_menu.move(275, 200)

        self.cokgen_buton = QPushButton('Ekle', self)
        self.cokgen_buton.clicked.connect(lambda: self.cokgen_kenar_ekleyici())
        self.cokgen_buton.move(375, 200)

        self.cokgen_buton_ciz = QPushButton('Ciz', self)
        self.cokgen_buton_ciz.clicked.connect(lambda: self.cokgen_olusturucu())
        self.cokgen_buton_ciz.move(375, 250)

    def cokgen_kenar_ekleyici(self):
        kenar_sy = 3
        if self.cokgen_kenar_say.text():
            try:
                kenar_sy = int(self.cokgen_kenar_say.text())
            except ValueError:
                pass
        self.cokgen_wd = Cokgen_pencere(kenar_sy)
        self.cokgen_wd.show()

    def nokta_olusturucu(self):
        sozluk = {"Kucuk Boy": 3, "Orta Boy": 8, "Buyuk Boy": 13, "Siyah": 1, "Mavi": 2, "Kirmizi": 3}

        if self.nokta_koord.text() and self.nokta_koord.text():

            try:
                koord_x = int(self.nokta_koord.text().split(",")[0])+self.merkez_x_fark
                koord_y = int(self.nokta_koord.text().split(",")[1])+self.merkez_y_fark
                if self.tuvalde_mi(koord_x,koord_y):
                    boy = sozluk.get(self.nokta_boyut_menu.currentText())
                    renk = sozluk.get(self.nokta_renk_menu.currentText())
                    self.noktalar.insert(0, (koord_x, koord_y, boy, renk))
            except ValueError:
                pass
        self.tuval.noktalar=self.noktalar

    def cizgi_olusturucu(self):
        sozluk={"Duz":1,"Kesikli":2,"Noktali":3,"Siyah":1,"Mavi":2,"Kirmizi":3}
        if self.cizgi_koord1.text() and self.cizgi_koord2.text():
            try:
                x0=int(self.cizgi_koord1.text().split(",")[0])+self.merkez_x_fark
                y0=int(self.cizgi_koord1.text().split(",")[1])+self.merkez_y_fark
                x1=int(self.cizgi_koord2.text().split(",")[0])+self.merkez_x_fark
                y1=int(self.cizgi_koord2.text().split(",")[1])+self.merkez_y_fark
                if self.tuvalde_mi(x0,y0) and self.tuvalde_mi(x1,y1):
                    sekil=sozluk.get(self.cizgi_sekil_menu.currentText())
                    renk=sozluk.get(self.cizgi_renk_menu.currentText())
                    self.cizgiler.insert(0,(x0,y0,x1,y1,sekil,renk))
            except ValueError:
                pass
        self.tuval.cizgiler=self.cizgiler

    def cokgen_olusturucu(self):
            sozluk={"Duz Kenar":1, "Cizgili Kenar":2, "Noktali Kenar":3,"Siyah":1,"Mavi":2,"Kirmizi":3}
            try:
                koords=[(koord[0]+self.merkez_x_fark,koord[1]+self.merkez_y_fark) for koord in self.cokgen_wd.get_koords()]
                if all([self.tuvalde_mi(koord[0],koord[1]) for koord in koords]):
                    sekil=sozluk.get(self.cokgen_sekil_menu.currentText())
                    renk=sozluk.get(self.cokgen_renk_menu.currentText())
                    self.cokgenler.insert(0,(koords,sekil,renk))
            except ValueError:
                pass

            self.tuval.cokgenler=self.cokgenler


class Tuval(QMainWindow):
    def __init__(self,genislik,yukseklik):
        super().__init__()
        self.setGeometry(0, 0, 1920, 1080)
        self.genislik=genislik
        self.yukseklik=yukseklik
        self.tuval_top=int((1080-yukseklik)/2)
        self.tuval_left=int((1920-genislik)/2)
        self.setWindowTitle("Tuval")
        self.noktalar = []
        self.cizgiler = []
        self.cokgen_wd = None
        self.cokgen_index = 0
        self.cokgenler = []
        self.cokgen_kenar_koords = []

    def nokta_cizici(self, qp,x,y,boy,renk):
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        pen.setWidth(boy)
        if renk==1:
            pen.setColor(Qt.black)
        if renk==2:
            pen.setColor(Qt.blue)
        if renk==3:
            pen.setColor(Qt.red)
        qp.setPen(pen)
        qp.drawPoint(x,y)

    def cizgi_cizici(self,qp,x0,y0,x1,y1,sekil,renk):
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        if sekil==1:
            pen.setStyle(Qt.SolidLine)
        if sekil==2:
            pen.setStyle(Qt.DashLine)
        if sekil==3:
            pen.setStyle(Qt.DotLine)
        if renk == 1:
            pen.setColor(Qt.black)
        if renk == 2:
            pen.setColor(Qt.blue)
        if renk == 3:
            pen.setColor(Qt.red)
        qp.setPen(pen)
        qp.drawLine(x0, y0, x1, y1)

    def cokgen_cizici(self,qp,koord_list,sekil,renk):
        pen = QPen(Qt.black, 2, Qt.SolidLine)

        if renk == 1:
            pen.setColor(Qt.black)
        if renk == 2:
            pen.setColor(Qt.blue)
        if renk == 3:
            pen.setColor(Qt.red)
        if sekil==1:
            pen.setStyle(Qt.SolidLine)
        if sekil==2:
            pen.setStyle(Qt.DashLine)
        if sekil==3:
            pen.setStyle(Qt.DotLine)
        try:
            koseler=QPolygon([QPoint(kose[0],kose[1]) for kose in koord_list])
            qp.setPen(pen)
            qp.drawPolygon(koseler)
        except Exception:
            pass

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        [self.nokta_cizici(qp, l[0], l[1], l[2], l[3]) for l in self.noktalar]
        [self.cizgi_cizici(qp, l[0], l[1], l[2], l[3], l[4], l[5]) for l in self.cizgiler]
        [self.cokgen_cizici(qp, l[0], l[1], l[2]) for l in self.cokgenler]
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        qp.setPen(pen)
        qp.drawRect(self.tuval_left, self.tuval_top, self.genislik,self.yukseklik)
        qp.end()
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main=Main()
    sys.exit(app.exec_())