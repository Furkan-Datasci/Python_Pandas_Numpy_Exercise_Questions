#!/bin/python

import math
import os
import sys

# Dikdörtgen sınıfı
class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def area(self):
        return self.a * self.b

# Daire sınıfı
class Circle:
    def __init__(self, r):
        self.r = r
    
    def area(self):
        return math.pi * (self.r ** 2)  # math.pi kullanılmalı!

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')  # Çıktıyı dosyaya yazacak
    q = int(input())  # Kullanıcıdan giriş al
    queries = []

    for _ in range(q):  # xrange yerine range kullanıldı (Python 3 uyumu)
        args = input().split()  # Kullanıcıdan input al ve boşluklara göre böl
        shape_name, params = args[0], list(map(int, args[1:]))  # Şekil adını ve parametreleri al

        if shape_name == "rectangle":
            a, b = params[0], params[1]
            shape = Rectangle(a, b)  # Dikdörtgen nesnesi oluştur
        elif shape_name == "circle":
            r = params[0]
            shape = Circle(r)  # Daire nesnesi oluştur
        else:
            raise ValueError("invalid shape type")  # Hatalı giriş yapılırsa hata ver

        fptr.write("%.2f\n" % shape.area())  # Alanı hesapla ve dosyaya yaz
    fptr.close()  # Dosyayı kapat
