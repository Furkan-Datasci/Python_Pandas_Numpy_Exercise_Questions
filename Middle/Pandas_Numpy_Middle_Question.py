import pandas as pd
import numpy as np

# np.arange kullanarak 0’dan 50’ye kadar 7’nin katlarını içeren bir array oluştur.
array = np.arange(0,50,7)
print(array)

# np.linspace ile 0 ile 1 arasında 10 eşit bölünmüş değer üret.
array_2 = np.linspace(0,1,10)
print(array_2)

# np.eye kullanarak 5x5 birim matrisi oluştur.
array_3 = np.eye(5,5)
print(array_3)

# np.random.randint ile 1–100 arasında rastgele (4x4) matris oluştur.
array_4 = np.random.randint(1,101,size = (5,5))
print(array_4)

# Yukarıdaki matrisin en büyük ve en küçük elemanını bul.
print(f"Max değer: {np.max(array_4)} , Min Değer: {np.min(array_4)}")

# np.array([1,2,3,4,5]) dizisini ters çevir.
array_5 = np.array([1,2,3,4,5])
print(array_5[::-1])

# np.zeros ile (3,4,2) boyutunda sıfırlardan oluşan bir dizi oluştur.
array_6 = np.zeros((3,4,2))
print(array_6)

# [1, 2, 3, 4] ve [5, 6, 7, 8] dizilerini yatay ve dikey olarak birleştir.
array_7 = np.array([1, 2, 3, 4]) 
array_8 = np.array([5, 6, 7, 8])
print(f"Yatay olarak birleştirme: {np.hstack((array_7,array_8))}")
print(f"{np.vstack((array_7,array_8))} : Dikey olarak birleştirme")

# np.array([[1,2,3],[4,5,6],[7,8,9]]) matrisinde 2. satırı al.
array_9 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(f"2. satırdaki değerler: {array_9[1]}")

# np.array([1,2,3,4,5,6,7,8,9]) dizisini 3x3 matrise reshape et.
array_10 = np.array([1,2,3,4,5,6,7,8,9])
print(array_10.reshape(3,3))

"""------------------------------Pandas soruları 10 soru------------------------------------"""

# Bir sözlükten DataFrame oluştur:
data = {"Name": ["Ali", "Veli", "Ayşe"], "Age": [25, 30, 22], "City": ["Bursa", "İstanbul", "Ankara"]}
frame = pd.DataFrame(data)
"print(frame)"
    
# df içindeki ilk 2 satırı getir (head).
"print(frame.head(2))"

# df’deki Age sütununu seç.
""""print(frame["Age"])"""

# df’de sadece Age > 25 olan satırları filtrele.
mask = frame["Age"]>25
"print(frame[mask])"
"""print(frame["Age"][mask])"""

# Yeni bir sütun ekle: "Salary" = [3000, 4000, 3500].
"""
frame["Salary"] =  [3000, 4000, 3500]
print(frame)
"""
"""
df = pd.DataFrame({"Salary":[3000, 4000, 3500]})
print(df)
"""

# df’yi Age sütununa göre küçükten büyüğe sırala.
print(frame.sort_values(by="Age"))

# df’deki ortalama Age değerini hesapla.
print(frame["Age"].mean())

# df’yi City sütununa göre grupla ve her grubun ortalama yaşını bul.
df = frame.groupby("City")["Age"].mean()
print(df)

# df.to_csv("output.csv", index=False) komutunu çalıştır – CSV’ye yaz.
frame.to_csv("mean_pandas.csv",index=False)

# pd.read_csv("output.csv") ile CSV dosyasını tekrar oku.
print(pd.read_csv("mean_pandas.csv"))