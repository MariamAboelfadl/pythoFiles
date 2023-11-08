d={}
for i in range(int(input())):
    c = input()
    if c in d: 
        d[c]+=1
    else: 
        d[c]=1
print(len(d))
for i in d: 
    print(d[i], end = " ")