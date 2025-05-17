import random
import sys
import os

os.system('clear')
jugadas = ['piedra', 'papel', 'tijera']

computador = random.choice(jugadas)

usuario = (sys.argv[1])

if usuario not in jugadas or len(sys.argv) > 2:
    print('Argumento inválido: Debe ser piedra, papel o tijera.\n')
    exit()

elif usuario == computador:
    print(f'Tu jugaste {usuario}\nComputador jugó {computador}\nHa sido un empate\n')
    exit()

elif usuario == 'piedra' and computador == 'tijera' or usuario == 'papel' and computador == 'piedra' or usuario == 'tijera' and computador == 'papel':
    print(f'Tu jugaste {usuario}\nComputador jugó {computador}\nFelicidades, has ganado!!!\n')
    exit()
else:
    print(f'Tu jugaste {usuario}\nComputador jugó {computador}\nHas perdido, mejor suerte la próxima\n')
    exit()
