import random
import math

def firstgeneration(length, population_size):
    population = []
    for _ in range(population_size):
        individual = [random.randint(0, 1) for _ in range(length)]
        population.append(individual)
    return population

def individualtreatment(individual):
    length = len(individual) // 2
    x = individual[:length]
    y = individual[length:]
    x, y = convertbase10(x, y)
    x = (x * 200/((2**length)-1)) - 100
    y = (y * 200/((2**length)-1)) - 100
    valor_f6 = f6(x, y)
    return valor_f6

def convertbase10(x, y):

    valor_x = 0
    valor_y = 0
    for i in range(len(x)):
        valor_x += int(x[i]) * (2 ** (len(x) - 1 - i))

    for i in range(len(y)):
        valor_y += int(y[i]) * (2 ** (len(y) - 1 - i))

    return valor_x, valor_y


def f6(x, y):
    result = 0.5 - ((math.sin(math.sqrt(x**2 + y**2)) ** 2) - 0.5) / ((1.0 + 0.001 * (x**2 + y**2)) ** 2)

    return result