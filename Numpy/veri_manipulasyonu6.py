from random import random

import numpy as np

# İndex ile elemanlar erişme

# Random bir vektör oluşturma
a = np.random.randint(10,size=10)
# vekötrü yazdırma işlemi
print(a)
# İlk elemana erişme (indexler 0'dan başlar)
print(a[0])
# Sonuncu elemana erişme
print(a[-1])
# Erişilen elemanı değiştirme
a[0] = 1

# Random bir matris oluşturma
b = np.random.randint(10,size=(3,5))
# Matrisi yazdırma
print(b)
# 0. satırın 0. sütununda ki elemana erişme
print(b[0,0])
#Elemanı değiştirme
b[0,0] = 100

