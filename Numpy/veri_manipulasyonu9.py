import numpy as np

# Fancy Index ile elemanlara erişim

# Vektör ile
vector = np.arange(start=10, stop=50, step=5)  # 10'dan başlayarak 5'er 5'er artan bir vektör oluştur
print(vector)

# Belirli indekslerdeki elemanları almak için fancy indexing
vector_getir = [1, 3, 5]  # 1., 3. ve 5. indekslerdeki elemanları seç
print(vector[vector_getir])

# ---------------------------------------

# Matris ile
matris = np.arange(9).reshape((3,3))  # 0'dan 8'e kadar sayıları içeren 3x3'lük bir matris oluştur
print(matris)

# Fancy index kullanarak matrisin belirli satır ve sütun elemanlarını al
satir = np.array([0, 1])  # 0. ve 1. satırları seç
sutun = np.array([1, 1])  # 1. sütunları seç

print(matris[satir, sutun])  # Seçilen satır ve sütunlarındaki elemanları yazdır
