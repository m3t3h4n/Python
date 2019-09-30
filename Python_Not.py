#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Liste


# In[5]:


#string i parçalayıp listeye dönüştürme list() fonksiyonu
isim="metehan"
liste= list(isim)
print(liste)


# In[6]:


#Yada ;
isim = "metehan"
liste = []
for i in isim:
    liste.append(i)
print(liste)


# In[7]:


#Listeleri birleştirme işlemi
liste1 = [1,2,3,4]
liste2 = [5,6,4,8]
birlesikListe = liste1+liste2
print(birlesikListe)


# In[8]:


#Listeye Eleman Ekleme
liste = [1,2,3,4]
liste = liste + ["metehan"]
print(liste)


# In[9]:


#Yada;
liste = [1,2,3,4]
liste.append("Metehan")
print(liste)


# In[13]:


# pop() methodu
#Eğer içerisine değer vermezsek listedeki son elemanı listeden atıp ekrana basar.Eğer içerisine değer verirsek, içindeki değere karşılık gelen indeksdeki eleman listeden atılır ve ekrana basar
liste = [1,2,3,4,5,6,7,8]
liste.pop()
liste.pop(6)


# In[14]:


#sort methodu listenin içindeki elemanları küçükten büyüğe doğru sıralanmasını sağlar.
liste = [6,9,2,7,8,1]
liste.sort()
print(liste)
#Eğer içierisinde string değerler olsaydı alfabetik sıraya göre sıralardı


# In[15]:


#İç içe listeler
liste1 = [1,2,3]
liste2 = [4,5,6]
liste3 = [7,8,9]
yeniListe = [liste1,liste2,liste3]
print(yeniListe)


# In[16]:


#elemanlarına ulaşmak için ise
print(yeniListe[1][0])


# In[ ]:


#Demetler
#Demetler lisstelerle birebir ayıdır fakat aralarındaki tek fark oluşturma şekli ve değiştirilemez oluşlarıdır.


# In[18]:


#For döngüsüyle karkater dizilerinin üzerinde gezinmek
isim = "metehan"
for karakter in isim:
    print(karakter)
#Bu olay, liste ve demet içinde geçerlidir.
#For döngüleri özel bir işlem yapılmamışsa, genellikle string değerler üzerinde çalıştırılır.Eğer sayısal değerler ile döngüyü döndürmek istiyorsak, for döngüsüyle beraber range() fonksiyonu da kullanılmalı yada while döngüsü kullanılmalıdır.


# In[2]:


#range() fonksiyonu; belirtilen başlangıç ve bitiş değerleri arasında bir sayı dizisi oluşturur.Eğer Başlangıç Değeri belirtilmezse, 0'dan başlar.
for i in range(5):
    print(i)


# In[3]:


#yada;
liste = list(range(1,20))
print(liste)


# In[25]:


#Döngülerde kullanılan break ve continue ifadesi
#Break; eğer döngü, herhangi bir yerde break ifadesiyle karşılaştığı zaman döngünün çalışmasını bir anda durdurur.
#break ifadesi hangi döngünün içindesye o döngü durur.Eğer iç içe birçok döngü varsa ve break ifadesi en içteki döngünün içindeyse, sadece en içteki döngü durur.
#Örnek:
i = 0
while(i<20):
    print(i)
    if(i == 10):
        print("Döngü durdu")
        break
    i+=1


# In[28]:


#for döngüsüyle örnek
for i in range(20):
    print(i)
    if(i == 10):
        print("Döngü durdu")
        break
    


# In[30]:


#Continue; Eğer döngü continue ifadesi ile karşılaştığı zaman, devamındaki işlemleri yapmayı kesip döngünün başına dönüp devam eder.
for i in range(10):
    if(i == 3 or i == 5):
        print("İşlem durdu")
        continue
    print("i: ",i)


# In[31]:


#ÖNEMLİ : COMPREHENSİON ARAŞTIR


# In[32]:


