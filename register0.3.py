
import math

print ("Эта прога решает квадратные уровнения")
exemple_a = int(input('Введите коофицыент a - '))
exemple_b = int(input('Введите коофицыент b - '))
exemple_c = int(input('Введите коофицыент c - '))
D = exemple_b * exemple_b - 4 * exemple_a * exemple_c
print(f"Дискреминант(D) = {D}")
if D > 0:
    x1 = ((exemple_b * -1) + math.sqrt(D)) / (2 * exemple_a)
    x2 = ((exemple_b * -1) - math.sqrt(D)) / (2 * exemple_a)
    print(f'x1 = {x1}')
    print(f'x2 = {x2}')
elif D == 0:
    x3 = (exemple_b * -1) / (2 * exemple_a)
    print(f'x3 = {x3}')
elif D < 0:
    print("Нет корней")
else:
    print("Error")





