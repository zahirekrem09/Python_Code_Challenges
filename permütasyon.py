def perm(arr):
    result = list([[]])
    for i in range(len(arr)):
        t = list()
        for y_lst in result:
            for j in arr:
                if j not in y_lst:
                    new_lst = list(y_lst)
                    new_lst.append(j)
                    t.append(list(new_lst))
        result = t
        print(result)
    return result
print(perm([1,2,3]))


def perm(arr,size):
    result = list([[]])
    for i in range(size):
        t = list()
        for y_lst in result:
            for j in arr:
                if j not in y_lst:
                    new_lst = list(y_lst)
                    new_lst.append(j)
                    t.append(list(new_lst))
        result = t
        #print(result)
    return result
print(perm([1,2,3,4],3))



lst=list(input("enter number array for permutation"))
n=int(input("enter times of combination"))
if len(lst)>n:
    p=[[x for x in range(0)]]
    for i in range(n):
        p = [[a] + b for a in lst for b in p if (a not in b)]
    print(p)
else:
    print("Please enter a combination number lower than list length")
    
    
    
    
x=[1,2,3]
n=len(x)
def permutate(a, l, r):
    if l==r:
        print(x)
    else:
        for i in range(l,r+1):
            a[l], a[i] = a[i], a[l]
            permutate(a, l+1, r)
            a[l], a[i] =a[i], a[l]
permutate(x, 0, n-1)