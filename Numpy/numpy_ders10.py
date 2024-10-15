import numpy as np

# Koşullu eleman işlemleri

# Bir vektör oluştur
vector = np.array([1, 2, 3, 99, 99, 3, 2, 1])

# Koşullu işlem: 40'tan küçük olan elemanlar True, diğerleri False
print(vector < 40)

# 40'tan küçük olan elemanları getir
print(vector[vector < 40])

# 40'tan büyük olan elemanları getir
print(vector[vector > 40])

# 40 veya daha küçük olan elemanları getir
print(vector[vector <= 40])

# 40 veya daha büyük olan elemanları getir
print(vector[vector >= 40])

# 40'a eşit olmayan elemanları getir
print(vector[vector != 40])

# Vektör elemanlarının her birini 2 ile çarp
print(vector * 2)

# Vektör elemanlarını 5'e böl
print(vector / 5)

# Vektör elemanlarını önce 5 ile çarp, sonra 10'a böl
print(vector * 5 / 10)

# Vektör elemanlarının karesini al
print(vector ** 2)
