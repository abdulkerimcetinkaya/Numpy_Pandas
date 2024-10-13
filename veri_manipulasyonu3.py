import numpy as np

# Array (dizi) birleştirme işlemi (concatenation)

# Vektörler ile birleştirme
# x, y ve z adlı 1 boyutlu numpy dizilerini oluşturuyoruz
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
z = np.array([7, 8, 9])

# Vektörlerin birleştirilmesi
# np.concatenate ile dizileri birleştiriyoruz. Sonuç tek boyutlu bir vektör olur.
vector = np.concatenate([x, y, z])
print(vector)  # [1 2 3 4 5 6 7 8 9]

# Matrisler ile birleştirme
# a, b ve c adlı 2 boyutlu numpy dizilerini oluşturuyoruz.
a = np.array([[1, 2, 3],
              [4, 5, 6]])

b = np.array([[7, 8, 9],
              [10, 11, 12]])

c = np.array([[13, 14, 15],
              [16, 17, 18]])

# Dikey olarak (satır bazlı) matrislerin birleştirilmesi (axis=0 varsayılan)
# Birleştirilen matrisin boyutu satır bazında artar.
matris = np.concatenate([a, b, c])
print(matris)
# Çıktı:
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]
#  [13 14 15]
#  [16 17 18]]

# Yatay olarak (sütun bazlı) matrislerin birleştirilmesi (axis=1)
# Bu sefer birleştirilen matrisin boyutu sütun bazında artar.
matris2 = np.concatenate([a, b, c], axis=1)
print(matris2)
# Çıktı:
# [[ 1  2  3  7  8  9 13 14 15]
#  [ 4  5  6 10 11 12 16 17 18]]
