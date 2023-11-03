a = ['Matemáticas', 'Historia', 'Lengua', 'Química', 'Física']
notas = []

for i in range(a):
    n = int(input('Introduce la nota de cada asignatura: '))
while n > 10 or n < 0:
    n = int(input('Introduce la nota de cada asignatura: '))
notas.append(n)

print('En', i, 'has sacado', n)