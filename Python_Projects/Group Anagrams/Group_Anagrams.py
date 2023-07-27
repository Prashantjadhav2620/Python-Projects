



from collections import defaultdict

def Group_Anagrams(a):
    d = defaultdict(list)
    for i in a:
        sorted_i = " ".join(sorted(i))
        d[sorted_i].append(i)
    return d.values()



words = ["tea", "eat", "bat", "ate", "arc", "car"]

print(Group_Anagrams(words))

# Output :- dict_values([['tea', 'eat', 'ate'], ['bat'], ['arc', 'car']])