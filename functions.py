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


def evaluatepopulation(population, elite_amount):
    F6score = []

    for individual in population:
        value = individualtreatment(individual)
        F6score.append(value)

    elites = []
    used_indexes = []

    if elite_amount > len(population):
        elite_amount = len(population)

    for _ in range(elite_amount):
        best_index = 0
        best_score = -1

        for i in range(len(population)):
            if i not in used_indexes:
                if F6score[i] > best_score:
                    best_score = F6score[i]
                    best_index = i

        used_indexes.append(best_index)
        elites.append(population[best_index][:])

    return F6score, elites

def crossover(parent1, parent2, crossover_rate):
    if random.random() <= crossover_rate:
        crossover_point = random.randint(1, len(parent1) - 1)

        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]

        return child1, child2

    return None, None

def mutation(individual, mutation_rate):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = 1 - individual[i]
    return individual

def rouletteselection(population, F6score):
    selected_population = []
    total_F6score = sum(F6score)

    for _ in range(len(population)):
        random_value = random.uniform(0, total_F6score)

        current_sum = 0

        for i in range(len(population)):
            current_sum += F6score[i]

            if current_sum >= random_value:
                selected_population.append(population[i])
                break

    return selected_population