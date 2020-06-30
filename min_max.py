def min_r(liste):
    if len(liste) == 1:
        return liste[0]
    else:
        if liste[0] < liste[1]:
            return min_r([liste[0]] + liste[2:])
        else:
            return min_r([liste[1]] + liste[2:])


def max_r(liste):
    if len(liste) == 1:
        return liste[0]
    else:
        if liste[0] > liste[1]:
            return max_r([liste[0]] + liste[2:])
        else:
            return max_r([liste[1]] + liste[2:])

# print min_r([1,1,2,1231,-123,-431241234,-1213,123123])
# print max_r([1,1,2,1231,-123,-431241234,-1213,123123])