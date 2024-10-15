import numpy as np

# Array Ayırma (Splitting)

# Vektör ile ayırma
x = np.array([1, 2, 3, 99, 99, 3, 2, 1])

# np.split ile vektörü 3 parçaya ayırıyoruz.
# [3,5] parametresi 3. ve 5. indekslerde bölünme noktalarını belirler.
a, b, c = np.split(x, [3, 5])

# 3 parçaya ayrılan vektörü yazdırıyoruz.
print(a, b, c)
# Çıktı:
# [1 2 3] [99 99] [3 2 1]
print("-" * 45)

# Matris ile ayırma
# 4x4 boyutunda bir matris oluşturuyoruz (0'dan 15'e kadar sayılarla)
m = np.arange(16).reshape(4, 4)
print(m)
# Çıktı:
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]]

# Dikey olarak matris bölme (vsplit)
# np.vsplit ile matrisin satır bazında bölünmesi
# [2] parametresi 2. satırdan itibaren böler.
print("vsplit'den sonra")
alt, ust = np.vsplit(m, [2])
print(alt, ust)
# Çıktı:
# [[0 1 2 3]
#  [4 5 6 7]] [[ 8  9 10 11]
#              [12 13 14 15]]

# Yatay olarak matris bölme (hsplit)
# np.hsplit ile matrisin sütun bazında bölünmesi
# [2] parametresi 2. sütundan itibaren böler.
sag, sol = np.hsplit(m, [2])
print(sag, sol)
# Çıktı:
# [[ 0  1]
#  [ 4  5]
#  [ 8  9]
#  [12 13]] [[ 2  3]
#            [ 6  7]
#            [10 11]
#            [14 15]]
