def eleman_ekleyici(eleman, liste_listesi): # liste icindeki her listeye elemani ekler
    if liste_listesi == []:
        return []
    else:
        return [liste_listesi[0] + [eleman]] + eleman_ekleyici(eleman, liste_listesi[1:])
# print(eleman_ekleyici("1234", [[1],[2],[3,4,5]]))


def altKumeler(liste):
    if len(liste) == 0:
        return [[]]
    else:
        return altKumeler(liste[:-1]) + eleman_ekleyici(liste[-1], altKumeler(liste[:-1]))
# print(sorted(altKumeler(["a","b","c"]), key=lambda x: -len(x)))