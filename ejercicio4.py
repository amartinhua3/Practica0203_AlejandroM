c = int(input('Introduzca los números ganadores de la primitiva: '))
m = []
for i in range(c, 8):
    c = int(input('Introduzca los números ganadores de la primitiva: '))
m.append(c)
nums = m.sort()
print('Los números ganadores de la primitiva son: ', nums)
