# SORU-1: Bir listede en çok tekrar eden elemanı bulan fonksiyon yaz.
# Örn: [1,2,2,3,3,3,4] → 3


# SORU-2: Bir cümledeki kelimeleri uzunluklarına göre sırala.
# Örn: "Bugün hava çok güzel" → ["çok", "hava", "Bugün", "güzel"]


# SORU-3: Fibonacci serisini verilen n terime kadar listeleyen fonksiyon yaz.
# Örn: n=7 → [0, 1, 1, 2, 3, 5, 8]


# SORU-4: İki string’in anagram olup olmadığını kontrol eden fonksiyon yaz.
# Örn: "listen" ve "silent" → True


# SORU-5: Bir listedeki tüm çift sayıların çarpımını döndür.
# Örn: [2,3,4,5] → 8


# SORU-6: Bir metinde geçen her harfin frekansını bul.
# Örn: "python" → { "p":1, "y":1, "t":1, "h":1, "o":1, "n":1 }


# SORU-7: Bir listedeki sayıları küçükten büyüğe sıralamak için bubble sort algoritmasını uygula 
# (kendi yaz, sort() kullanma).


# SORU-8: Bir listedeki sayılardan sadece asal olanları döndüren fonksiyon yaz.
# Örn: [2,3,4,5,6] → [2,3,5]
            

# SORU-9: Bir 2D matris veriliyor, matrisin transpozunu hesapla.
#[[1,2,3],
# [4,5,6]]


# SORU-10: Bir metindeki en uzun kelimeyi bulan fonksiyon yaz.
# Örn: "Python öğrenmek çok güzel" → "öğrenmek"


# SORU-10 CEVAP:
def en_uzun_kelime(metin):
    kelimeler = metin.split()  
    uzun = max(kelimeler, key=len)  
    return "SORU-10 CEVAP:",uzun

print(en_uzun_kelime("Python öğrenmek çok güzel"))


# SORU-9 CEVAP:
list_1 = [[1, 2, 3],
          [4, 5, 6]]
transpoz = []
for i in range(len(list_1[0])):  
    yeni_satir = []
    for j in range(len(list_1)):
        yeni_satir.append(list_1[j][i])  
    transpoz.append(yeni_satir)

print("SORU-9 CEVAP:",transpoz)


# SORU-8 CEVAP:
list_1 = [2,3,4,5,6]
asal_sayilar = []
for i in list_1:
    is_asal = True
    for n in range(2, i):
        if i % n == 0:
            is_asal = False
            break
    if is_asal:
        asal_sayilar.append(i)
print("SORU-8 CEVAP:",asal_sayilar)


# SORU-7 CEVAP:
list_1 = [8, 6, 3, 5, 4, 2, 7, 1, 9, 0, 124, 12, 15]

n = len(list_1)

for i in range(n):  
    for j in range(0, n - i - 1):  # her turda son i eleman zaten sıralı
        if list_1[j] > list_1[j + 1]:
            # swap (yer değiştir)
            list_1[j], list_1[j + 1] = list_1[j + 1], list_1[j]

print("SORU-7 CEVAP:",list_1)    


# SORU-6 CEVAP:
kelime = "python"
slc = {}
for i in kelime:
    if i in slc:
        slc[i] += 1
    else:
        slc[i] = 1 
print("SORU-6 CEVAP",slc)

#Alternatif
"""
Küçük bir ek bilgi: Eğer Python’da hazır fonksiyon kullanmak istersek,
collections.Counter diye bir modül var.
Onunla bu işlem tek satırda da yapılabiliyor:

from collections import Counter
print(Counter("python"))
"""


# SORU-5 CEVAP:
list_1 = [2,3,4,5,6,7,11,12]
k = 1 
for i in list_1:
    if i % 2 == 0:
        k *= i
print("SORU-5 CEVAP:",k)


# SORU-4 CEVAP:
def anagram(s1,s2):
    return sorted(s1) == sorted(s2)
    
print("SORU-4 CEVAP:",anagram("listen","silent"))
print("SORU-4 CEVAP:",anagram("Hello","World"))


# SORU-3 CEVAP:
def fibonacci(n):
    dizi = [0, 1]   # ilk iki eleman
    while len(dizi) < n:
        dizi.append(dizi[-1] + dizi[-2])
    return "SORU-3 CEVABI: ",dizi[:n]
"""
terim = int(input("Lütfen bir sayı giriniz"))
print(fibonacci(terim))
"""


# SORU-2 CEVAP:
kelimeler = "Bugün hava çok güzel"
ayirma = kelimeler.split()

siralama = sorted(ayirma, key=len)
print("SORU-2 CEVABI:",siralama)


# SORU-1 CEVAP:
list_1 = [1,2,2,3,3,3,4]
sayac = {}

for i in list_1:
    if i in sayac:
        sayac[i] += 1
    else:
        sayac[i] = 1
print("SORU-1 CEVABI: ",max(sayac,key=sayac.get))
