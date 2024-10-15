import numpy as np

# Alt küme üzerinde copy metodu

# 5x5 boyutunda rastgele tam sayılardan oluşan bir matris oluştur
a = np.random.randint(10, size=(5,5))
print(a)

# İlk 3 satır ve ilk 2 sütunu dilimle ve alt_a adlı değişkene ata
alt_a = a[0:3, 0:2]
print(alt_a)

# Dilimlenmiş verinin ilk elemanını değiştir
alt_a[0, 0] = 999
# Dilimlenmiş verinin ikinci satır ikinci sütun elemanını değiştir
alt_a[1, 1] = 888
# Orijinal dizi de etkilendiği için a matrisini tekrar yazdır
print(a)

# ------------------------------------------------------------

# Yeni bir 5x5 boyutunda rastgele tam sayılardan oluşan b dizisi oluştur
b = np.random.randint(10, size=(5,5))
print(b)

# a dizisinin belirli bir kısmının kopyasını oluştur ve alt_b adlı değişkene ata
alt_b = a[0:3, 0:2].copy()
print(alt_b)

# alt_b üzerinde değişiklik yap, bu değişiklik sadece alt_b'yi etkiler
alt_b[0, 0] = 999

# Orijinal b dizisi üzerinde değişiklik yapılmadığı için b'yi tekrar yazdır
print(b)

# alt_b'nin değişmiş hali
print(alt_b)
