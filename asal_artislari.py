import math
import time
import statistics
from collections import Counter
from asallik_kontrolu import asal_mi

# asal sayıların artışını listeler. mesela 2 3 5 7 asal sayıları +1 +2 +2 diye gidiyor.
# artışların hep küçük sayılar olması ilginç bir şey.

while True:
    asal_listesi = []
    istenilen_sayida_asal = int(input("İstediğiniz asal sayı artışları terim sayısını giriniz: "))+1
    baslama_zamani= time.time()
    k = 2
    while len(asal_listesi) < istenilen_sayida_asal:
        if asal_mi(k):
            asal_listesi.append(k)
        k += 1
    asal_artislar = [asal_listesi[sayi]-asal_listesi[sayi-1] for sayi in range(1,len(asal_listesi))]
    print(asal_artislar)
    print(f"\n{k} tane sayı arasından {len(asal_artislar)} tane asal sayı artışını {round(time.time() - baslama_zamani,5)} saniyede ayağınıza getirdik.")
    print(f"Ortalama artış: {round(statistics.mean(asal_artislar),4)}")
    print(f"En çok tekrar eden artışlar: (sayi, tekrar sayısı) formatında")
    print(Counter(asal_artislar))

