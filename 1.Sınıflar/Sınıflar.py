#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Sınıflar
#Kendi veri tiplerimizi oluşturmak ve bu ver tiplerinden objeler üretmek için öncelikle objeleri üreteceğimiz yapıyı tanımlamamız gerek.
#Bunu tasarladığımız yapıya da class denir.
#Classlar objelerimizi oluştururken, objelerin özellklerini ve metodlarını tanımladığımız bir yapıdır ve her bir objeyi bu yapya göre üretiriz.


# In[2]:


#Örnek
class kisiBilgisi(): #Sınıfımızı tanımladık
    ad = "Metehan"
    soyad = "Özdeniz"
    yas = 20


# In[3]:


#Sınıflardan objeler oluşturmak için ise
#obje_ismi = sınıf_ismi
bilgi = kisiBilgisi() #kisiBilgisi veri tipinden bir bilgi objesi oluşturuldu
#Bilgi objesi artık kisiBilgisi sınıfındaki bütün özellklere(attributs) sahip olmuş oldu.


# In[5]:


#Bu objenin özelliklerini görmek için ise
#obje_ismi.özellik_ismi
print(bilgi.ad)
print(bilgi.soyad)
print(bilgi.yas)


# In[6]:


#Başka bir obje oluşturalım
bilgi2 = kisiBilgisi()
print(bilgi2.ad,bilgi2.soyad,bilgi2.yas)


# In[7]:


#Oluşturulan objelerin özellikleri aynı oldu.Çünkü aslında bu objelerin özellikleri birer sınıf özelliğidir.
#Yani bir obje oluşturulduğunda, bu özelliklerin değerleri varsayılan olarak gelir.
#Bu özelliklerin değerlerine obje oluşturulmadan da erişilebilir.
#Class_ismi.Özellik_ismi()
print(kisiBilgisi.ad)
print(kisiBilgisi.soyad)


# In[8]:


#Her bir objeyi başlangıçta farklı değerlerle oluşturmak için, her bir objeyi oluştururken objelerin değerilerini classa göndermemiz gerekiyor.
#Bunun içinde özel bir metodu kullanmak gerekiyor.
# __init__() metodu
# __init__() metodu python da yapıcı(constructor) fonksiyon olarak da adlandırılır.
# Bu metod objeler oluşturulurken, yani classlar çalışırken, otomatik olarak çağrılan ilk fonksiyondur.
#Yani objeleri oluştururken objelerin özelliklerini __init__() fonksiyonunun içine yazarak,  classda  da ilk olarak __init__()
#fonksiyonu çalışacağı için, ilk olarak class ın özelliklerini de tanımlamış oluruz.
#Bu sayede objeyi oluştururken, objeye argüman girerek, classın içindeki ilk çalışacak olan __init()__ fonksiyonuna parametre
#göndermiş oluyoruz ve objemizin özellikleri tanımlanmış oluyor.


# In[1]:


#Örnek 
class kisiBilgisi():
    #Daha herhangi bir özellik atanmadı
    def __init__(self):
        print("Class'ın içindeki __init__() fonksiyonu çalıştı.")
bilgi = kisiBilgisi()
print(bilgi)


# In[12]:


#Objelerin içinde __init__() fonksiyonu gibi birçok metod vardır.
#Objeler oluşturulurken bizim oluşturduğumuz özellikler dışında bu metodlar da varsayılan olarak objelerin içinde oluşur.
#Objenin içindeki metodları ve özellikleri görmek için ise
print(dir(bilgi))
#Bu varsayılan metodlarıda kendi istediğimiz gibi değiştirip kullanabiliriz.


# In[13]:


#Peki buradaki self ne anlama geliyor.
#self kelimesi obje oluşturulurken o objeyi gösteren bir referanstır ve metodlarda en başata bulunması gereken bir parametredir.
#Yani objenin bütün özellikleri ve metodları bu referans üzerinden kullanılmalıdır.


# In[5]:


#Örnek
class kisiBilgisi():
    def __init__(self,ad,soyad,yas,numara = "bilgi yok"): #parametrelerin değerleri objeler oluşturulurken gönderilircektir.
        self.ad = ad #self.özellik_ismi = parametre değeri şeklinde objemizin ad özelliğine değeri atıyoruz.
        self.soyad = soyad #self.özellik_ismi = parametre değeri şeklinde objemizin soyad özelliğine değeri atıyoruz.
        self.yas = yas #self.özellik_ismi = parametre değeri şeklinde objemizin yas özelliğine değeri atıyoruz.
        self.numara = numara #self.özellik_ismi = parametre değeri şeklinde objemizin numara özelliğine değeri atıyoruz.
