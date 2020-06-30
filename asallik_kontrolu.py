import math
def asal_mi(sayi):
    if sayi >= 2:
        i=2
        while i <= math.sqrt(sayi):
            if sayi % i == 0:
                return False
            i += 1
        else:
            return True
    else:
        return False
