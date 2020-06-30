def bolen_bul(sayi):
    i = 1
    bolenler = ""
    while i <= sayi:
        if sayi % i == 0:
            bolenler += f"{i} "
        i += 1
    return bolenler


if __name__ == "__main__":
    while True:
        try:
            print(bolen_bul(int(input("Bölenlerine bakılacak sayıyı giriniz: "))))
        except ValueError:
            print("Geçersiz değer. Tam sayı giriniz.\n")