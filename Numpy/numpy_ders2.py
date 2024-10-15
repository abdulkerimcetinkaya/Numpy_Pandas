import numpy as np

# Şekil Değiştirme (Reshaping)

# Tek boyutlu dizi (Vektör)
# 1'den 9'a kadar sayılar içeren tek boyutlu bir dizi oluşturuluyor.
a = np.arange(1, 10)
print(a)  # [1 2 3 4 5 6 7 8 9]

# 2 Boyutlu Dizi (Matris)
# 1'den 9'a kadar sayıları içeren diziyi 3x3'lük bir matrise dönüştürüyoruz.
b = np.arange(1, 10).reshape((3, 3))
print(b)  # [[1 2 3] [4 5 6] [7 8 9]]

# Tekrar tek boyutlu bir dizi oluşturma
c = np.arange(1, 10)  # [1 2 3 4 5 6 7 8 9]
print(a.ndim)

# 'a' dizisinin boyutunu (reshape) değiştirme
# 'a' dizisini 1 satır ve 9 sütun olacak şekilde yeniden şekillendiriyoruz.
d = a.reshape((1, 9))
print(d.ndim)  # 2, çünkü artık dizi 2 boyutlu hale geldi (1 satır, 9 sütun)
print(d.shape)  # (1, 9), yani 1 satır ve 9 sütundan oluşan bir dizi.
