import pandas as pd
import numpy as np

# NumPy array'inden bir pandas Series (Seri) oluşturma
a = np.array([15, 25, 37, 42, 55])
seri = pd.Series(a, index=["a", "b", "c", "d", "e"])  # Her değere özel bir index atıyoruz
print(seri)  # Oluşturulan seriyi ekrana yazdırma

# Serinin index bilgilerine erişme
print(seri.index)  # Serinin index'lerini gösterir

# Serinin anahtarlarına (indexlere) erişme (keys() bir fonksiyon)
print(seri.keys)  # Serinin index bilgilerine ulaşmayı sağlar

# Serinin elemanlarını hem index hem de değer olarak listeleme
print(list(seri.items()))  # Her bir index ve değeri bir tuple olarak listeler

# Serinin sadece değerlerine erişme
print(seri.values)  # Serideki değerleri bir NumPy array olarak döndürür

# Belirli bir index'in seride olup olmadığını kontrol etme
print("a" in seri)  # 'a' index'i seride var mı diye kontrol eder, sonuç True/False olur
