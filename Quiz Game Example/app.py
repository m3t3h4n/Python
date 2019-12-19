from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QMessageBox, QTableWidget, QTableWidgetItem # MessageBox oluşturuabilmek için QWidget, QPushButton ve QMessageBox modullerini dahil ettik
from PyQt5 import uic
import sys
import random
from functools import partial #Buttonun clicked.connect özelliğine yazılan fonksiyonun parametre alabilmesi için bu modül dahil edildi.
import mysql.connector
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import threading #threading modülünün timer özelliğini kullanabilmek için ve iki işlemide aynı anda yapabilmek için bu modül dahil edildi. Kullanamadım :'(

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('acilis.ui', self)

        self.btnBasla.clicked.connect(self.basla)
        self.btnSoruEkle.clicked.connect(self.soruEkle_Duzenle_Sil)
        self.btnCikis.clicked.connect(self.cikis)
        
    def basla(self):
        self.sorularYaz = SoruYaz()
        self.sorularYaz.show()
    
    def soruEkle_Duzenle_Sil(self):
        self.soru_ekle = SoruEkle_Duzenle_Sil()
        self.soru_ekle.show()
    
    def cikis(self):
        sys.exit()

class SoruGetir():
    def __init__(self):
        super(SoruGetir, self).__init__()
    i = 0
    def soruGetir(self):
        self.i +=1
        connection=mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'sorulardb'
        )
        imlec = connection.cursor()
        imlec.execute("select * from sorular")
        sonuc = imlec.fetchall()
        
        return sonuc

