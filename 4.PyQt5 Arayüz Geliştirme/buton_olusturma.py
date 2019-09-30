import sys
from PyQt5 import QtWidgets

def Pencere():
    app = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("Buton Oluşturma")
    button1 = QtWidgets.QPushButton(pencere) #pencerenin içine QtWidgets modülünün QPushButton sınıfının özelliklerini taşıyan button1 objesi olusturulması
    button1.setText("Tamam") #button1 objesinin textini değiştirmeye yarar
    button1.move(30,50)

    label1 = QtWidgets.QLabel(pencere)
    label1.setText("Bu bir butondur")
    label1.move(30,20)
    
    pencere.setGeometry(100,100,600,600)
    pencere.show()
    sys.exit(app.exec_())
Pencere()
