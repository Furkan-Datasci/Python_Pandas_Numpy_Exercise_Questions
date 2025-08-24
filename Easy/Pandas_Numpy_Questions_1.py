import numpy as np
import pandas as pd
import seaborn as sb
import random as rd

# SORU-1: 0’dan 20’ye kadar olan sayılardan oluşan bir NumPy array oluştur
# ve sadece çift sayıları ekrana yazdır.
"""
arr = np.arange(0,21,1)
cift_sayilar = arr[arr % 2 == 0]
print(cift_sayilar)
"""


# SORU-2: 5x5 boyutunda birim matris (identity matrix) oluştur.
"""
matr = np.identity(5)   
print(matr)
"""

# SORU-3: 10 elemanlı 0–1 arası rastgele sayılardan oluşan bir NumPy array üret.
# Ortalamasını bul.
"""
arr = np.random.rand(10)
ortalama = np.mean(arr)

print(arr)
print("Ortalama: ",ortalama)
"""


# SORU-4: Bir NumPy array’indeki tüm negatif değerleri 0 ile değiştir.
# Örn: [-1, 3, -5, 7] → [0, 3, 0, 7]
"""
arr = np.array([-1, 3, -5, 7])
arr[arr < 0 ] = 0
print(arr)
"""


# SORU-5: [1,2,3,4,5] dizisinin kümülatif toplamını (cumsum) hesapla.
# Örn: [1,3,6,10,15]
"""
arr = np.array([1,2,3,4,5])
print(np.cumsum(arr))
"""

# SORU-6: 3x3 boyutunda rastgele tamsayılardan oluşan bir matris üret.
# Satır toplamlarını bul.
"""
arr = np.random.randint(0,20,(3,3))
toplam = arr.sum(axis=1)
print(arr)
print(toplam)
"""


# SORU-7: 4x4 boyutunda bir matris üret.
# Köşegen (diagonal) elemanlarının toplamını bul.
"""
arr = np.random.randint(0,40,(4,4))
diag_sum = 0
for i in range(4):
    diag_sum += arr[i,i]
print(arr)
print("diag_toplam = ",diag_sum)
"""


# SORU-8: 10x10 boyutunda rastgele sayılardan oluşan bir matris üret.
# En büyük ve en küçük değerleri bul.
"""
arr = np.random.randint(0,100,(10,10))
print(arr)
print(np.max(arr),np.min(arr))
"""

# SORU-9: 12 elemanlı bir NumPy array’i oluştur ve bunu 3x4 matrise dönüştür.
"""
arr = np.random.randint(0,20,(4,3))
print(arr)
print(arr.reshape(3,4))
"""


# SORU-10: İki NumPy array’ini eleman bazlı çarp.
# Örn: [1,2,3] ve [4,5,6] → [4,10,18]
"""
arr_1 = np.array([1,2,3])
arr_2 = np.array([4,5,6])
carpim = arr_1 * arr_2
print(carpim)
"""


"PANDAS SORULARI"

# SORU-11: Sütunları ["isim", "yaş", "şehir"] olan bir DataFrame oluştur.
# İçine 3 satırlık örnek veri ekle.
veri = [["Aleyna",22,"Yozgat"],
        ["Furkan",22,"Yozgat"],
        ["Fatih",30,"Bursa"]  ]
df= pd.DataFrame(veri,columns=["isim", "yaş", "şehir"])
"""
print(df)
"""


# SORU-12: Yukarıdaki DataFrame’den sadece "yaş" sütununu seç.
"""print(df["yaş"])"""



# SORU-13: "yaş" sütununun ortalamasını hesapla.
"""print(df["yaş"].mean())"""


# SORU-14: "şehir" sütununda Yozgat olan satırları filtrele.
"""
filtered = df[df["şehir"]== "Yozgat"] 
print(filtered)
"""

# SORU-15: Yeni bir sütun ekle → "emekli_mi".
# Eğer yaş > 60 ise True, değilse False.
"""
df["emekli mi?"] = df["yaş"] > 60
print(df["emekli mi?"])
"""


# SORU-16: Bir CSV’den okunan DataFrame’de "maas" sütununu büyükten küçüğe sırala.
"""
veriler = {
    "isim": ["Ali", "Ayşe", "Mehmet", "Fatma", "Furkan"],
    "departman": ["IT", "HR", "IT", "Finance", "HR"],
    "maas": [12000, 9500, 15000, 11000, 13500]
}

df = pd.DataFrame(veriler)
df.to_csv("maaslar.csv", index=False)
print("CSV dosyası oluşturuldu!")

df_1 = pd.read_csv("maaslar.csv")
print(df_1.head())
"""


# SORU-17: Bir DataFrame’de eksik (NaN) değerleri bul ve her sütundaki sayısını yazdır.
"""
data = {
    "isim": ["Ali", "Ayşe", "Mehmet", None],
    "yas": [20, None, 22, 21],
    "not": [85, 90, None, 70]
}
df = pd.DataFrame(data)
print(df.isnull().sum())
"""


# SORU-18: DataFrame’i "departman" sütununa göre grupla.
# Her grup için ortalama maaşı hesapla.
"""
data = {
    "isim": ["Ali", "Ayşe", "Mehmet", "Fatma", "Ahmet", "Zeynep"],
    "departman": ["IT", "IT", "HR", "HR", "IT", "HR"],
    "maas": [5000, 6000, 4000, 4500, 7000, 4800]
}
df = pd.DataFrame(data)
df.to_csv("departman.csv",index=False)
print(df.groupby("departman")["maas"].mean())
"""


# SORU-19: "tarih" sütunu olan bir DataFrame’de,
# yıl bazında kaç satır olduğunu say.
"""
data = {
    "isim": ["Ali", "Ayşe", "Mehmet", "Fatma"],
    "tarih": ["2022-05-01", "2022-07-13", "2023-01-20", "2023-03-11"]
}

df_2 = pd.DataFrame(data)
df_2.to_csv("tarıh.csv",index=False)

df_2["tarih"] = pd.to_datetime(df_2["tarih"])
print(df_2.groupby(df_2["tarih"].dt.year).size())
"""


# SORU-20: İki DataFrame’i "isim" sütununa göre birleştir (merge).
"""
df_2 = pd.read_csv("departman.csv")
print(pd.merge(df,df_2,on="isim",how="inner"))
"""

"""-----------------------------Apply , Map, Lambda Soruları---------------------------"""

