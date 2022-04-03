import islem
from math import *
print(""""******* 
(1) toplama
(2) çıkarma
(3) çarpma
(4) bölme
(5) karesini alma
******""")
def plus(sayi1,sayi2):
    return sayi1 + sayi2
def minus(sayi1,sayi2):
    return sayi1 - sayi2
def multiplication(sayi1,sayi2):
    return sayi1 * sayi2



secim=input("1/2/3/4/5: ")

sayi1 = float(input("sayi giriniz: "))
sayi2 = float(input("sayi giriniz: "))
if(secim=="1"):
    print("sonuc: ",plus(sayi1,sayi2))
elif(secim=="2"):
    print("sonuc: ",minus(sayi1,sayi2))
elif(secim=="3"):
    print("sonuc: ",multiplication(sayi1,sayi2))
elif(secim=="4"):
    print("sonuc: ",islem.divide(sayi1,sayi2))
elif(secim=="5"):
    print("sonuc: ",islem.pow(sayi1, sayi2))

else:
    print("gecersiz islem...!")



