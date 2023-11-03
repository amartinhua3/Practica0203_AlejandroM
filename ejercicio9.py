p = [input('Escriba una palabra: ')]
v = ['a', 'e', 'i', 'o', 'u']
b = len(p)
x = 0
for i in range(p):
    if p[i] == v:
        x = x + 1
        print('La vocal', v, 'se repite', x, 'veces en la palabra que ha escrito')
