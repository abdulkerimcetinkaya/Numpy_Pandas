import numpy as np
import pandas as pd

# Rastgele integer dizileri oluşturma (5 elemanlı)
s1 = np.random.randint(10, size=5)
s2 = np.random.randint(10, size=5)
s3 = np.random.randint(10, size=5)

# Bu dizileri bir sözlük yapısında birleştiriyoruz (her biri ayrı bir sütun)
sozluk = {"var1": s1, "var2": s2, "var3": s3}

# Sözlüğü pandas DataFrame'e çevirme
df = pd.DataFrame(sozluk)
print(df)  # DataFrame'i ekrana yazdırma

# İlk satırı (index 0 olan satır) getirme
print(df[0:1])

# İndeks isimlerini değiştirme (0,1,2 yerine a,b,c,...)
df.index = ['a', 'b', 'c', 'd', 'e']
print(df)

# Satır silme işlemi
df.drop("a", axis=0, inplace=True)  # 'a' indeksli satırı sil
print(df)

# Fancy index ile birden fazla satır silme
l = ["b", "c"]  # Silmek istediğimiz satırların indeks isimleri
df.drop(l, axis=0, inplace=True)  # 'b' ve 'c' indeksli satırları sil
print(df)

# Yeni bir sütun ekleme (var1 ile var3 sütunlarının çarpımı)
df["var4"] = df["var1"] * df["var3"]
print(df)
