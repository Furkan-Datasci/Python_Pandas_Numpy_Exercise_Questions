names = ['Ali','Yağmur','Hakan','Deniz']
years = [1998,2000,1998,1987]

#   "Cenk" ismini listenin sonuna ekleyiniz.
#names.append('Cenk')

#   "Sena" değerini listenin başına ekleyiniz.
#names.insert(0,'Sena')
#names.insert(len(names),'Mehmet')

#   "Deniz" ismini listeden siliniz .
#index = names.index('Deniz')
#names.pop(index)
#names.pop(-2)

#   "Deniz" isminin indeksi nedir?
#print(names.index('Deniz'))

#   "Ali" listenin elamanı mıdır?
result = 'Ali' in names

#   Liste elemanlarını ters çevirin. 
#names.reverse()
#years.reverse()

#   Liste elemanlarını alfabetik olarak sıralayınız.
#   names.sort()

#   years listesini rakamsal büyüklüğe göre sıralayınız. 
#years.sort()
#years.reverse()

#   str = "Chevrolet,Dacia" karakter dizisini listeye çeviriniz.
str = "Chevrolet,Dacia"
result = str.split(',')
print(result)

#   years dizisinin en büyük ve en küçük elemanı nedir ?
# max = max(years)
# min = min(years)
# print(max,min)

#   years dizisinin kaç tane 1998 elamnı vardır ? 
#print(years.count(1998))

#   years dizisinin tüm elemanlarını siliniz .
#years.clear()

#   Kullanıcıdan aldığınız 3 tane marka bilgisini bir listede  saklayınız.
markalar = []

marka = input("marka: ")
markalar.append(marka)


marka = input("marka: ")
markalar.append(marka)


marka = input("marka: ")
markalar.append(marka)

print(markalar)



# print(names)
# print(years)
