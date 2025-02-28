"""print("otopark ücreti hesaplama")
saat=int(input("otoparkta kaç saat beklediniz:"))
ucret=0
if saat==1:
    ucret +=5
elif saat>1 and saat<=5:
    ucret +=5+4*saat
elif saat>5:
    ucret +=5+3*saat
print(ucret)"""


"""print("iki sayı arasındaki sayıların toplamı ")
sayi=int(input("bir sayı giriniz :"))
sayi2=int(input("ikinci sayıyı giriniz:"))
toplam=0
for i in range(sayi,sayi2+1):
    toplam +=i
print(toplam)"""
    


"""print("asal sayı bulma ")
sayi=int(input("bir sayi giriniz :"))
i=2
while i< sayi and i>0 :
    
    if sayi % i ==0:
        print("sayi asal değildir ")
    else:
        print("sayi asaldır ")
    break
if sayi==2:
    print("sayi asaldır")
if sayi<0:
    print("negatif değerler asal olamaz")"""



"""print("yazdığınız kelimeyi tersten yazan uygulama")
word=input("bir kelime giriniz :")
index=len(word)-1
while index>= 0:
    print(word[index])
    index -=1"""

print("yazılan sayıya kadar olan tek ve çift sayıların ayrı ayrı toplamı ")
sayi=int(input("bir sayi giriniz :"))
teksayi_toplami=0
ciftsayi_toplami=0

for x in range(1,sayi+1):
    if x % 2 ==0:
        ciftsayi_toplami +=x
    else:
        teksayi_toplami +=x
print(" yazdığınız sayıya kadar olan tek sayıların toplamı :",teksayi_toplami)
print("yazdığınız sayıya kadar olan çift sayıların toplamı :",ciftsayi_toplami)

