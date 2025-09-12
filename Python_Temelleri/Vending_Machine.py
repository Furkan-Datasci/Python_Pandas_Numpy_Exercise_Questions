#!/bin/python3

import math
import os
import sys

class VendingMachine:
    def __init__(self, num_items, item_coins):
        self.stock = num_items  # Başlangıçtaki ürün sayısı
        self.price = item_coins  # Ürün başına fiyat

    def buy(self, num_items, num_coins):
        # 1️⃣ Yeterli ürün var mı kontrol et
        if num_items > self.stock:
            raise ValueError("Not enough items")
        
        # 2️⃣ Kullanıcının parası yeterli mi kontrol et
        total_cost = num_items * self.price
        if num_coins < total_cost:
            raise ValueError("Not enough coins")
        
        # 3️⃣ Satış işlemi: ürünleri düş, para üstünü hesapla
        self.stock -= num_items  # Ürün sayısını güncelle
        change = num_coins - total_cost  # Para üstü hesapla
        
        return change  # Para üstünü döndür

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # İlk giriş: otomatın başlangıç değerleri
    num_items, item_coins = map(int, input().split())
    machine = VendingMachine(num_items, item_coins)

    # Kaç işlem yapılacağını al
    n = int(input())
    for _ in range(n):
        num_items, num_coins = map(int, input().split())
        try:
            change = machine.buy(num_items, num_coins)  # Satın alma işlemi
            fptr.write(str(change) + "\n")  # Para üstünü yaz
        except ValueError as e:
            fptr.write(str(e) + "\n")  # Hata mesajını yaz

    fptr.close()


""" "raise" ne işe yarıyor: 
Bir Hata Verdirmek. Python kodlayıcısı olarak bir durum gerçekleştiğinde
uygulamanın hata vermesini isteyebiliriz. 
Bunun için raise komutu kullanırız."""