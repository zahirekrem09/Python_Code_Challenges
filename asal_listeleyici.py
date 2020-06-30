import math
import time
from asallik_kontrolu import asal_mi



while True:
    asal_listesi = []
    istenilen_sayida_asal = int(input("İstediğiniz asal sayı miktarını giriniz: "))
    baslama_zamani= time.time()
    k = 2
    while len(asal_listesi) < istenilen_sayida_asal:
        if asal_mi(k):
            asal_listesi.append(k)
        k += 1
    print(asal_listesi)
    print(f"\n{k} tane sayı arasından {len(asal_listesi)} tane asal sayıyı "
          f"{round(time.time() - baslama_zamani,5)} saniyede ayağınıza getirdik."
          f"\nAsallık yüzdesi: %{100*len(asal_listesi)/k}")
    cikti_istegi = input("Listeyi txt dosyasına çıkartmak için evet yaziniz. "
                         "Başka bir liste oluşturmak için hayır yaziniz: ")
    if cikti_istegi == "evet":
        File_object = open(r"asal_listesi.txt","w")
        File_object.write(str(asal_listesi))
        File_object.close()
