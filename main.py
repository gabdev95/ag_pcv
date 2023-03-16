import random

# Define a matriz de distâncias entre as cidades
distances = [
    [0, 107, 241, 190, 124, 80, 316, 76, 152, 157, 283, 133, 113, 297, 228, 129, 348, 276, 188, 150, 65, 341, 184, 67, 221, 169],
    [107, 0, 148, 137, 88, 127, 336, 183, 134, 95, 254, 180, 101, 234, 175, 176, 265, 199, 182, 67, 42, 278, 271, 146, 251, 105],
    [241, 148, 0, 374, 171, 259, 509, 317, 217, 232, 491, 312, 280, 391, 412, 349, 422, 356, 355, 204, 182, 435, 417, 292, 424, 116],
    [190, 137, 374, 0, 202, 234, 222, 192, 248, 42, 117, 287, 79, 107, 38, 121, 152, 86, 68, 70, 137, 151, 239, 135, 137, 242],
    [124, 88, 171, 202, 0, 61, 392, 202, 46, 160, 319, 112, 163, 322, 240, 232, 314, 287, 238, 155, 65, 366, 300, 175, 307, 57],
    [80, 127, 259, 234, 61, 0, 386, 141, 72, 167, 351, 55, 157, 331, 272, 226, 362, 296, 232, 164, 85, 375, 249, 147, 301, 118],
    [316, 336, 509, 222, 392, 386, 0, 233, 438, 254, 202, 439, 235, 254, 210, 187, 313, 266, 154, 282, 321, 298, 168, 249, 95, 437],
    [76, 183, 317, 192, 202, 141, 233, 0, 213, 188, 272, 193, 131, 302, 233, 98, 344, 289, 177, 216, 141, 346, 108, 57, 190, 245],
    [152, 134, 217, 248, 46, 72, 438, 213, 0, 206, 365, 89, 209, 368, 286, 278, 360, 333, 284, 201, 111, 412, 321, 221, 353, 72],
    [157, 95, 232, 42, 160, 167, 254, 188, 206, 0, 159, 220, 57, 149, 80, 132, 193, 127, 100, 28, 95, 193, 241, 131, 169, 200],
    [283, 254, 491, 117, 319, 351, 202, 272, 365, 159, 0, 404, 176, 106, 79, 161, 165, 141, 95, 187, 254, 103, 279, 215, 117, 359],
    [133, 180, 312, 287, 112, 55, 439, 193, 89, 220, 404, 0, 210, 384, 325, 279, 415, 349, 285, 217, 138, 428, 310, 200, 354, 169],
    [113, 101, 280, 79, 163, 157, 235, 131, 209, 57, 176, 210, 0, 186, 117, 75, 231, 165, 81, 85, 92, 230, 184, 74, 150, 208],
    [297, 234, 391, 107, 322, 331, 254, 302, 368, 149, 106, 384, 186, 0, 69, 191, 59, 35, 125, 167, 255, 44, 309, 245, 169, 327],
    [228, 175, 412, 38, 240, 272, 210, 233, 286, 80, 79, 325, 117, 69, 0, 122, 122, 56, 56, 108, 175, 113, 240, 176, 125, 280],
    [129, 176, 349, 121, 232, 226, 187, 98, 278, 132, 161, 279, 75, 191, 122, 0, 244, 178, 66, 160, 161, 235, 118, 62, 92, 277],
    [348, 265, 422, 152, 314, 362, 313, 344, 360, 193, 165, 415, 231, 59, 122, 244, 0, 66, 178, 198, 286, 77, 362, 287, 228, 358],
    [276, 199, 356, 86, 287, 296, 266, 289, 333, 127, 141, 349, 165, 35, 56, 178, 66, 0, 112, 132, 220, 79, 296, 232, 181, 292],
    [188, 182, 355, 68, 238, 232, 154, 177, 284, 100, 95, 285, 81, 125, 56, 66, 178, 112, 0, 128, 167, 169, 179, 120, 69, 283],
    [150, 67, 204, 70, 155, 164, 282, 216, 201, 28, 187, 217, 85, 167, 108, 160, 198, 132, 128, 0, 88, 211, 269, 159, 197, 172],
    [65, 42, 182, 137, 65, 85, 321, 141, 111, 95, 254, 138, 92, 255, 175, 161, 286, 220, 167, 88, 0, 299, 229, 104, 236, 110],
    [341, 278, 435, 151, 366, 375, 298, 346, 412, 193, 103, 428, 230, 44, 113, 235, 77, 79, 169, 211, 299, 0, 353, 289, 213, 371],
    [184, 271, 417, 239, 300, 249, 168, 108, 321, 241, 279, 310, 184, 309, 240, 118, 362, 296, 179, 269, 229, 353, 0, 121, 162, 345],
    [67, 146, 292, 135, 175, 147, 249, 57, 221, 131, 215, 200, 74, 245, 176, 62, 287, 232, 120, 159, 104, 289, 121, 0, 154, 220],
    [221, 251, 424, 137, 307, 301, 95, 190, 353, 169, 117, 354, 150, 169, 125, 92, 228, 181, 69, 197, 236, 213, 162, 154, 0, 352],
    [169, 105, 116, 242, 57, 118, 437, 245, 72, 200, 359, 169, 208, 327, 280, 277, 358, 292, 283, 172, 110, 371, 345, 220, 352, 0],
]

