print("""*************
Bir Sayının Bölenlerini Bulma\nÇıkmak İçin (q) ya basın
*************""")

def bolenler(sayi):
    bolen_listesi = []
    for i in range(1,sayi+1):
        if(sayi%i == 0):
            bolen_listesi.append(i)
    print(sayi,"Sayısının bölenleri,",bolen_listesi)
while True:
    deger = input("Bir değer Girin :")
    if(deger == "q"):
        print("Programdan Çıkılıyor...")
        break
    else:
        bolenler(int(deger))
        break