class SoruYaz(QMainWindow):
    def __init__(self):
        super(SoruYaz, self).__init__()
        uic.loadUi('sorular.ui', self)
        
        self.labelDisabled()
        self.soru_yaz()
        self.btnA.clicked.connect(partial(self.kontrol, "a"))
        self.btnB.clicked.connect(partial(self.kontrol, "b"))
        self.btnC.clicked.connect(partial(self.kontrol, "c"))
        self.btnD.clicked.connect(partial(self.kontrol, "d"))
        self.lblSoruSayisi.setText("1")

    soruSayisi = 1
    def soruAl(self):
        sorular=SoruGetir()
        self.soru_sayisi = len(sorular.soruGetir())
        if self.soruSayisi <= self.soru_sayisi: #sorular.Sorugetir() objesinin uzunluğunu kontrol edip hatanın önüne geçmek için bu koşul kullanıldı
            self.demet = sorular.soruGetir()[self.soruSayisi-1]
            self.soru = self.demet[1]
            self.a = self.demet[2]
            self.b = self.demet[3]
            self.c = self.demet[4]
            self.d = self.demet[5]
            self.dogruCevap = self.demet[6]

        return self.soru_sayisi, self.soru, self.a, self.b, self.c, self.d, self.dogruCevap

    i = 0
    def soru_yaz(self):
        self.sorular = self.soruAl()
        if self.sorular[0] >= self.soruSayisi:
            self.i+=1
            print(self.i)
            
            self.lblSoru.setText(self.demet[1])
            self.btnA.setText(self.demet[2])
            self.btnB.setText(self.demet[3])
            self.btnC.setText(self.demet[4])
            self.btnD.setText(self.demet[5])
            return
            
        else:
            print("Sorular Bitti")
            self.buttonControl(False)
            print("Tebrikler. 1.000.000 TL Kazandınız...")
            buttonReply = QMessageBox.question(self, 'Tebrikler', "Tebrikler. 1.000.000 TL Kazandınız... Yeni oyun oynamak ister misiniz?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if buttonReply == QMessageBox.Yes:
                print('Yeni oyun başlıyor....')
                self.soruSayisi = 1
                self.i = 0
                self.lblPuan.setText("")
                self.lblSoruSayisi.setText(str(self.soruSayisi))
                self.soru_yaz()
                self.buttonControl(True)
                self.labelSifirla()
                self.labelDisabled()
            else:
                print('No clicked.')
    
    def kontrol(self, b):
        if self.soruAl()[6] == b:
            print("Doğru Cevap")
            self.labelRenkelendir()
            self.lblPuan.setText(str(self.puan()))
            self.soruSayisi +=1
            self.lblSoruSayisi.setText(str(self.soruSayisi))
            print("Soru Sayısı " ,self.soruSayisi)
            self.soru_yaz()
        else:
            self.buttonControl(False)
            if self.soruSayisi == 1: #İlk soru için, yanlış cevap verilince hiç özdül kazanamadığını belirten koşul
                buttonReply = QMessageBox.question(self, "Kaybettiniz...", "Hiç ödül kazanamadınız. Tekrar oynamak ister misiniz?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if buttonReply == QMessageBox.Yes:
                    print('Yeni oyun başlıyor....')
                    self.soruSayisi = 1
                    self.i = 0
                    self.lblPuan.setText("")
                    self.lblSoruSayisi.setText(str(self.soruSayisi))
                    self.soru_yaz()
                    self.buttonControl(True)
                    self.labelSifirla()
                    self.labelDisabled()
                else:
                    print('No clicked.')
            else: #2 ve 2 den sorular için yanlış cevap verilince ne kadar ödül kazanacağını belirtecek koşul
                buttonReply = QMessageBox.question(self, 'Kaybettiniz...', "Yanlış Cevap. Ödülünüz "+ self.lblPuan.text()+ " TL. Tekrar oynamak ister misiniz?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if buttonReply == QMessageBox.Yes:
                    print('Yeni oyun başlıyor....')
                    self.soruSayisi = 1
                    self.i = 0
                    self.lblPuan.setText("")
                    self.lblSoruSayisi.setText(str(self.soruSayisi))
                    self.soru_yaz()
                    self.buttonControl(True)
                    self.labelSifirla()
                    self.labelDisabled()
                else:
                    print('No clicked.')
            
    def buttonControl(self, tF):
        self.btnA.setEnabled(tF)
        self.btnB.setEnabled(tF)
        self.btnC.setEnabled(tF)
        self.btnD.setEnabled(tF)
    def labelDisabled(self):
        self.lbl500.setEnabled(False)
        self.lbl1000.setEnabled(False)
        self.lbl2000.setEnabled(False)
        self.lbl3000.setEnabled(False)
        self.lbl5000.setEnabled(False)
        self.lbl7500.setEnabled(False)
        self.lbl15000.setEnabled(False)
        self.lbl30000.setEnabled(False)
        self.lbl60000.setEnabled(False)
        self.lbl125000.setEnabled(False)
        self.lbl250000.setEnabled(False)
        self.lbl1000000.setEnabled(False)
    def labelRenkelendir(self):
        if self.soruSayisi == 1:
            self.lbl500.setEnabled(True)
            self.lbl500.setStyleSheet("QLabel#lbl500 {background: green; color: white}")
        elif self.soruSayisi == 2:
            self.lbl1000.setEnabled(True)
            self.lbl1000.setStyleSheet("QLabel#lbl1000 {background: green; color: white}")
        elif self.soruSayisi == 3:
            self.lbl2000.setEnabled(True)
            self.lbl2000.setStyleSheet("QLabel#lbl2000 {background: green; color: white}")
        elif self.soruSayisi == 4:
            self.lbl3000.setEnabled(True)
            self.lbl3000.setStyleSheet("QLabel#lbl3000 {background: green; color: white}")
        elif self.soruSayisi == 5:
            self.lbl5000.setEnabled(True)
            self.lbl5000.setStyleSheet("QLabel#lbl5000 {background: green; color: white}")
        elif self.soruSayisi == 6:
            self.lbl7500.setEnabled(True)
            self.lbl7500.setStyleSheet("QLabel#lbl7500 {background: green; color: white}")
        elif self.soruSayisi == 7:
            self.lbl15000.setEnabled(True)
            self.lbl15000.setStyleSheet("QLabel#lbl15000 {background: green; color: white}")
        elif self.soruSayisi == 8:
            self.lbl30000.setEnabled(True)
            self.lbl30000.setStyleSheet("QLabel#lbl30000 {background: green; color: white}")
        elif self.soruSayisi == 9:
            self.lbl60000.setEnabled(True)
            self.lbl60000.setStyleSheet("QLabel#lbl60000 {background: green; color: white}")
        elif self.soruSayisi == 10:
            self.lbl125000.setEnabled(True)
            self.lbl125000.setStyleSheet("QLabel#lbl125000 {background: green; color: white}")
        elif self.soruSayisi == 11:
            self.lbl250000.setEnabled(True)
            self.lbl250000.setStyleSheet("QLabel#lbl250000 {background: green; color: white}")
        elif self.soruSayisi == 12:
            self.lbl1000000.setEnabled(True)
            self.lbl1000000.setStyleSheet("QLabel#lbl1000000 {background: green; color: white}")
    def labelSifirla(self):
        self.lbl500.setStyleSheet("QLabel#lbl500 {color: black}")
        self.lbl1000.setStyleSheet("QLabel#lbl1000 {color: black}")
        self.lbl2000.setStyleSheet("QLabel#lbl2000 {color: black}")
        self.lbl3000.setStyleSheet("QLabel#lbl3000 {color: black}")
        self.lbl5000.setStyleSheet("QLabel#lbl5000 {color: black}")
        self.lbl7500.setStyleSheet("QLabel#lbl7500 {color: black}")
        self.lbl15000.setStyleSheet("QLabel#lbl15000 {color: black}")
        self.lbl30000.setStyleSheet("QLabel#lbl30000 {color: black}")
        self.lbl60000.setStyleSheet("QLabel#lbl60000 {color: black}")
        self.lbl125000.setStyleSheet("QLabel#lbl125000 {color: black}")
        self.lbl250000.setStyleSheet("QLabel#lbl250000 {color: black}")
        self.lbl1000000.setStyleSheet("QLabel#lbl1000000 {color: black}")
    def puan(self):
        if self.soruSayisi == 1:
            return 500
        elif self.soruSayisi == 2:
            return 1000
        elif self.soruSayisi == 3:
            return 2000
        elif self.soruSayisi == 4:
            return 3000
        elif self.soruSayisi == 5:
            return 5000
        elif self.soruSayisi == 6:
            return 7500
        elif self.soruSayisi == 7:
            return 15000
        elif self.soruSayisi == 8:
            return 30000
        elif self.soruSayisi == 9:
            return 60000
        elif self.soruSayisi == 10:
            return 125000
        elif self.soruSayisi == 11:
            return 250000
        elif self.soruSayisi == 12:
            return 1000000
        

class SoruEkle_Duzenle_Sil(QMainWindow, QWidget):
    def __init__(self):
        super(SoruEkle_Duzenle_Sil, self).__init__()
        uic.loadUi('soru_ekle.ui', self)
        self.createTable()
        self.btnEkle.clicked.connect(self.mesaj)
        self.btnDuzenle.clicked.connect(self.duzenle)
        self.btnSil.clicked.connect(self.sil)
        self.btnTemizle.clicked.connect(self.temizle)
        self.soruId = ""

    def mesaj(self):
        buttonReply = QMessageBox.question(self, 'Uyarı', "Soruyu Eklemek istediğinize emin misiniz?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            print('Yes clicked.')
            self.soru_ekle()
            self.createTable()
        else:
            print('No clicked.')
        self.show()

    def mesaj2(self):
        buttonReply = QMessageBox.question(self, 'Uyarı', "Veriler başaşrıyla eklendi.", QMessageBox.Ok)
        if buttonReply == QMessageBox.Ok:
            print('Ok clicked.')
            self.temizle()
        self.show()

    def soru_ekle(self):
        self.soru = self.txtSoru.text()
        self.a = self.txtA.text()
        self.b = self.txtB.text()
        self.c = self.txtC.text()
        self.d = self.txtD.text()
        connection=mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'sorulardb'
        )

        imlec = connection.cursor()
        if self.rdbA.isChecked() == True:
            sql = "insert into sorular (soru, a, b, c, d, dogruCevap) values ("+"'"+self.soru+"'"+","+"'"+self.a+"'"+","+"'"+self.b+"'"+","+"'"+self.c+"'"+","+"'"+self.d+"'"+","+"'"+"a"+"'"+")"           
            imlec.execute(sql)
            self.mesaj2()
        elif self.rdbB.isChecked() == True:
            sql = "insert into sorular (soru, a, b, c, d, dogruCevap) values ("+"'"+self.soru+"'"+","+"'"+self.a+"'"+","+"'"+self.b+"'"+","+"'"+self.c+"'"+","+"'"+self.d+"'"+","+"'"+"b"+"'"+")"           
            imlec.execute(sql)
            self.mesaj2()
        elif self.rdbC.isChecked() == True:
            sql = "insert into sorular (soru, a, b, c, d, dogruCevap) values ("+"'"+self.soru+"'"+","+"'"+self.a+"'"+","+"'"+self.b+"'"+","+"'"+self.c+"'"+","+"'"+self.d+"'"+","+"'"+"c"+"'"+")"           
            imlec.execute(sql)
            self.mesaj2()
        elif self.rdbD.isChecked() == True:
            sql = "insert into sorular (soru, a, b, c, d, dogruCevap) values ("+"'"+self.soru+"'"+","+"'"+self.a+"'"+","+"'"+self.b+"'"+","+"'"+self.c+"'"+","+"'"+self.d+"'"+","+"'"+"d"+"'"+")"           
            imlec.execute(sql)
            self.mesaj2()
        else:
            print("Lütfen doğru cevabı seçin.")
            buttonReply = QMessageBox.question(self, 'Uyarı', "Lütfen doğru cevabı seçin", QMessageBox.Ok)
            if buttonReply == QMessageBox.Ok:
                print('Ok clicked')
    def createTable(self):
        
        self.sorular=SoruGetir()
        self.soru_sayisi = len(self.sorular.soruGetir())
        self.tableWidget.setRowCount(self.soru_sayisi)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setHorizontalHeaderLabels(["SORU", "A Şıkkı", "B Şıkkı", "C Şıkkı", "D Şıkkı", "Doğru Cevap"])
        self.tableWidget.clicked.connect(self.soru_getir)

        i = 0
        while i < self.soru_sayisi:
            self.demet = self.sorular.soruGetir()[i]
            self.soru = self.demet[1]
            self.a = self.demet[2]
            self.b = self.demet[3]
            self.c = self.demet[4]
            self.d = self.demet[5]
            self.dogruCevap = self.demet[6]

            self.tableWidget.setItem(i,0, QTableWidgetItem(self.soru))
            self.tableWidget.setItem(i,1, QTableWidgetItem(self.a))
            self.tableWidget.setItem(i,2, QTableWidgetItem(self.b))
            self.tableWidget.setItem(i,3, QTableWidgetItem(self.c))
            self.tableWidget.setItem(i,4, QTableWidgetItem(self.d))
            self.tableWidget.setItem(i,5, QTableWidgetItem(self.dogruCevap))
            i += 1
    def soru_getir(self):
        for tiklananYer in self.tableWidget.selectedItems():
            tiklananYerSatir = tiklananYer.row()
            sorular = self.sorular.soruGetir()[tiklananYerSatir]
            self.soruId = sorular[0]
            soru = sorular[1]
            a = sorular[2]
            b = sorular[3]
            c = sorular[4]
            d = sorular[5]
            dogrucevap = sorular[6]
            
            if dogrucevap == "a":
                self.rdbA.setChecked(True)
                self.txtSoru.setText(soru)
                self.txtA.setText(a)
                self.txtB.setText(b)
                self.txtC.setText(c)
                self.txtD.setText(d)
            elif dogrucevap == "b":
                self.rdbB.setChecked(True)
                self.txtSoru.setText(soru)
                self.txtA.setText(a)
                self.txtB.setText(b)
                self.txtC.setText(c)
                self.txtD.setText(d)
            elif dogrucevap == "c":
                self.rdbC.setChecked(True)
                self.txtSoru.setText(soru)
                self.txtA.setText(a)
                self.txtB.setText(b)
                self.txtC.setText(c)
                self.txtD.setText(d)
            elif dogrucevap == "d":
                self.rdbD.setChecked(True)
                self.txtSoru.setText(soru)
                self.txtA.setText(a)
                self.txtB.setText(b)
                self.txtC.setText(c)
                self.txtD.setText(d)
    
    def duzenle(self):
        if self.soruId != "" and self.txtSoru.text() != "":
            connection=mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'sorulardb'
            )
            imlec = connection.cursor()

            if self.rdbA.isChecked() == True:
                buttonReply = QMessageBox.question(self, 'Uyarı', "Son kararınız mı?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if buttonReply == QMessageBox.Yes:
                    sql = "update sorular set soru='"+self.txtSoru.text()+"',a = '"+self.txtA.text()+"',b='"+self.txtB.text()+"',c='"+self.txtC.text()+"',d='"+self.txtD.text()+"', dogruCevap='a' where id = "+str(self.soruId)+""
                    imlec.execute(sql)
                    QMessageBox.question(self, 'Başarılı', "Soru başarıyla düzenlendi.", QMessageBox.Ok)
                    self.createTable()
                else:
                    print('No clicked.')
            elif self.rdbB.isChecked() == True:
                buttonReply = QMessageBox.question(self, 'Uyarı', "Son kararınız mı?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if buttonReply == QMessageBox.Yes:
                    sql = "update sorular set soru='"+self.txtSoru.text()+"',a = '"+self.txtA.text()+"',b='"+self.txtB.text()+"',c='"+self.txtC.text()+"',d='"+self.txtD.text()+"', dogruCevap='b' where id = "+str(self.soruId)+""
                    imlec.execute(sql)
                    QMessageBox.question(self, 'Başarılı', "Soru başarıyla düzenlendi.", QMessageBox.Ok)
                    self.createTable()
                else:
                    print('No clicked.')
            elif self.rdbC.isChecked() == True:
                buttonReply = QMessageBox.question(self, 'Uyarı', "Son kararınız mı?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if buttonReply == QMessageBox.Yes:
                    sql = "update sorular set soru='"+self.txtSoru.text()+"',a = '"+self.txtA.text()+"',b='"+self.txtB.text()+"',c='"+self.txtC.text()+"',d='"+self.txtD.text()+"', dogruCevap='c' where id = "+str(self.soruId)+""
                    imlec.execute(sql)
                    QMessageBox.question(self, 'Başarılı', "Soru başarıyla düzenlendi.", QMessageBox.Ok)
                    self.createTable()
                else:
                    print('No clicked.')
            elif self.rdbD.isChecked() == True:
                buttonReply = QMessageBox.question(self, 'Uyarı', "Son kararınız mı?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if buttonReply == QMessageBox.Yes:
                    sql = "update sorular set soru='"+self.txtSoru.text()+"',a = '"+self.txtA.text()+"',b='"+self.txtB.text()+"',c='"+self.txtC.text()+"',d='"+self.txtD.text()+"', dogruCevap='d' where id = "+str(self.soruId)+""
                    imlec.execute(sql)
                    QMessageBox.question(self, 'Başarılı', "Soru başarıyla düzenlendi.", QMessageBox.Ok)
                    self.createTable()
                else:
                    print('No clicked.')
        else:
            QMessageBox.question(self, 'Uyarı', "İlk önce düzenlenecek soruyu tablodan seçin", QMessageBox.Ok)

    def sil(self):
        if self.soruId != "" and self.txtSoru.text() != "":
            connection=mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'sorulardb'
            )
            imlec = connection.cursor()
            buttonReply = QMessageBox.question(self, 'Uyarı', "Son kararınız mı?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if buttonReply == QMessageBox.Yes:
                sql = "delete from sorular where id = "+str(self.soruId)+""
                imlec.execute(sql)
                QMessageBox.question(self, 'Başarılı', "Soru başarıyla silindi.", QMessageBox.Ok)
                self.createTable()
                self.temizle()
            else:
                print('No clicked.')
        else:
            QMessageBox.question(self, 'Uyarı', "İlk önce silinecek soruyu tablodan seçin.", QMessageBox.Ok)

    def temizle(self):
        self.txtSoru.setText("")
        self.txtA.setText("")
        self.txtB.setText("")
        self.txtC.setText("")
        self.txtD.setText("")
        self.rdbA.setChecked(False)
        self.rdbB.setChecked(False)
        self.rdbC.setChecked(False)
        self.rdbD.setChecked(False)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    MW = MainWindow()
    MW.show()
    sys.exit(app.exec_())