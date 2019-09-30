import os #os modülü işletim sisteminde işlemler gerçekleştirebildiğimiz standart bir python modülüdür.

print(os.getcwd()) #Python dosyamızın bulunduğu dizini getirir.

os.chdir("C:/xampp/htdocs") #changedir yani yolu değiştir.
print(os.getcwd()) 
print(os.listdir()) #Belirtilen dizindeki dosya ve klasörleri listeler.

def dizinListele():
    for i in os.listdir():
        print(i) #Belirtilen dizindeki dosya ve klasörleri alt alta listeledi.
dizinListele()

#Belirtilen dizinde klasör oluşturma.
os.mkdir("Python_Klasör_Oluşturma_Testi")
dizinListele()

#Belirtilen dizinde belirtilen klasörü silme.
os.rmdir("Python_Klasör_Oluşturma_Testi")
dizinListele()

#Belirlenen dizindeki dosyanın ismini değiştirme
os.rename("test.txt","test2.txt") #test.txt dosyasının ismini test2.txt yaptı
dizinListele()

#Belirtilen Yoldaki Bütün Dosya ve Klasörleri Listeleme
print(os.walk("C:/xampp/htdocs")) #bir demet objesi oluşturdu.Düzenli bir şekilde görmek için ise;
for i in os.walk("C:/xampp/htdocs"):
    print(i)
#Daha düzenli görmek için ise;
for yol,klasor_adi,dosya_adi in os.walk("C:/xampp/htdocs"):
    print("Yol :",yol)
    print("Klasör adı :",klasor_adi)
    print("Dosya adı :",dosya_adi)
    print("******************************************************************************")