bilgi = kisiBilgisi("Metehan","Özdeniz", 20) #Artık değerler gönderilerek objelerin özelliklerine istenilen değerler verilebilir.
#bilgi objesi oluşurken kisiBilgisi classına numara argümanını girmedik.Çünkü numara parametresine varsayılan bir değer verdik.
print(bilgi.ad)
print(bilgi.soyad)
print(bilgi.yas)
print(bilgi.numara)


# In[14]:


#Bir sınıf içerisine metodlar tanımlama
class Yazilimci():
    def __init__(self,ad,soyad,numara,maas,diller):
        self.ad = ad
        self.soyad = soyad
        self.numara = numara
        self.maas = maas
        self.diller = diller
    def bilgiGoster(self):
        print("Yazılımcı bilgisi :\n Ad : {}\nSoyad : {}\nNumara : {}\nMaaş :{}\nDiller : {}".format(self.ad,self.soyad,self.numara,self.maas,self.diller))
bilgi = Yazilimci("Metehan","ısofjasfd","sdpfg",5465,["C#","Python"])
print(bilgi.bilgiGoster())
#Burada bilgiGoster methodu self den başka parametre almadığı için argüman girilmedi.Eğer Method parametre alsaydı
#objeyi kullanırken de argüman girmek zorunda kalacaktık.


# In[27]:


#Örnek
class Yazilimci():
    def __init__(self,ad,soyad,numara,maas,diller):
        print("Yazilimci Classının __init__() fonksiyonu çalıştı.")
        self.ad = ad
        self.soyad = soyad
        self.numara = numara
        self.maas = maas
        self.diller = diller
    def bilgiGoster(self):
        print("Yazılımcı bilgisi :\n Ad : {}\nSoyad : {}\nNumara : {}\nMaaş :{}\nDiller : {}".format(self.ad,self.soyad,self.numara,self.maas,self.diller))
    def maasYukselt(self,yeniMaas):
        print("Maaş Yükseltildi..")
        self.maas += yeniMaas
    def dilEkle(self, yeniDil):
        print("Dil Eklendi..")
        self.diller.append(yeniDil)
bilgi = Yazilimci("Metehan","ısofjasfd","sdpfg",5465,["C#","Python"])
print(bilgi.bilgiGoster())
bilgi.maasYukselt(500)
bilgi.dilEkle("JavaScript")
bilgi.bilgiGoster()
#maasYukselt ve dilEkle methodları parametre aldığı için objeleri gösterirken argümanda girildi.


# In[26]:


#Inheritance(Miras alma) : Bir sınıfın özelliklerini başka bir sınıfta kullanmaya yarar
#Örnek
class Programcı(Yazilimci): #İçerisine herhangi bir özellik tanımlanmamasına rağmen Yazilimci sınıfının özelliklerini miras aldı
    pass #Daha sonra birşey yazılacağı, sınıfı böyle çalıştır anlamına gelir.Eğer boş bırakılsaydı hata verirdi.
programci = Programcı("Mücahit","Duman","98969",5986,["HTML","PHP","Css"])
programci.bilgiGoster()

programci.dilEkle("JavaScript")
programci.bilgiGoster()


# In[25]:


#Miras alınan class ın içine kendi fonksiyonlarımızda yazılabilir.
#Örnek : 
class Programci(Yazilimci):
    def zam_yap(self,zam):
        self.maas += zam
        print("Zam yapıldı")
programci = Programci("Mücahit","Duman","68456",5000,["C#"])
programci.bilgiGoster()
programci.zam_yap(1000)
programci.bilgiGoster()


# In[28]:


#Eğer ana class daki fonksiyon ismiyle miras alınan classdaki fonksiyonun ismi aynı ise ne olur?
#Override yani ana classdaki fonksiyon iptal olur.


# In[29]:


#Super anahtar kelimesi
#Super en genel anlamıyla override ettiğimiz bir methodun içinde miras aldığımız sınıfın metodlarını 
#alt sınıflardan kullanmamızı sağlar.


