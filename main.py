from functions import convertbase10, f6
from alghoritm import geneticalgorithm

elite_amount = 2
population_size = 100
length = 44
max_generations = 40
mutation_rate = 0.008
crossover_rate = 0.65
total_individuals = population_size * max_generations
final_population, final_scores = geneticalgorithm(length, population_size, max_generations, mutation_rate, elite_amount, crossover_rate)
best_individual = final_population[final_scores.index(max(final_scores))]
best_x, best_y = convertbase10(best_individual[:length//2], best_individual[length//2:])
best_x = (best_x * 200/((2**(length//2))-1)) - 100
best_y = (best_y * 200/((2**(length//2))-1)) - 100
best_score = f6(best_x, best_y)

print(f"Total Individuals Evaluated: {total_individuals}")
print(f"Best Individual: {best_individual}")
print(f"Best x: {best_x}, Best y: {best_y}")
print(f"Best F6 Score: {best_score}")