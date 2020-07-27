def anagram(lst:list):
    anagram_lst = list(set([[j for j in lst if set(i) == set(j) and len(i)==len(j)] for i in lst ]))
    for i in lst:
        add_list= [j for j in lst if set(i) == set(j) and len(i)==len(j)]
        if not add_list in anagram_lst:
            anagram_lst.append(add_list)
    return anagram_lst

anagram(["eat","tea","tan","ate","nat","bat","eate"])




a=["eat", "tea", "tan", "ate", "nat", "bat"]
b={}
for i in a:
    x="".join(sorted(i))
    if x not in b.keys():
        b[x]=[]
    b[x].append(i)
print(list(b.values())) 