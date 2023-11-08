from itertools import product
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    li = []
    X = list(range(x+1))
    Y = list(range(y+1))
    Z = list(range(z+1))
    result = list(sorted(set(product(X,Y,Z))))
    print(list(map(list,list(filter(lambda x: sum(x)!=n,result)))))