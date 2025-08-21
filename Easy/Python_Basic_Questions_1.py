#SORU-1: Bir listedeki en büyük sayıyı bulan bir fonksiyon yaz.
# Örn: [3, 7, 2, 9] → 9



#SORU-2: Bir string içindeki sesli harflerin (a, e, i, o, u) sayısını bulan bir fonksiyon yaz.
# Örn: "ankara" → 3



#SORU-3: 1’den 100’e kadar olan sayılardan sadece 3 ve 5’e aynı anda bölünebilenleri yazdır.



#SORU-4: Bir listenin ortalamasını hesaplayan fonksiyon yaz.
# Örn: [10, 20, 30] → 20.0


#SORU-5 Girilen sayının asal sayı olup olmadığını kontrol eden fonksiyon yaz.
# Örn: 7 → True, 9 → False



#SORU-6: Bir metindeki her kelimenin kaç kere geçtiğini sayan fonksiyon yaz.
# Örn: "merhaba dünya merhaba" → { "merhaba": 2, "dünya": 1 }




#SORU-7: Bir listedeki tekrar eden elemanları kaldırıp sadece benzersiz olanları döndür.
# Örn: [1,2,2,3,4,4] → [1,2,3,4]



#SORU-8: Bir listedeki en küçük sayıyı ve en büyük sayıyı aynı anda döndüren fonksiyon yaz.
# Örn: [4,1,9,2] → (1, 9)



#SORU-9: 0’dan 20’ye kadar olan çift sayıların karelerini liste halinde döndür.
# Örn: [0, 4, 16, ..., 400]




#SORU-10: Bir cümledeki kelimeleri tersten sırayla yazdır.
# Örn: "Python öğrenmek çok güzel" → "güzel çok öğrenmek Python"



#SORU-11: Bir liste veriliyor: [10, 20, 30, 40, 50].
# Bu listedeki elemanların toplamını kendin hesapla (yani sum() kullanmadan).


    
#SORU-12: Girilen bir kelimenin palindrom olup olmadığını kontrol eden bir fonksiyon yaz.
# Örn: "kayak" → True, "merhaba" → False




#SORU-13: 0’dan 50’ye kadar olan sayılardan sadece 7’nin katlarını liste halinde döndür.



#SORU-14: Bir cümledeki kelime sayısını bulan bir fonksiyon yaz.
# Örn: "Bugün hava çok güzel" → 4



#SORU-15: Bir listenin içindeki en büyük ikinci sayıyı döndüren fonksiyon yaz.
# Örn: [5, 9, 2, 8] → 8



#SORU-16: Kullanıcıdan alınan bir sayının faktöriyelini hesapla.
# Örn: 5! = 120



#SORU-17: Bir string’de geçen tüm karakterleri alfabetik sırayla yazdır.
# Örn: "python" → hnopty



#SORU-18: Bir listedeki tüm elemanları tersten döndür.
# Örn: [1, 2, 3, 4] → [4, 3, 2, 1]



#SORU-19: Bir listenin içindeki tek sayıların karelerini yeni bir listeye al.
# Örn: [1,2,3,4,5] → [1, 9, 25]



#SORU-20: Bir string’deki boşlukları kaldırıp geri kalanını yazdır.
# Örn: "Merhaba Dünya" → "MerhabaDünya"





#Soru-1 Cevap
list_1 = list([3, 7, 2, 9])
print("Soru-1 ",max(list_1))

#Soru-2 Cevap
kelime = "ben bu yarışmaya katılacağım."
sesli = "aeiouöı"
x=0
for i in kelime:
    if i in sesli:
        x += 1 
    else:
        continue
print("Soru-2 ",x)    
# Aletrnatif:
x = sum(1 for i in kelime if i in sesli )
print("Soru-2 ",x)  


#Soru-3 Cevap
x = list(range(1,101))
bölünebilen = []
for i in x:
    if i % 3 == 0 and i % 5 == 0 :
        bölünebilen.append(i)
