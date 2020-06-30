"""
Input : A = [1, 2, 3, 4, 5]
Output : [    48]
         [  20,28] 
         [ 8, 12,16] 
         [3, 5, 7, 9] 
       [1,  2, 3,4, 5] 
"""
def t(taban):
    if len(taban) == 1:
        return []
    else:
        return [taban[0] + taban[1]] + t(taban[1:])

def t_ucgeni(taban):
    if len(taban) == 1:
        return [taban]
    else:
        return t_ucgeni(t(taban)) + [taban]

print "\n".join(map(str,t_ucgeni([1, 2, 3, 4, 5])))