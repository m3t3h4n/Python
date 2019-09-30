#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*args parametresi
def fonksiyon(*args): #Bu fonksiyon istediğim kadar parametre alabilir ve istediğim kadar argüman gönderebilirm.
    for i in args:
        print(i)
fonksiyon(1,2,3,4,5) #Gönderilen argümanlar args adında bir demete dönüştü ve for döngüsü ile çektim.


# In[2]:


def fonksiyon(isim,*args):
    print("İsim : ",isim)
    print("----------------")
    for i in args:
        print(i)
fonksiyon("Metehan",1,2,3) #Metehan argümanı ilk önce isim parametresi ile eşleşiyor ve ondan sonraki argümanlar ise *args parametresi ile eşleşiyor.


# In[4]:


#**kwargs parametresi : parametrelere isim vermeye yarar.Parametreleri bir sözlüğe dönüştürür.
def fonksiyon(**kwargs):
    print(kwargs)
fonksiyon(isim="Metehan",soyad="Özdeniz",numara=123) #parametreler bir sözlüğe dönüştü


# In[7]:


#Örnek
def fonksiyon(**kwargs):
    for i,j in kwargs.items():
        print("Argüman ismi:",i,"Argüman Değeri:",j)
fonksiyon(isim="Metehan",soyad="Özdeniz",numara=123)


# In[9]:


#*args ve **kwargs birlikte kullanma:
def fonksiyon(*args,**kwargs):
    for i in args:
        print(i)
    print("---------------")
    for i,j in kwargs.items():
        print(i,j)
fonksiyon(1,2,3,4,isim="Metehan",soyad="Özdeniz",numara=123) #ilk parametre *args olduğu için istediğim kadar değer verdim,ikinci parametre de **kwargs olduğu için sözlük veritipine uygun argüman gönderdim ve sonuç: 


# In[11]:


#İç içe fonksiyonlar
#Örnek
def fonksiyon():
    print("Büyük fonksiyon çalıştı.")
    def fonksiyon2():
        print("Küçük fonksiyon çalıştı.")
    fonksiyon2()
fonksiyon()


# In[12]:


#İç içe fonksiyonlarda argüman gönderme
def fonksiyon(*args):
    def toplama(args):
        toplam = 0
        for i in args:
            toplam+= i
        print("Toplam : ", toplam)
    toplama(args)
fonksiyon(1,2,3,4,5,6,7)
#İçerideki fonksiyon parametre olarak dışarıdaki fonksiyonun parmetresini alabilir.ş


# In[16]:


#Fonksiyonları return ile dönmek
#Dikkat : Fonksiyonun içindeki bir değeri return etmek değilde, bütün bir fonksiyonu return etmek.
#Örnek:
def islem(islem_adi):
    def toplama(*args):
        toplam= 0
        for i in args:
            toplam+=i
        print("Toplam : ",toplam)
    def carpma(*args):
        carpım = 1
        for i in args:
            carpım*=i
        print("Çarpım : ",carpım)
    if(islem_adi == "toplama"):
        return toplama #Toplama fonksiyonu return edildi.
    elif(islem_adi == "çarpma"):
        return carpma #carpma fonksiyonu return edildi.
toplamaFonksiyonu = islem("toplama") #islem fonksiyonu toplama fonksiyonunu return etti ve artık toplama fonksiyonu toplamaFonksiyonu objesine eşit oldu
toplamaFonksiyonu(1,2,3,4,5,6,7)
carpmaFonksiyonu = islem("çarpma") #islem fonksiyonu carpma fonksiyonunu return etti ve artık carpma fonksiyonu carpmaFonksiyonu objesine eşit oldu.
carpmaFonksiyonu(1,2,3,4,5)


# In[ ]:


#Decorator fonksiyonların oluşturulması ve kullanılması
#Decorator fonksiyonlar ; fonksiyonlarımıza ekstra özellik eklediğimz fonksiyonlardır ve kod tekrarı yapmamızı engeller.
#Konuyu anlamadım....

