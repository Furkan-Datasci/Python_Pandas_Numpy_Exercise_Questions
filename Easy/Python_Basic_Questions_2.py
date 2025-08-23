# SORU-1: Bir listenin toplamını kendin hesapla (sum kullanma).
# Örn: [1,2,3] → 6


# SORU-2: Bir string’deki sesli harf sayısını bul.
# Örn: "ankara" → 3


# SORU-3: 1–100 arasında 3 ve 5’e aynı anda bölünenleri yazdır.


# SORU-4: Listedeki maksimum ve minimumu aynı anda döndür.
# Örn: [4,1,9,2] → (1,9)


# SORU-5: Bir sayının asal olup olmadığını kontrol eden fonksiyon yaz.


# SORU-6: Bir cümledeki kelime sayısını bul.
# Örn: "Bugün hava güzel" → 3

# SORU-6 CEVAP:
"""
kelime = input("LÜtfen bir kelime giriniz:")
ayirma = kelime.split()
print(f"Soru-6 Cevap: {len(ayirma)} kelimeden oluşmaktadır.")
"""
# SORU-7: Bir kelimenin palindrom olup olmadığını kontrol et.
# Örn: "kayak" → True

# SORU-7 Cevap: 
"""
kelime = input("Lütfen bir kelime giriniz")
palindrom = True
for i in kelime[::-1]:
    if kelime != i:    
        palindrom = False
        
if palindrom:
    print(f"Soru-7 Cevap: {kelime} kelimesi bir palindrom kelimedir.")
else:
    print(f"Soru-7 Cevap: {kelime} kelimesi bir palindrom kelimedir.")
"""

# SORU-8: Listedeki tekrar edenleri kaldır (sıra önemli değil).
# Örn: [1,2,2,3] → [1,2,3]
"""
list_1 = [1,2,2,3,4,4,4,4,5,1,6,7,8,9]
print(f"Soru-8 Cevap: {set(list_1)}")
"""
# SORU-9: 0–20 arası çift sayıların karelerini listele.
# Örn: [0,4,16,...,400]
"""
list_2 = list([i ** 2 for i in list(range(1,21))])
print(f"Soru-9 Cevap: {list_2}")
"""     

# SORU-10: Cümledeki kelimeleri tersten sırala.
# Örn: "Python öğrenmek güzel" → "güzel öğrenmek Python"
"""
kelime = "Python öğrenmek güzel"
ayri = kelime.split()
yeni_kelime = []
for i in ayri[::-1]:
    yeni_kelime.append(i)
print(f"Soru-10 Cevap: {yeni_kelime}")
"""
# SORU-11: Bir listenin ortalamasını hesapla.
"""
list_1 = [1,2,3,4,5,6,7,8,9,10]
toplam = 0
for i in list_1:
    toplam += i
print(f"Soru-11 Cevap: {toplam / len(list_1)}")
"""
# SORU-12: Bir string’deki harf frekansını sözlük olarak döndür.
# Örn: "aba" → {"a":2,"b":1}
"""
list_2 = "abasıyanık"
def_1 = {}
for i in list_2:
    if i in def_1:
        def_1[i] += 1
    else:
        def_1[i] = 1
print(def_1)
"""

# SORU-13: İki listenin kesişimini bul.
# Örn: [1,2,3] & [2,3,4] → [2,3]
"""
list_1 = [1,2,3,4,5,6,7,8,9,10]
list_2 = [2,3,4,5,6,7,8,9,10,11,12,13,14,2,2,2,2]
ortak = []
for i in list_1:
    if i in list_2:
        ortak.append(i)
print(f"Soru-12  Cevap: {ortak}")
"""
# SORU-14: Bir listeyi yerinde (in-place) ters çevir (slice kullanma).
"""
list_1 = "Selamün Aleyküm"
ters = []
for i in list_1[-1::-1]:
    ters.append(i)
print(f"Soru-14 Cevap: {ters}")
"""
# SORU-15: En büyük ikinci sayıyı döndür (tek geçişte çözmeye çalış).
"""
list_1 = [1,2,3,4,5,6,7,8,9,10,11,12,12,139]
max_1 = max(list_1)
list_1.remove(max(list_1))
print(max(list_1))
"""
# SORU-16: Girilen sayının faktöriyelini hesapla.
"""
sayi = int(input("Lütfen bir sayı griniz: "))
carpım = 1
for i in list(range(2,sayi+1)):
    carpım *= i
print(carpım)
"""
# SORU-17: Verilen metindeki en uzun kelimeyi döndür.
"""
kelime = " SEN Seni seviyom dingil, abi fırlamacıklı sucuklu ekmek damlacıklıklarındakininsarısı"
kelimeler = kelime.split()
uzun = []
a = 1
for i in kelimeler:
    if len(i) > len(kelimeler[a]):
        uzun = i
        a +=1
print(uzun)
"""
# SORU-18: Sadece tek sayıların karelerini yeni listeye al (list comprehension).
"""
print(list(i for i in list(range(1,61)) if i % 2 != 0))
"""



# SORU-1 CEVAP:
"""
list_1 = [1,2,3]
toplam = 0
for i in list_1:
    toplam += i
print("SORU-1: Toplam:",toplam)
"""

# SORU-2 CEVAP:
"""
kelime = input("Lütfen bir kelime giriniz:")
sesli_harfler = ["a","e","ı","i","o","ö","u","ü"]
harf_sayisi = []
for i in kelime.lower():
    if i in sesli_harfler:
        harf_sayisi += i
print("SORU-2 CEVAP:", len(harf_sayisi)) 
"""

# SORU-3 CEVAP:
"""
tam_bölünenler = []
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        tam_bölünenler.append(i)
print("SORU-3 CEVAP:",tam_bölünenler)
"""
# Another way 3:
"""
tam_bölünenler = [i for i in range(1,101) if i % 3 == 0 and i % 5 == 0]
print(tam_bölünenler)
"""

# SORU-4 CEVAP:
"""
list_1 = [4,1,9,2,15,20,99,130,0]
print("SORU-5 CEVAP: Max:",max(list_1),", Min:",min(list_1))
"""

# SORU-5 CEVAP:
"""
Sayi = int(input("Lütfen bir sayı giriniz: "))
Asal = True 

if Sayi < 2:
    print(f"Soru-5 cevap: {Sayi} sayısı asal değildir.")
else:
    for i in range(2, int(Sayi**0.5) + 1): 
        if Sayi % i == 0:
            Asal = False
            break 
    if Asal:
        print(f"Soru-5 cevap: {Sayi} sayısı asaldır.")
    else:
        print(f"Soru-5 cevap: {Sayi} sayısı asal değildir.")
"""
