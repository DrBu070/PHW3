print('HomeWork5')
k = int(input('Введите число: '))
def NumFib(k):
    n = []
    a, b = 1, 1
    for i in range(k):
        n.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (k+1):
        n.insert(0, a)
        a, b = b, a - b
    return n

n = NumFib(k)
print(NumFib(k))
print(n.index(0))