import numpy as np
import pandas as pd

# 1 ile 30 arasında rastgele 10x3 boyutunda bir matris oluşturuluyor
m = np.random.randint(1, 30, (10, 3))

# Bu matrisi DataFrame'e dönüştürüyoruz ve sütun isimlerini belirliyoruz
df = pd.DataFrame(m, columns=['A', 'B', 'C'])
print("DataFrame:\n", df)

# loc: Etiket bazında satır seçimi, burada 0'dan 3'e kadar olan satırları seçiyoruz
# 0:3 dahil olduğu için 0'dan 3'e kadar olan satırlar seçilecek.
print("\nloc ile 0-3 arasındaki satırlar:\n", df.loc[0:3])

# iloc: Pozisyon bazında satır seçimi, burada 0'dan 3'e kadar olan satırları seçiyoruz
# Bu seçilimde 3. satır dahil değil, yani 0, 1, 2 satırları seçilecek.
print("\niloc ile 0-3 arasındaki satırlar:\n", df.iloc[0:3])

# loc ile belirli satır ve sütun seçimi
# Burada 2. ve 4. satırdan, 'A' ve 'B' sütunlarını alıyoruz
print("\nloc ile 2. ve 4. satırdan 'A' ve 'B' sütunlarını seçme:\n", df.loc[[2, 4], ['A', 'B']])

# iloc ile belirli satır ve sütun seçimi
# 1. ve 5. satırdan, 1. ve 2. sütunları seçiyoruz (index 0'dan başlar)
print("\niloc ile 1. ve 5. satırdan, 1. ve 2. sütunları seçme:\n", df.iloc[[1, 5], [0, 1]])

# DataFrame'den bir koşula bağlı olarak satır seçimi
# 'A' sütununda 10'dan büyük olan değerleri içeren satırlar seçiliyor
print("\n'A' sütununda 10'dan büyük olan satırlar:\n", df[df['A'] > 10])

# Tüm satırları alıp yalnızca belirli sütunları seçme
# Bu örnekte yalnızca 'B' sütununu alıyoruz
print("\nB sütununu alma:\n", df['B'])

# Tüm satırlarda 'A' ve 'B' sütunlarının toplamını yeni bir sütun olarak ekliyoruz
df['Sum_AB'] = df['A'] + df['B']
print("\nYeni sütun 'Sum_AB' eklenmiş DataFrame:\n", df)

# Birden fazla satır silme, 2. ve 4. satırları siliyoruz
df.drop([2, 4], axis=0, inplace=True)
print("\n2. ve 4. satırlar silindikten sonra:\n", df)
