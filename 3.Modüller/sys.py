import sys #sys modülü, sistemimizde kurulu olan python sürümünü, yönettiğimiz bir modüldür.
#Bu modülü kullanarak python sistemine özgü fonksiyonları ve özellikleri kullanabiliriz.

#sys.exit ; Bu fonksiyon çalışan python programını sonlandırır.

a = input("Çıkmak için (q) ya basın :")
if a == "q":
    sys.exit() #sys.exit() den sonra program kapanacağı için devamındaki satırlar da çalışmaz.

#sys.argv ; Bu fonksiyon, python dosyamız terminalden çalıştırılırken, yanında yazılan parametreleri
#dosya ismiyle beraber bir listeye kaydetmeye yarar.
#listenin 0. indeksi ise herzaman dosya ismidir.
print(sys.argv) #terminalden dosya çalıştırılırken girilen komutları bir listeye attı
for i in sys.argv:
    print(i)

#Örnek

def kok_bul(a,b,c):
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("Reel Kök Yok..")
    elif delta == 0:
        print("Çift katlı kök.")
        x1 = (-b - delta ** 0.5) / (2*a)
        x2 = (-b + delta ** 0.5) / (2*a)
    elif delta > 0:
        print("Reel kök var..")
        x1 = (-b - delta ** 0.5) / (2*a)
        x2 = (-b + delta ** 0.5) / (2*a)

    return (x1,x2)

if len(sys.argv) == 4:
    print("Kök Bulma : ",kok_bul(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])))
else:
    print("*Lütfen doğru değer girin..\n>sys.py [a] [b] [c]")
