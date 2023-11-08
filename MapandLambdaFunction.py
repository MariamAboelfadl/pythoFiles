cube = lambda x: x**3

def fibonacci(n):
    l=[]
    a, b = 0, 1
    for i in range(n):
        l.append(a)
        a, b = b, a+b
    
    return l

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))