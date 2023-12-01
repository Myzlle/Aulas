'''co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto Adjacente:'))
hi = (co ** 2 + ca ** 2) ** (1/2)
print (' A hipotenusa vai medir {:.2f}'.format(hi))'''

import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto Adjacente:'))
hi = math.hypot(co, ca)
print('O valor da hiptonesua vai medir: {:.2f}'.format(hi))
