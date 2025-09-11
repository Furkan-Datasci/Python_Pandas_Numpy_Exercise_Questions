'''
öğrenciler = {
    '120' :{
        'Ad' = 'Ali',
        'Soyad' = 'Yılmaz',
        'Telefon' = '532 333 00 01'
    },
    '125' : {
        'ad' = 'Can',
        'soyad' = 'Korkmaz',
        'Telefon' = '532 129 06 09'
    
    },
    '130' : {
        'Ad ' = 'Volkan',
        'Soyad' = 'Yükselen',
        'Telefon' = '552 216 09 83'
    },
}

    1- Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle 
    dictioanary içinde saklayınız.

    2-Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin . 

'''
ogrenciler = {}

number = input("öğrenci number: ")
name = input("öğrenci name: ")
surname = input("öğrenci surname: ")
phone = input("örenci phone: ")


# ogrenciler[number] = {
#     'ad' : name ,
#     'soyad' : surname , 
#     'numara' : phone ,
# }

ogrenciler.update({
    number : {
        'ad': name ,
        'soyad': surname ,
        'tel no' : phone ,
    }
})

print(ogrenciler)