#Fonksiiyonlar
#Fonksiyona parametre ve argüman tanımlama
def selamla(isim):
    print("Merhaba ", isim)
selamla("Metehan")

#Fonksiyon tanımlarken içine tanımlanan değer parametre, çağırırken içne tanımlanan değer ise argüman olmaktadır.


# In[33]:


#Örnek
def topla(s1,s2,s3):
    print(s1,",",s2,"ve",s3,"sayılarının toplamı,",s1+s2+s3)
topla(3,4,5)


# In[ ]:


#bir sayının faktöriyelini hesaplayan fonksiyon
fak = int(input("Bir sayı girin :"))
def faktoriyel(sayi):
    faktoriyel = 1
    if(sayi == 1 or sayi == 0):
        print(sayi,"Faktoriyeli", faktoriyel)
    else:
        while(sayi>= 1):
            faktoriyel *= sayi
            sayi -=1
        print("Faktoriyel : ",faktoriyel)
faktoriyel(fak)


# In[ ]:


#Return ifadesi
#return; bir fonksiyonun sonucunda elde edilen değeri dışına göndermeye yarar. Böylelikle fonksiyondan alınan değer bir değişkene depolanabilir ve programın farklı yerlerinde kullanılabilir.
#Örnek
def toplama(a,b,c):
    print("Toplamları,",a+b+c)
def ikiyleCarp(d):
    print("İkiyle Çarpımı,"d*2)
toplam = toplama(3,4,5)
ikiyleCarp(toplam)
#Şeklinde yapılırsa hata verir.Çünkü toplam değişkeninin içine toplama fonksiyonunun değerini return etmeden atmaya çalıştık fakat toplama fonksiyonu bir değer döndürmediği için toplam değişkeninin içi boş olacaktır ve ikiyleCarp fonksiyonuda çalışmayacaktır.


# In[ ]:


#Doğru hali
def toplama(a,b,c):
    toplam= a+b+c
    return toplam
def ikiyleCarp(d):
    carpim = d*2
    print("ikiyle çarpımı,",carpim)
ikiyleCarp(toplama(3,4,5))


# In[39]:


#Return ifadesi fonksiyonun en sonunda çalıştırılmalıdır.Çünkü return ifadesinden sonra fonksiyon biter.


# In[ ]:


#Örnek
def ikiyleTopla(a):
    print("Birinci fonksiyon çalıştı.")
    return a+2
def ucleCarp(a):
    print("İkinci fonksiyon çalıştı.")
    return a*3
def ikiyeBol(a):
    print("Üçüncü fonksiyon çalıştı.")
    a/2
    print(a)
ikiyeBol(ucleCarp(ikiyleTopla(10)))
#Üçüncü fonksiyondaki değeri return etmeye gerek yok.Çünkü geri dönen değeri kullanacak yer yok.


# In[2]:


#Varsayılan parametre
#Örnek
def selamla(isim = "metehan"):
    print("Merhaba :",isim)
selamla()
#fonksiyon çağrılırken argüman girilmedi.Çünkü fonksiyon tanımlanırken varsayılan bir parametre değeri verildi.


# In[3]:


#Örnek
def bilgiGoster(isim="metehan",soyisim="Özdeniz",numara="58746"):
    print("Bilgiler :",isim,soyisim,numara)
bilgiGoster()
#Birden fazla varsayılan parametre girilirken verilen bilgilerin sırayla girilmesine dikkat edilmelidir.


# In[9]:


#Bir fonksiyona istediğimiz kadar parametre ve argüman vermek istersek *(yıldız)lı parametere kullanmalıyız
def toplama(*parametreler): #artık fonkiyonun parametreleri bir demet halini aldı
    toplam = 0
    print("Fonksiyona verilen parametreler :", parametreler)
    for i in parametreler:
        toplam+=i
    return toplam
sonuc = toplama(3,4,5)
print("Fonksiyonun Sonucu :",sonuc)


# In[ ]:


