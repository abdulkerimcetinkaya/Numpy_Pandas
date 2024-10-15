import numpy as np

# Array Sıralama (Sorting)

# Vektör ile sıralama
a = np.array([8, 5, 7, 1, 9, 2, 3, 6, 4])

# np.sort() kullanımı:
# Bu fonksiyon array'in orijinal yapısını değiştirmeden sıralanmış bir kopyasını döndürür.
a_sort = np.sort(a)
print(a_sort)
# Çıktı: [1 2 3 4 5 6 7 8 9]

# .sort() kullanımı:
# Bu fonksiyon array'in orijinal yapısını kalıcı olarak değiştirir ve array'i yerinde sıralar.
a.sort()
print(a)
# Çıktı: [1 2 3 4 5 6 7 8 9]

# 3x3 boyutunda rastgele bir matris oluşturuyoruz (normal dağılım kullanarak)
b = np.random.normal(20, 5, (3, 3))
print(b)
# Örneğin çıktı:
# [[17.  23.2 22.1]
#  [19.  25.  15. ]
#  [22.  18.  20. ]]

# Satırları sıralama:
# axis=1 parametresi, her satırın kendi içinde sıralanacağı anlamına gelir.
sirali1 = np.sort(b, axis=1)
print(sirali1)
# Çıktı (satır bazlı sıralama):
# [[17.  22.1 23.2]
#  [15.  19.  25. ]
#  [18.  20.  22. ]]

# Sütunları sıralama:
# axis=0 parametresi, her sütunun kendi içinde sıralanacağı anlamına gelir.
sirali2 = np.sort(b, axis=0)
print(sirali2)
# Çıktı (sütun bazlı sıralama):
# [[17.  18.  15. ]
#  [19.  23.2 20. ]
#  [22.  25.  22.1]]
