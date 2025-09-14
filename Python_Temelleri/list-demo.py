# 1- "Bmw,Mercedes,Opel,Mazda"elemanlarına sahip bir liste oluşturunuz.
arabalar = ['BMW','Mercedes','Opel','Mazda']

# 2- liste kaç elemanlıdır ?
result = len(arabalar)

# 3- Listenin ilk ve son elemanı nedir ? 
result =  arabalar[0]
result = arabalar[-1]

# 4- Mazda değerini  Toyota ile değiştirin.
result = arabalar[3].replace('Mazda','Toyota' )

# 5- Mercedes listenin bir elemanı mıdır ? 
result = arabalar[0].startswith('Mercedes')
result = 'mercedes' in arabalar  

# 6- listenin -2 indeksindeki değer nedir ? 
result = arabalar[-2]

# 7- Listenin ilk 3 elemanı alın. 
result = arabalar[0] + arabalar[1] + arabalar[2]
result = arabalar[0:3]

# 8- Listenin son iki elemanı yerine "Toyota" ve "Renault" değerlerini ekleyin.
arabalar[-1] = 'Toyota'
arabalar[-2] = 'Renault'
arabalar[-2:] = ['Toyota' , 'Renault'] 

# 9- Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin .
result = arabalar + ['Audi' , 'Nissan'] 

# 10-Listenin son elemanını silin 
result = arabalar[0:-1]
del arabalar[-1]
result = arabalar
# 11-Listenin son elemanlarını tersten yazdırın.
result = arabalar[::-1]

# 12-Aşağıdaki verileri bir liste içinde saklayınız. 

            # studentA : Yiğit Bilgi 2010 , (70,60,70)
            # studentB : Sena Turan  1999 , (80,80,70)
            # studentC : Ahmet Turan 1998 , (80,70,90)

studentA = ['Yiğit' , 'Bilgi ' , 2010 , [70,60,70] ]
studentB = ['Sena' , 'Turan' , 1999 , [80,80,70]]
studentC = ['Ahmet' ,' Turan' , 1998 , [80,70,90]]

# 13-Liste elemanlarını ekrana yazdırınız.
result = studentA[0]
result = studentB[1]
result = studentC[3]
result = f"{studentA[0]} {studentA[1]} {2019-studentA[2]} yaşında ve not ortalaması {studentA[3][1]} "

print(arabalar)
print(result)