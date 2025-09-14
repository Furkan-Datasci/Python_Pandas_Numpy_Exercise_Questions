website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1- 'course' karakter dizisinde kaç karakter bulunmaktadır ?
result = len(course)
lenght = len(website)

# 2- 'website' içinden www karakterlerini alın .
result = website[7:10]

# 3- 'website' içinden com karakterlerini çıkarın.
result = website[22:25]
result = website[lenght-3:lenght]

# 4- 'course' içinden ilk 15 ve son 15 karakterlerini alın.
result = course[0:15]+ course[-15:]

# 5- 'course' ifadesindeki karakterleri tersten yazdırın .
# result = course[-1:0:-1] Bana ait olan
result = course[::-1] 

name, surname, age, job = 'Bora', 'Yılmaz', 32, 'mühendis'

# 6- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
# 'Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim mühendis.'
result = "Benim adım "+ name +" "+ surname + ", Yaşım " + str(age) + "ve mesleğim "+ job
result = "Benim adım {} {} , Yaşım {} ve mesleğim {}." 
result = f"Benim adım {name} {surname}, Yaşım {age} ve mesleğim {job} "

# 7- 'Hello world' ifadesindeki w harfini 'W' ile değiştirin.
s =  'Hello world'
result = s[:6] +"W"+ s[-4:]
# result = s.replace('w',"W")

# 8- 'abc' ifadesini yan yana 3 defa yazdırın.

result = "abc"*3
 
print(result)

