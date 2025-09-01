import numpy as np
import pandas as pd

# ---------------- NumPy + Pandas Karma Sorular ---------------- #

# 1. 1 ile 100 arasında rastgele 25 sayı üret (5x5 matris) ve her sütunun ortalamasını hesapla.
# Cevap:

"""
arr = np.random.randint(1, 101, (5, 5))e
print("Matris:\n", arr)

# sütunların ortalaması  (axis=0 sütun yönü demek)
col_means = arr.mean(axis=0)
print("Sütun Ortalamaları:\n", col_means)
"""

# ---------------------------------------------------------------

# 2. np.arange ile 1’den 20’ye kadar sayıları üret, 4x5 matrise reshape et. 
# Daha sonra her satırın maksimum değerini bul.
# Cevap:

"""
arr = np.arange(1,21).reshape(4,5).max(axis=1)
print(arr)
"""

# ---------------------------------------------------------------


# 3. Aşağıdaki sözlükten DataFrame oluştur. Salary sütununun ortalamasını al. 
# Ortalamanın üzerinde maaş alan kişileri filtrele.

data = {"Name": ["Ali","Ayşe","Veli","Fatma"],
        "Age": [25,30,22,28],
        "Salary": [5000,6000,4500,7000]}
# Cevap:
"""
frame = pd.DataFrame(data)
frame_Salary = frame["Salary"].mean()

yüksek_maas = frame[frame["Salary"] > frame_Salary]

print(frame)
print(f"AVG-Salary: {frame_Salary}")
print(f"Yüksek Maaş Alanlar: {yüksek_maas}")
"""

# ---------------------------------------------------------------


# 4. 10 elemanlı rastgele bir NumPy array oluştur. 
# Bu array’i pandas Series’e çevir ve 5’ten büyük elemanları seç.
# Cevap:
"""
random = np.random.randint(1,11,10)
series = pd.Series(random)
print(f"Array : {random}")
print(f"Series : \n{series[series>5]}")
"""
# ---------------------------------------------------------------


# 5. 1’den 12’ye kadar sayılardan bir NumPy array oluştur. 
# 3x4 matrise reshape et. Daha sonra Pandas DataFrame’e çevirip sütun isimlerini A, B, C, D yap.
# Cevap:
"""
arr = np.random.randint(1,13,12).reshape(3,4)
print(f"Array: \n{arr}")
frame = pd.DataFrame(arr)
frame.columns = ["A","B","C","D"]
print(f"frame: \n{frame}")
"""
# ---------------------------------------------------------------


# 6. df DataFrame’inde Age sütununa göre grupla ve Salary ortalamalarını bul. 
# Çıkan sonucu DataFrame olarak göster.
# (Önce data’yı tekrar DataFrame’e çevir)
# Cevap:
# print(f"Dataframe: \n{data}")
"""
frame = pd.DataFrame(data).groupby("Age")[["Salary"]].mean()
print(f"avg_salary: \n{frame}")
"""
# ---------------------------------------------------------------

# 7. 0 ile 1 arasında 100 rastgele sayı üret. NumPy kullanarak ortalama, median ve std hesapla.
# Cevap:
"""
arr = np.random.rand(100)

mean_val = np.mean(arr)
median_val = np.median(arr)
std_val = np.std(arr)

print("Ortalama:", mean_val)
print("Median:", median_val)
print("Standart Sapma:", std_val)
"""

# ---------------------------------------------------------------
# 8. Aşağıdaki DataFrame’den sadece “Math > 60 ve Science > 70” koşulunu sağlayan öğrencileri seç.

data2 = {"Name":["Ali","Ayşe","Veli","Fatma"],
         "Math":[50,80,65,90],
         "Science":[60,95,75,55]}
# Cevap:
"""
frame = pd.DataFrame(data2)
filtered = frame[(frame["Math"]>60) & (frame["Science"]>70)]
print(f"Filtreli Hali: \n{filtered}")
"""

# ---------------------------------------------------------------
# 9. 1’den 100’e kadar olan sayılardan NumPy array oluştur. 
# Bu array’den sadece çift sayıları seç ve Pandas Series’e dönüştür.
# Cevap:

"""
arr = np.arange(1,101)
seri = arr[arr % 2 == 0]
print(f"seri: {seri}")
"""

# ---------------------------------------------------------------

# 10. df3 DataFrame oluştur: “City, Temp, Rain”. 
# City’ye göre grupla → her şehrin ortalama sıcaklığını ve toplam yağışını bul.
df3 = pd.DataFrame({
    "City":["Bursa","İstanbul","Bursa","Ankara","İstanbul","Ankara"],
    "Temp":[30,28,32,25,27,24],
    "Rain":[5,10,0,12,8,7]
})
# Cevap:
"""
df3 = pd.DataFrame({
    "City":["Bursa","İstanbul","Bursa","Ankara","İstanbul","Ankara"],
    "Temp":[30,28,32,25,27,24],
    "Rain":[5,10,0,12,8,7]
})

result = df3.groupby("City").agg({
    "Temp": "mean",
    "Rain": "sum"
}).reset_index()

print(result)
"""

# ---------------------------------------------------------------
# 11. 5x5 rastgele matris üret. Köşegen (diagonal) elemanlarını çek ve ortalamasını bul.
# Cevap:



# ---------------------------------------------------------------


# 12. Aşağıdaki DataFrame’de “Age” sütununu kategorilere ayır: 
# 0-25 = “Genç”, 26-40 = “Orta”, 40+ = “Yaşlı”
df4 = pd.DataFrame({
    "Name":["Ali","Ayşe","Mehmet","Fatma"],
    "Age":[23,35,42,28]
})
# Cevap:
# ---------------------------------------------------------------