# In[30]:


#Örnek:
class Yazilimci(): #Sınfımızı tekrar tanımlayalım.
    def __init__(self,ad,soyad,numara,maas,diller):
        print("Yazilimci Classının __init__() fonksiyonu çalıştı.")
        self.ad = ad
        self.soyad = soyad
        self.numara = numara
        self.maas = maas
        self.diller = diller
    def bilgiGoster(self):
        print("Yazılımcı bilgisi :\n Ad : {}\nSoyad : {}\nNumara : {}\nMaaş :{}\nDiller : {}".format(self.ad,self.soyad,self.numara,self.maas,self.diller))
    def maasYukselt(self,yeniMaas):
        print("Maaş Yükseltildi..")
        self.maas += yeniMaas
    def dilEkle(self, yeniDil):
        print("Dil Eklendi..")
        self.diller.append(yeniDil)
bilgi = Yazilimci("Metehan","ısofjasfd","sdpfg",5465,["C#","Python"])
print(bilgi.bilgiGoster())
bilgi.dilEkle("JavaScript")
bilgi.bilgiGoster()


# In[37]:


#Override yapacağımız ve miras alacağımız sınıfımızıda tanımlayalım
class Programci(Yazilimci):
    def __init__(self,ad,soyad,numara,maas,diller,hobiler): #Override yapılacak fonksiyon tekrar çağrıldı ve hobiler adında yeni bir parametre eklendi
        #Override methodunda ad,soyad,numara,maas diller özelliklerini tekrar tanımlamamak için, iptal edilen fonksiyondan çağırmak için super() anahtar kelimesi kullanılır
        super().__init__(ad,soyad,numara,maas,diller) #Override yapılan yani iptal olan methodun özelliklerini tekrar aldı
        self.hobiler = hobiler #Override yapıalan fonksiyona hobiler adında yeni bir özellik eklendi
        print("Programci classının __init__() fonksiyonu çalıştı...")
    def bilgileri_goster(self):
        print("Programcı bilgisi : ")
        print("Ad : {}\nSoyad : {}\nNumara : {}\nMaaş : {}\nDiller : {}\nHobiler : {}".format(self.ad,self.soyad,self.numara,self.maas,self.diller,self.hobiler))
        
    def zam_yap(self,zam):
        self.maas += zam
        print("Zam yapıldı")
programci = Programci("Mücahit","Duman","68456",5000,["C#"],"Kitap Okumak")
programci.bilgileri_goster()


# In[43]:


#Özel Methodlar : Bizim özel olarak oluşturmadığımız, ancak her class a default olarak tanımlanan methodlardır.
#__str__() methodu: bir objeyi print fonksiyonu ile ekrana yazdırdığımızda geri döndürülecek değeri oluşturmaya yarar.Eğer __str__() methodunu kendimiz oluşturmazsak python bu methodu default olarak oluşturup bizim önümüze sunacaktır.
#Örnek : 
class Kitap():
    def __init__(self,isim,yazar,sayfa_sayisi,tur):
        print("Kitap class ının __init__() fonksiyonu...")
        self.isim = isim
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi
        self.tur = tur
kitap1 = Kitap("İstanbul Hatırası","Ahmet Ümit",561,"Polisiye")
print(kitap1) #Ekrana "<__main__.Kitap object at 0x0000000005713908>" şeklinde bir değer döndürdü.__str__() methodu bu değeri istediğimiz şekilde return etmeye yarar


# In[45]:


#Örnek:
class Kitap():
    def __init__(self,isim,yazar,sayfa_sayisi,tur):
        print("Kitap class ının __init__() fonksiyonu...")
        self.isim = isim
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi
        self.tur = tur
    def __str__(self):
        return "Kitap Adı : {}\nYazar : {}\nSayfa Sayısı : {}\nTür : {}".format(self.isim,self.yazar,self.sayfa_sayisi,self.tur)
kitap1 = Kitap("İstanbul Hatırası","Ahmet Ümit",561,"Polisiye")
print(kitap1)
#İlk başta kitap1 objesi ekrana print fonksiyonu ile yazdırıldığındaki değer ile şimdiki değer arasında ki fark...
#Not : __str__() methodunda geri döndürülecek değerin başına mutlaka return ifadesi koyulmalıdır.


