import numpy as np

# Array alt küme işlmeleri (Slicing)

# Vektörlerde slice işlemleri

# 20 ile 30 arasında sıralı bir vektör oluşturma
a = np.arange(20,30)
# Vtörü yazdırma
print(a)

# 0. indeksten 3.indekse kadar (3 dahil değil) seçme işlemi
print(a[0:3])

# En baştan 3.indekse kadar (3 dahil değil) seçme işlemi
print(a[:3])

# 3.indeksten sonuncu indekse kadar seç
print(a[3:])

# 1.indeksten başlayıp ikişer ikişer artarak seçme
print(a[1::2])

# ----------------------------------

# Matrislerde slice işlemleri

# 5x5 lik random bir matris oluşturduk
b = np.random.randint(10, size=(5,5))
# matrisi yazdırma
print(b)

# satır olarak hepsini sütun olarak 0. sütunu al
print(b[:,0])

# 0.satır ve tüm sütunları seç
print(b[0,:])

# 0'dan 2'ye kadar satırları, 0'dan 3'e kadar sütunları al
print(b[0:2, 0:3])