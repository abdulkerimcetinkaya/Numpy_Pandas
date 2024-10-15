import numpy as np

# Array Özellikleri

# ndim : Dizinin kaç boyutlu olduğunu gösterir.
# shape : Dizinin boyut bilgilerini (satır, sütun sayısı gibi) gösterir.
# size : Dizide toplam kaç eleman olduğunu gösterir.
# dtype : Dizideki elemanların veri tipini gösterir.

# Tek boyutlu dizi (Vektör) oluşturma
print("Tek boyutlu a dizisi")
# 10 elemanlı, 0 ile 9 arasında rastgele tam sayılardan oluşan bir dizi oluşturuluyor.
a = np.random.randint(10, size=10)
print(a)
# Dizinin boyut sayısını yazdır
print(a.ndim)
# Dizinin boyut bilgisi (kaç eleman içerdiği)
print(a.shape)
# Dizinin toplam eleman sayısı
print(a.size)
# Dizideki elemanların veri tipi
print(a.dtype)


print("-"*45)


# 2 Boyutlu Dizi (Matris) oluşturma
print("Çift boyutlu b dizisi")
# 3 satır ve 5 sütundan oluşan, 0 ile 9 arasında rastgele tam sayılardan oluşan bir dizi (matris) oluşturuluyor.
b = np.random.randint(10, size=(3, 5))
print(b)
# Dizinin boyut sayısını yazdır
print(b.ndim)
# Dizinin boyut bilgisi
print(b.shape)
# Dizinin toplam eleman sayısı
print(b.size)
# Dizideki elemanların veri tipi
print(b.dtype)
