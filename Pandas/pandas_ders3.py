import pandas as pd
import numpy as np

# NumPy array'i oluşturma ve DataFrame'e dönüştürme
l = np.arange(10, 20).reshape((5, 2))  # 10 ile 19 arasındaki sayıları 5x2 boyutunda bir array'e çevirme

# Bu NumPy array'ini pandas DataFrame'e dönüştürme
df = pd.DataFrame(l, columns=["deg1", "deg2"])  # Kolon isimlerini "deg1" ve "deg2" olarak belirledik
print(df)  # DataFrame'i ekrana yazdırma

# DataFrame'in eksenlerini gösterir (satır ve sütun bilgileri)
print(df.axes)

# DataFrame'in boyut bilgisi (satır sayısı, sütun sayısı)
print(df.shape)

# DataFrame'in boyut sayısı (kaç boyutlu olduğunu gösterir, 2D DataFrame olduğu için 2 dönecek)
print(df.ndim)

# DataFrame'deki toplam eleman sayısı (satır sayısı * sütun sayısı)
print(df.size)

# DataFrame'in saf değerlerine erişim (NumPy array olarak döner)
print(df.values)

# DataFrame'in `values`'unun veri tipi (NumPy array)
print(type(df.values))

# DataFrame'in ilk 5 satırını gösterir (head bir metot olduğundan parantez ile çağırmalısınız)
print(df.head())

# DataFrame'in son 5 satırını gösterir (tail bir metot olduğundan parantez ile çağırmalısınız)
print(df.tail())
