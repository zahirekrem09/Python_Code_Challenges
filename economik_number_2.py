import math
import time
def asal_mi(sayi):
    if sayi >= 2:
        i = 2
        while i <= math.sqrt(sayi):
            if sayi % i == 0:
                return False
            i += 1
        else:
            return True
    else:
        return False
def is_economical(sayi):
    # sayi=150528
    b = time.time()
    asal_listesi = [i for i in range(2, sayi + 1) if asal_mi(i) and not sayi % i]
    ussuz_carpanlar = asal_listesi.copy()
    # [2, 3, 7]
    for asal in asal_listesi:
        us = 1
        while sayi % asal ** us == 0:
            us += 1
        else:
            asal_listesi[asal_listesi.index(asal)] = asal ** (us - 1)
    # [1024, 3, 49]

    count = len("".join(map(str, ussuz_carpanlar)))
    # "237"
    for i, k in list(zip(ussuz_carpanlar, asal_listesi)):
        bas_say = int(math.log(k, i))
        if (bas_say) != 1:
            count += len(str(bas_say))
    if int(count) == len(str(sayi)):
        return f"Equadigital {count}   {round(time.time() - b, 5)} saniyede  getirdik."
    elif int(count) <= len(str(sayi)):
        return f"Frugal {count}  {round(time.time() - b, 5)} saniyede  getirdik."
    else:
        return f"Wasteful {count}  {round(time.time() - b, 5)} saniyede  getirdik."


print(is_economical(150528))
