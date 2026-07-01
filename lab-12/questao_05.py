import random
import time
voltas = random.randint(0,10)
cont = 1
for i in range(1,voltas):
    print(f'Volta {cont}: Mais uma volta')
    cont += 1
    time.sleep(1)
print('Acabou')