print("Soru-3 ",bölünebilen)    


#Soru-4 Cevap
avarage = [10, 20, 30]
print("Soru-4 ",sum(avarage)/len(avarage))


#Soru-5 Cevap
aralik = list(range(2, 101))
asal = []

for i in aralik:
    is_asal = True
    for n in range(2, i):
        if i % n == 0:
            is_asal = False
            break
    if is_asal:
        asal.append(i)

print("Soru-5 ",asal)



#Soru-6 Cevap
kelime = "merhaba dünya merhaba"
kelimeler = kelime.split()   # ["merhaba", "dünya", "merhaba"]

frekans = {}  # boş sözlük

for k in kelimeler:
    if k in frekans:       # daha önce eklenmişse sayısını artır
        frekans[k] += 1
    else:                  # ilk defa görüyorsak 1’den başlat
        frekans[k] = 1

print("Soru-6 ",frekans)



#Soru-7 Cevap
list_2 = [1,2,2,3,4,4,5,6,7,8,8,8,9,9,9]
print("Soru-7 ",set(list_2))



#Soru-8 Cevap
list_3 = [4,1,9,2]
print("Soru-8 ",max(list_3),min(list_3))



#Soru-9 Cevap
list_1 = list(range(0,21))
cift_sayilar = []
for i in list_1:
    if i % 2 == 0:
        cift_sayilar.append(i)
print("Soru-9 ",cift_sayilar)



#Soru-10 Cevap
kelime = "Python öğrenmek çok güzel"
kelimeler = kelime.split()
ters = kelimeler[::-1]
print("Soru-10 "," ".join(ters))


#Soru-11 Cevap
toplam = 0
for i in [10, 20, 30, 40, 50]:
    toplam += i
print("Soru-11 ",toplam)


#Soru-12 Cevap
kelimeler = list(["kayak","merhaba"])
for i in kelimeler:
    if i == i[::-1]:
        print("Soru-12 ",i,"= True")
    else:
        print("Soru-12 ",i,"= False")


#Soru-13 Cevap
print("Soru-13",list(range(0,51,7)))


#Soru-14 Cevap
kelime = "Bugün hava çok güzel"
print("Soru-14",len(kelime.split()))


#Soru-15 Cevap
liste_4 = [5, 9, 2, 8,7,11,10,15,17,18,19,20]
index_adımı = 0
for i in liste_4:
    if max(liste_4) > i and i > liste_4[index_adımı]:
        max_deger = i
print("Soru-15 ",max_deger)
print("Soru-15 ",max(liste_4))        

# Başka bir yol:
"""
liste_4 = [5, 9, 2, 8, 7, 11, 10, 15, 17, 18, 19, 20]
benzersiz = list(set(liste_4))  # tekrar eden varsa kaldır
benzersiz.sort(reverse=True)    # büyükten küçüğe sırala
print("Soru-15", benzersiz[1])  # 2. en büyük sayı
"""


#Soru-16 Cevap
sayi = int(input("Lütfen bir sayı giriniz: "))
faktoriyel = 1 
if sayi <= 0:
    print("Soru-16","Lütfen tekrar deneyiniz!")
else:
    for i in list(range(1,sayi+1)):
        faktoriyel *= i  
    print("Soru-16",faktoriyel)  


#Soru-17 Cevap
kelime = "python"
siralama = sorted(kelime)
siralama 
print("Soru-17"," ".join(siralama))


#Soru-18 Cevap
list_1 = [1, 2, 3, 4]
print("Soru-18 ",list_1[::-1])


#Soru-19 Cevap
list_1 = [1,2,3,4,5]
list_2 = []
for i in list_1:
    list_2.append(i**2)
print("Soru-19 ",list_2)


#Soru-20 Cevap
print("Soru-20 ","Merhaba Dünya".replace(" ",""))


