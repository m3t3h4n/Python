import sys

print(sys.argv)

for i in sys.argv:
    print(i)

def bilgi_goster(ad, soyad):
    print("Bilgiler : ",ad,soyad)

bilgi_goster(sys.argv[1],sys.argv[2])