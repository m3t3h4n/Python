import sys #Uygulamayı komut satırından çalıştıracağımız için ve komut satırından argümanlar göndereceğimiz
#için sys modülünü import ediyoruz.
from PyQt5 import QtWidgets,QtGui #İndirilip kurulan PyQt5 modülünü kullanmak için PyQt5 modülünü import ediyoruz.
#Pencere vs. özelliklerini de kullanaiblmek için ise PyQt5 modülünün QtWidgets Sınıfını dahil ediyoruz.
#Pencerenin içinde resim tablo vs. ekleyebilmek içinde QtGui sınıfını dahil ediyoruz.

def Pencere():
    app = QtWidgets.QApplication(sys.argv) #PyQt5 projelerinde mutlaka uygulama objesinin olması gerek.Ve sys.argv ile komut satırından çalıştırılıcak argümanlar gönderilmeli
    pencere = QtWidgets.QWidget() #PyQt5 Programı içinde de bir pencere oluşturmak için QtWisgets in içindeki QtWidget sınıfından pencere objesi oluşturulmalı.
    pencere.setWindowTitle("İlk python pencerem") #Pencereye isim vermek için
    label1 = QtWidgets.QLabel(pencere) #Pencerenin içine label atmaya yarar.
    pictureBox1 = QtWidgets.QLabel(pencere) #Pencerenin içine bir nesne attı

    pictureBox1.setPixmap(QtGui.QPixmap("img/ekrem_cakir.jpg")) #Pencerenin içine resim attı.
    pictureBox1.move(70,150) #pictureBox1 objeisinin yerini değiştirmeye yarar
    label1.setText("Bu bir yazıdır") #Labelin textini değiştirmeye yarar.
    label1.move(220,30) #Labelin yerini değiştirmeye yarar.
    pencere.setGeometry(100,100,600,600) #Pencere açılmadan önce, açılacağı konum ve büyüklüğü ayarlamamızı sağlar.İlk iki değer pencerenin nereden başlayacağı,son iki değer ise pencerenin büyüklük değeridir.
    pencere.show() #Pencereyi açmak için.
    sys.exit(app.exec_())#Pencerenin sürekli açık kalması için bir döngüye giriyor.Pencere kaptılmadığı sürece uygulamayı çalışır durumda bırakır.
#Yukarıdaki blok her PyQt5 projesinde olması gereken bir iskelet.
Pencere()
