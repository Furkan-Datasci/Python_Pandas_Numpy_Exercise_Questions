'''
    Daire Alanı = πr²
    Daire Çevresi = 2πr
    
    * Yarı çapı verilen bir dairenin alan  ve çevresini 
    hesaplayınız.(r:3.14)

''' 
pi = 3.14

r = float(input("yarı çap:"))

alan = pi * (r ** 2)
print('Alan = ', type(alan))
 
cevre = 2 * pi * r
print('Çevre =' , type(cevre))

print("alan: " + str(alan) + " Çevre: " + str(cevre))