#Global ve Local Değişkenler
#Fonksiyonlarda tanımlanan değişkenler local değişkenler olarak tanımlanırlar.
#Yeni bir fonksiyon bloğunda tanımlanan değişkenler fonksiyona özgüdür.Ve Dışarıdan erişilemezler.
#Fonksiyon çalışmasını bitirdikten sonra değişkenler bellekten silinirler ve yok olur.
#Örnek
def fonksiyon(a):
    a = 5
print(a) #Değişken yok oldu.Hata verir.


# In[10]:


#Global değişkenler de fonksiyon dışında tanımlanan değişkenlerdir ve tanımlandıktan sonra programın her yerinden erişileblirler.


# In[15]:


#Global değişkenleri fonksiyonlarda kullanabilmek için ise "global" ifadesi kulklanılır
a = 5
def fonksiyon():
    global a #Bunun sayesinde dışarıdaki global değişkeni fonksiyonda da kullanabiliriz.
    a = 10 #Artık dışarıdaki a global değişkeni 10 oldu
    print(a)
fonksiyon()
print(a)


# In[16]:


#Modüller
#Bir Python modülünü programımıza import ederek bu modüller içinde yazılan hazır fonksiyonlardan ve sınıflardan kullanabilir 
#ve programlarımızı daha efektif bir şekilde yazabiliriz.
#Eğer modül diye bir kavram olmasaydı, programlarımızdaki herbir fonksiyonu ve sınıfı kendimiz yazmak zorunda kalacaktık.


# In[17]:


#Bir modülü prorgrama dahil etmek için;
#Yöntem1
#import [modül adı] şeklinde tanımlanır.
#Örnek math modülü


# In[19]:


import math #Modül içeri aktarıldı.Artık bu modülün bütün fonksiyonları kullanılabilir.
#Modülün içindeki fonksiyonları görmek için
print(dir(math))


# In[21]:


#modülün içiğndeki fonkssiyonların kullanımını görmek için
print(help(math))


# In[22]:


#Bu import edilen modüllerin fonksiyonlarını kullanabilmek için ise;
#modül_adı.fonksiyon_adı()


# In[24]:


#Örnek : math modülünün içimdeiki factorial fonksiyonunu kullanabilmek için
print(math.factorial(5)) #5 sayısının faktöriyelini buldu.
#Eğer bu modül import edilmeseydi, bir sayının faktöriyelini bulma fonksiyonunu kendi elimizle yazmak zorunda kalacaktık.


# In[26]:


#Bir modülü kendi belirlediğimiz isimle kullanabilmek için ise;
#import modul_adı as vereceğimiz_isim
#Örnek
import math as matematik #math modülünü matematik ismiyle tanımladık
print(matematik.factorial(5)) #math modülünü ise matematik ismiyle kullandık


# In[27]:


#Yöntem2
#from modül_adı import*
#Eğer modül böyle tanımlanmışsa modülü kullanırken modül ismini kullanmadan direkt olarak fonksiyonun ismini yazarak kullanırlır
#*yıldız(*) ise modülün içindeki bütün fonksiyonları programa f-dahil et anlamına gelir.
#Eğer bir modülün içindeki belirli fonksyonları kullanacaksak, kullanacağımız fonksiyonları yıldızın yerine virgülle ayırarak yazmalıyız.


# In[29]:


#Örnek
from math import * # * ile Modülün içindeki bütün fonksiyonları programa dahil et dedik
print(factorial(5))


# In[31]:


#Modülün içindeki belirli fonksiyonları almak için ise
from math import factorial,floor
print(factorial(5))
print(floor(3.5))
#Eğer modülün içindeki kullanacağımız fonksiyonu programa dahil etmeden kullanırsak hata verir.


# In[32]:


#Not : Eğer kendi tanımladığımız fonksiyon, modülün fonksiyonunun ismiyle aynıysa, program en son gördüğü fonksiyonu çalıştıracaktır
#Fakat hepsi çalışacaktır.


# In[ ]:




