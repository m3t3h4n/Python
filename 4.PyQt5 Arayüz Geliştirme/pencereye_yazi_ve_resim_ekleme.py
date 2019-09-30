import sys 
from PyQt5 import QtWidgets,QtGui
#Pencerenin içinde resim tablo vs. ekleyebilmek içinde QtGui sınıfını dahil ediyoruz.

def Pencere():
    app = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("Yazı ve Resim Ekleme")
    label1 = QtWidgets.QLabel(pencere) #Pencerenin içine QtWidgets modülünün QLabel sınıfının özelliklerini taşıyan label1 objesi oluşturuldu.
    pictureBox1 = QtWidgets.QLabel(pencere) #Pencerenin içine obje oluşturmaya yarar

    pictureBox1.setPixmap(QtGui.QPixmap("img/ekrem_cakir.jpg")) #picureBox1 objesinin içine resim atmaya yarar
    pictureBox1.move(70,150) #pictureBox1 objeisinin yerini değiştirmeye yarar
    label1.setText("Bu bir yazıdır") #label1 objesinin text ini değiştirmeye yarar
    label1.move(220,30) #label1 objesinin yerini değiştirmeye yarar
    pencere.setGeometry(100,100,600,600)
    pencere.show()
    sys.exit(app.exec_())

Pencere()