# Define os nomes das cidades
city_names = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# Define os parâmetros do algoritmo genético
POPULATION_SIZE = 15
ELITE_SIZE = 5
MUTATION_RATE = 0.01
GENERATIONS = 3500

# Define a classe para representar uma solução (ou indivíduo) do problema
class Solution:
    def __init__(self, cities):
        self.cities = cities
        self.full_route = cities + [cities[0]]  # Adiciona a primeira cidade no final
        self.distance = self.calculate_distance()
        
    def calculate_distance(self):
        distance = 0
        for i in range(len(self.full_route) - 1):
            distance += distances[self.full_route[i]][self.full_route[i+1]]
        return distance

# Define as funções para criar e evoluir a população
def create_population():
    population = []
    for i in range(POPULATION_SIZE):
        cities = list(range(len(distances)))
        random.shuffle(cities)
        solution = Solution(cities)
        population.append(solution)
    return population

def rank_population(population):
    ranked_population = sorted(population, key=lambda solution: solution.distance)
    return ranked_population

def select_parents(population):
    parents = random.sample(population, 2)
    return parents

def crossover(parent1, parent2):
    child_cities = [None] * len(parent1.cities)
    start = random.randint(0, len(parent1.cities) - 1)
    end = random.randint(start, len(parent1.cities) - 1)
    for i in range(start, end + 1):
        child_cities[i] = parent1.cities[i]
    for city in parent2.cities:
        if city not in child_cities:
            for i in range(len(child_cities)):
                if child_cities[i] is None:
                    child_cities[i] = city
                    break
    child = Solution(child_cities)
    return child

def mutate(solution):
    if random.random() < MUTATION_RATE:
        i = random.randint(0, len(solution.cities) - 1)
        j = random.randint(0, len(solution.cities) - 1)
        solution.cities[i], solution.cities[j] = solution.cities[j], solution.cities[i]
        solution.distance = solution.calculate_distance()

def evolve_population(population):
    elite = population[:ELITE_SIZE]
    offspring = []
    while len(offspring) < POPULATION_SIZE - ELITE_SIZE:
        parent1 = select_parents(population)
        parent2 = select_parents(population)
        child = crossover(parent1[0], parent2[0])
        mutate(child)
        offspring.append(child)
    population = elite + offspring
    return population

# Define a função principal do algoritmo
def genetic_algorithm():
    population = create_population()
    best_solution = None
    for i in range(GENERATIONS):
        population = create_population()
    best_solution = None
    best_distance = float("inf")
    for i in range(GENERATIONS):
        population = evolve_population(population)
        population = rank_population(population)
        if population[0].distance < best_distance:
            best_solution = population[0]
            best_distance = population[0].distance
            best_full_route = " -> ".join(city_names[i] for i in best_solution.full_route)  # Transforma os números em nomes de cidades
            print(f"Iteração {i+1} - Aptidão: {best_distance}km \nPercurso: {best_full_route}\n ")
    best_full_route = " -> ".join(city_names[i] for i in best_solution.full_route)  # Transforma os números em nomes de cidades
    print('=' * 141)
    print('MELHOR SOLUÇÃO ENCONTRADA'.center(141))
    print('=' * 141)
    print(f"Distância total a ser percorrida: {best_distance}km \nPercurso: {best_full_route}\n")
    
        
best_solution = genetic_algorithm()