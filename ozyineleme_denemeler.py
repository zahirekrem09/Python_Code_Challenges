def arasi(n, m, adim):
    if n >= m:
        return []
    else:
        return [n] + arasi(n+adim, m, adim)
#print(arasi(0,10,3))


def cift_indeksler(liste):
    if liste == []:
        return []
    elif len(liste) % 2 != 0:
        return cift_indeksler(liste[:-1]) + [liste[-1]]
    else:
        return cift_indeksler(liste[:-1])
# print(cift_indeksler([0,1,2,3,4,5,6,7]))
# print(cift_indeksler([0,1,2,3,4,5,6]))


def map_ozyineli(fonksiyon, liste):
    if liste == []:
        return []
    else:
        return [fonksiyon(liste[0])] + map_ozyineli(fonksiyon, liste[1:])
# print(map_ozyineli(lambda x: x**4, [1,2,3,4,5]))


def n_inci_fibonacci_verimsiz(n):
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    else:
        return n_inci_fibonacci_verimsiz(n-1) + n_inci_fibonacci_verimsiz(n-2)
# for item in range(10):
#    print n_inci_fibonacci_verimsiz(item)
# bu kod verimsiz cunku zaten tekrarlamis oldugu degerleri tekrar tekrar hesapliyor.


def n_inci_fibonacci_verimli(n, onceki=1, suAnki=1):
    if n == 0:
        return 0
    elif n <= 1:
        return onceki
    else:
        return n_inci_fibonacci_verimli(n-1, suAnki, onceki+suAnki)
# for item in range(10):
#    print n_inci_fibonacci_verimli(item)


def fibseries(n, onceki=0, simdiki=1):
    if n <= 1:
        return [onceki]
    else:
        return [onceki] + fibseries(n-1, simdiki, onceki+simdiki)
#print fibseries(15)

def liste_elmn_ters_dondur_ozyineli(liste):
    if liste == []:
        return []
    else:
        if type(liste[-1]) == list:
            return ([liste_elmn_ters_dondur_ozyineli(liste[-1])]
                   + liste_elmn_ters_dondur_ozyineli(liste[:-1]))
        else:
            return [liste[-1]] + liste_elmn_ters_dondur_ozyineli(liste[:-1])
# print(liste_elmn_ters_dondur_ozyineli([1,2,[3,4,5,6,[7,8]],11,12,[13],[14]]))


def sum_ozyineli(liste):
    if liste == []:
        return 0
    else:
        if type(liste[0]) != list:
            return liste[0] + sum_ozyineli(liste[1:])
        else:
            return sum_ozyineli(liste[0]) + sum_ozyineli(liste[1:])
# print(sum_ozyineli([1,1,[1,1,[1,1,[1,1,[1,1,[1,1,[1,1]]]]]]]))


def count_r(element, liste):
    if len(liste) == 0:
        return 0
    elif liste[0] == element:
        return 1 + count_r(element, liste[1:])
    elif liste[0] != element:
        return 0 + count_r(element, liste[1:])
#print count_r('1', [1,2,3,4,5,'1',1,'1'])


def filter_r(func, liste):
    if len(liste) == 0:
        return []
    elif func(liste[0]):
        return [liste[0]] + filter_r(func, liste[1:])
    else:
        return filter_r(func, liste[1:])


def remove_all(element, liste):
    if len(liste) == 0:
        return []
    elif liste[0] == element:
        return remove_all(element, liste[1:])
    else:
        return [liste[0]] + remove_all(element, liste[1:])


# bir listede eger her sayi bir onceki sayinin karesiyse True doner, guzel bu bak
def progressive_square(liste):
    if len(liste) == 1:
        return True
    elif liste[1] != liste[0] ** 2:
        return False
    elif liste[1] == liste[0] ** 2:
        if len(liste) == 2:
            return True
        else:
            return progressive_square(liste[1:])


# python slice operatorunun yaptigi seyi yapiyo mesela
# >>> slice([1,2,3,4], -1, 0, -1)
# [4, 3, 2]
# https://nihil.ceng.metu.edu.tr/opc/pcourse/4/11/
def slice_r(liste, start, end, step):
    length = len(liste)
    if start > length: start = length
    if end > length: end = length
    if start < -length:
        start = 0
    if end == -length:
        end = 0
    if start < 0: start += length
    if end < -length:
        #buradaki amacim [1, 2, 3, 4, 5][-1:-100:-1] diyince mesela ilk elemani da alabilmek
        end = 0
        liste = [0] + liste
        start += 1
    if end < 0: end += length

    if step > 0:
        if start >= end:
            return []
        else:
            return [liste[start]] + slice_r(liste, start+step, end, step)
    else:
        if start <= end:
            return []
        else:
            return [liste[start]] + slice_r(liste, start+step, end, step)
#print slice_r([0,1,2,3,4,5,6,7,8,9], 8, 1, -1)
#print [0,1,2,3,4,5,6,7,8,9][8:1:-1]


# is_substring('ssip', 'mississippi')
# True
def is_substring(sub, string):
    # return sub in string
    if len(sub) >= len(string):
        return True if sub == string else False
    else:
        if sub == string[:len(sub)]:
            return True
        else:
            return is_substring(sub, string[1:])


# >>> substrings('ceng')
# [c', 'ce', 'cen', 'ceng', 'e', 'en', 'eng', 'n', 'ng', 'g']
def bastan_sona(string):
    if len(string) == 0:
        return []
    else:
        return bastan_sona(string[:-1]) + [string]

def substrings(string):
    if len(string) == 0:
        return []
    else:
        return bastan_sona(string) + substrings(string[1:])
#print substrings("ceng")

#https://nihil.ceng.metu.edu.tr/opc/pcourse/4/8/
def letter_pairs(string):
    if len(string) == 1:
        return []
    else:
        return [string[0] + string[1]] + letter_pairs(string[1:])