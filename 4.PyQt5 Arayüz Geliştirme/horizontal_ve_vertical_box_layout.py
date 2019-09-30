import sys
from PyQt5 import QtWidgets
#horizontalboxlayout objeleri yatay olarak yerleştirdiğimiz verticalboxlayout ise objeleri dikey olarak yerleştirdiğimiz nesnelerdir.


def Pencere():
    app = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("Horizontal and Vertical Boxlayout")
    btnTamam = QtWidgets.QPushButton("Tamam") #İlk önce butonlar oluşturuldu ve isimleri verildi.
    btnIptal = QtWidgets.QPushButton("İptal")

    # horizontal_box = QtWidgets.QHBoxLayout() #Bir horizontal_box adında QtWidgets modülünün içindeki QHBoxLayout sınıfına ait özellikleri taşıyan obje eklendi
    # horizontal_box.addWidget(btnTamam) #Oluşturulan buton objelerini addWidget sınıfıyla, oluşturulan horizontal_box objesinin içine atıyoruz
    # horizontal_box.addWidget(btnIptal)
    # horizontal_box.addStretch() #horizontalboxlayout nesnesini sola yasladı.Eğer addStretch sınıfı horizontal_box objesi oluşturulduktan sonra kullanılsaydı horizontallayoutbox nesnesini sağa yaslayacaktı.

    horizontal_box = QtWidgets.QHBoxLayout() #ilk önce horizontal_box objesi oluşturuldu
    horizontal_box.addStretch() #oluşturulan objenin üstüne addStretch sınıfı ile bir boşluk eklendi.
    horizontal_box.addWidget(btnTamam) #oluşturulan vertical_box içine addWidget sınıfı ile oluşturulan buton objeleri eklendi
    horizontal_box.addWidget(btnIptal)

    vertical_box = QtWidgets.QVBoxLayout() #vertical_box objesi oluşturuldu
    vertical_box.addStretch() #oluşturulan objenin sol tarafına addStretch sınıfı ile boşluk eklendi
    vertical_box.addLayout(horizontal_box) #oluşturulan vertical_box içine addLayout ile, oluşturulan horizontal_box layoutu eklendi

    
    #Görüldüğü gibi layout lar iç içe kullanılabilir.

    pencere.setLayout(vertical_box) #pencere objesinin içine setLayout sınıfı ile oluşturulan vertical_box nesnesi eklendi.
    pencere.setGeometry(100,100,500,500)
    pencere.show()
    sys.exit(app.exec_())
Pencere()    


