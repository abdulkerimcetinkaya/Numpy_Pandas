import pandas as pd
from pandas import Series

# Seri (Series) oluşturma işlemi

# Basit bir Seri oluşturma
a = pd.Series([1, 2, 3, 4, 5])
print(a)  # Seriyi ekrana yazdırma

# Serinin veri tipi
print(a.dtypes)  # Serideki verilerin tipi (int64 gibi)

# Serinin eksen bilgisi (index bilgisi)
print(a.axes)  # Serinin sahip olduğu eksenler (indexler)

# Serinin boyutu
print(a.ndim)  # Serinin kaç boyutlu olduğu (genelde 1'dir çünkü bir seri tek boyutludur)

# Serideki toplam eleman sayısı
print(a.size)  # Serinin toplam eleman sayısı

# Serideki değerler
print(a.values)  # Serinin değerlerini bir array (numpy) olarak döndürür

# İlk 3 elemanı gösterme
print(a.head(3))  # Serinin ilk 3 elemanını gösterir

# Son 3 elemanı gösterme
print(a.tail(3))  # Serinin son 3 elemanını gösterir

# ---------------------------------------

# İndex isimlendirme ile Seri oluşturma

b = Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
print(b)  # İndexleri ile birlikte seriyi yazdırma

# Belirli bir indexteki elemanı alma
print(b["a"])  # 'a' indexindeki değeri gösterme

# ---------------------------------------

# Sözlükten Seri oluşturma

# Bir sözlüğü Seri'ye dönüştürme
sozluk = pd.Series({"Reg": 10, "Log": 20, "Cart": 12})
print(sozluk)  # Sözlükten oluşturulan seriyi yazdırma
