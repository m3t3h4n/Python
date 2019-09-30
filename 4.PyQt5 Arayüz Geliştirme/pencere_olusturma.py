import sys #Uygulamayı komut satırından çalıştıracağımız için ve komut satırından argümanlar göndereceğimiz için sys modülünü import ediyoruz.
from PyQt5 import QtWidgets #İndirilip kurulan PyQt5 modülünü kullanmak için PyQt5 modülünü import ediyoruz.
#Pencere vs. özelliklerini de kullanaiblmek için ise PyQt5 modülünün QtWidgets Sınıfını dahil ediyoruz.

def Pencere():
    app = QtWidgets.QApplication(sys.argv) #PyQt5 projelerinde mutlaka uygulama objesinin olması gerek.Ve sys.argv ile komut satırından çalıştırılıcak argümanlar gönderilmeli
    pencere = QtWidgets.QWidget() #PyQt5 Programı içinde de bir pencere oluşturmak için QtWisgets in içindeki QtWidget sınıfından pencere objesi oluşturulmalı.
    pencere.setWindowTitle("İlk python pencerem") #Pencereye isim vermek için
    pencere.setGeometry(100,100,600,600) #Pencere açılmadan önce, açılacağı konum ve büyüklüğü ayarlamamızı sağlar.İlk iki değer pencerenin nereden başlayacağı,son iki değer ise pencerenin büyüklük değeridir.
    pencere.show() #Pencereyi açmak için.
    sys.exit(app.exec_())#Pencerenin sürekli açık kalması için bir döngüye giriyor.Pencere kaptılmadığı sürece uygulamayı çalışır durumda bırakır.
#Yukarıdaki fonksiyon her PyQt5 projesinde pencere açılması için, olması gereken bir iskelet.
Pencere()
