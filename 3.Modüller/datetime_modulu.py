from datetime import datetime

simdikiZaman = datetime.now() #Şuanki zamanı yıl ay gün saat ve salise şeklinde aldı ve bir objeye dönüştürdü.
# print("Yıl :",simdikiZaman.year)
# print("Ay :",simdikiZaman.month)
# print("Gün :",simdikiZaman.day)
# print("Saat :",simdikiZaman.hour)
# print("Dakika :",simdikiZaman.minute)
# print("Saniye :",simdikiZaman.second)
# print("Salise :",simdikiZaman.microsecond)

#Belli iki tarih arasında işlem yapma
#İlk önce istediğimiz tarihte bir datetime objesi oluşturmalıyız.Datetime objesi oluşturulurken Yıl, ay, gün
#saat,saniye ve salise değerleri tek tek girilmelidir.Ancak sadece belirli özellikleri girerek de
#bir datetime objesi oluşturulabilir.
suankiZaman = datetime.now()
dogumGunu = datetime(1998,4,28)
fark = suankiZaman - dogumGunu
print("Ölüme,",fark,"kadar yaklaşmışım.")