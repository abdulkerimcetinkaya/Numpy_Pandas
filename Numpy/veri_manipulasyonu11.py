import numpy as np

# Matematiksel işlemler

# Bir vektör (dizi) oluştur
a = np.array([8, 5, 7, 1, 9, 2, 3, 6, 4])

# ufunc (evrensel fonksiyonlar) kullanımı

# Her elemandan 2 çıkarma
print(np.subtract(a, 2))

# Her elemanı 2 ile çarpma
print(np.multiply(a, 2))

# Her elemanı 2'ye bölme
print(np.divide(a, 2))

# Her elemana 2 ekleme
print(np.add(a, 2))

# Her elemanın karesini alma
print(np.power(a, 2))

# Her elemanın 2 ile bölümünden kalanı bulma (mod alma)
print(np.mod(a, 2))

# Negatif bir sayının mutlak değerini alma
print(np.absolute(np.array([-3])))

# 360 derecenin sinüs değeri
print(np.sin(np.radians(360)))  # Dereceyi radiana çevirip hesaplama yapıyoruz

# 180 derecenin kosinüs değeri
print(np.cos(np.radians(180)))  # Aynı şekilde dereceyi radiana çeviriyoruz
