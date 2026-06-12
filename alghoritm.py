import random
from functions import firstgeneration, crossover, mutation, evaluatepopulation, rouletteselection

def geneticalgorithm(length, population_size, max_generations, mutation_rate, elite_amount, crossover_rate):
    t = 0

    population = firstgeneration(length, population_size)

    F6score, elites = evaluatepopulation(population, elite_amount)

    while t < max_generations:
        t += 1

        selected_population = rouletteselection(population, F6score)

        new_population = []

        while len(new_population) < population_size:
            child1 = None
            child2 = None

            while child1 == None or child2 == None:
                index1 = random.randint(0, len(selected_population) - 1)
                index2 = random.randint(0, len(selected_population) - 1)

                while index2 == index1:
                    index2 = random.randint(0, len(selected_population) - 1)

                parent1 = selected_population[index1]
                parent2 = selected_population[index2]

                child1, child2 = crossover(parent1, parent2, crossover_rate)

            child1 = mutation(child1, mutation_rate)
            child2 = mutation(child2, mutation_rate)

            new_population.append(child1)

            if len(new_population) < population_size:
                new_population.append(child2)

        replaced_indexes = []

        for elite in elites:
            random_index = random.randint(0, len(new_population) - 1)

            while random_index in replaced_indexes:
                random_index = random.randint(0, len(new_population) - 1)

            new_population[random_index] = elite[:]
            replaced_indexes.append(random_index)

        population = new_population

        F6score, elites = evaluatepopulation(population, elite_amount)

    return population, F6score