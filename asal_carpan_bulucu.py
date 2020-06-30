from asal_listesi import asallar
import math

# not: programa girilebilecek en büyük sayı 1299710'dur.

#stringdeki rakamları superscripte çeviren fonksiyon
def usleyici(uslencek_sayi):
    superscript_sozluk = {
        "0":"⁰",
        "1":"¹",
        "2":"²",
        "3":"³",
        "4":"⁴",
        "5":"⁵",
        "6":"⁶",
        "7":"⁷",
        "8":"⁸",
        "9":"⁹"
    }
    uslencek_sayi_liste = list(str(uslencek_sayi))
    for rakam in uslencek_sayi_liste:
        #denesene direk rakam = diyemiyoz mu
        uslencek_sayi_liste[uslencek_sayi_liste.index(rakam)] = superscript_sozluk[rakam]
    return "".join(uslencek_sayi_liste)


#asal çarpan listeleyici fonksiyon
def crpn_bulucu(sayix):
    carpan_listesi = []
    #ussuz_carpanlar = []
    en_son_carpan_listesi = ""
    #aşağıda ki şeyle tüm asalları taramasını engelledim ama yine de fazladan asalı tarıyor
    for item in asallar[:(sayix+3)]:
        if sayix % item == 0 and item not in carpan_listesi:
            carpan_listesi.append(item)
    ussuz_carpanlar = carpan_listesi.copy()
    #iki liste olacak buradan sonra

    for asal in carpan_listesi:
        us = 1
        while sayix % asal**us == 0:
            us += 1
        else:
            carpan_listesi[carpan_listesi.index(asal)]= asal ** (us-1)
            #listeden item böyle değiştiriliyormuş liste[x]=bişey

    for asaltamkare in carpan_listesi:
        asalkoku = ussuz_carpanlar[carpan_listesi.index(asaltamkare)]
        asalussu = math.log(asaltamkare,asalkoku)
        if asalussu != 1:
            en_son_carpan_listesi += f"{asalkoku}{usleyici(int(asalussu))}x"
            #en_son_carpan_listesi += f"({asalkoku}^{int(asalussu)})x"
        elif asalussu == 1:
            en_son_carpan_listesi += f"{asalkoku}x"

#[:-1 var çünkü bir tane x fazladan geliyor.
    return en_son_carpan_listesi[:-1]

if __name__ == "__main__":
    while True:
        try:
            while True:
                inputumuz=int(input("Asal çarpanları bulunacak sayıyı giriniz (azami 1299710): "))
                print(crpn_bulucu(inputumuz))
        except ValueError:
            print("Lütfen tam sayı giriniz.")
