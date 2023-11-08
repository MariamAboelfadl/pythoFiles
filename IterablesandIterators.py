from itertools import combinations
n=input()
data=input().split()
ocur = []
combs=list(combinations(data,int(input())))
for i in combs:
    if "a" in i:
        ocur.append(i)
print(len(ocur)/len(combs))