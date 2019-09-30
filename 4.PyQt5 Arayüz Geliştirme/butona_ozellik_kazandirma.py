import sys
from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget): #Pencere class ı QtWidgets modülünün içindeki QWidget sınıfını miras aldı
    def __init__(self): #QtWidgets modülünün içindeki Qwidget sınıfının __ini__() methodu override oldu
        super().__init__() #Override olan methodun özellikleri tekrar çağrıldı

        self.init_ui() #Program çalılştığında, __init__() methodu constructor method olduğundan ve ilk önce çalışıacağı için en sonda ini_ui() methodunu çalıştır dedik

    def init_ui(self):
        self.yazi = QtWidgets.QLabel() #class a yazi adında label özelliği eklendi
        self.yazi.setText("Butona daha tıklanmadı") #label e text değeri girildi
        
        self.button1 = QtWidgets.QPushButton() #class a button1 adında PushButton özelliği eklendi
        self.button1.setText("Yükselt") #button1 in text değeri girildi.

        self.button2 = QtWidgets.QPushButton()
        self.button2.setText("Azalt")
        self.say = 0

        verticalBox = QtWidgets.QVBoxLayout()
        verticalBox.addWidget(self.yazi)
        verticalBox.addWidget(self.button1)
        verticalBox.addWidget(self.button2)
        verticalBox.addStretch()

        horizontalBox = QtWidgets.QHBoxLayout()
        horizontalBox.addStretch()
        horizontalBox.addLayout(verticalBox)
        horizontalBox.addStretch()

        self.setLayout(horizontalBox)

        self.button1.clicked.connect(self.button1Clicked) #button1 objesine tıklandığında şu fonksiyonu çalıştır.
        self.button2.clicked.connect(self.button2Clicked)
        #self.setWindowTitle("Butona Özellik Kazandırma")
        #self.setGeomery(100,100,500,500)
        self.show()
    def button1Clicked(self):
        self.say+=1
        self.yazi.setText("Butona " + str(self.say) + " kere tıklandı")
    def button2Clicked(self):
            self.say -= 1
            self.yazi.setText(str(self.say))

        

app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
pencere.setWindowTitle("Butona Özellik Kazandırma")
pencere.setGeometry(100,100,500,500)
sys.exit(app.exec_())
