import random

# Define a matriz de distâncias entre as cidades
distances = [
    [0, 42, 61, 30, 17, 82, 31, 11, 27],
    [42, 0, 14, 87, 28, 70, 19, 33, 13],
    [61, 14, 0, 20, 81, 21, 8, 29, 15],
    [30, 87, 20, 0, 34, 33, 91, 10, 20],
    [17, 28, 81, 34, 0, 41, 34, 82, 22],
    [82, 70, 21, 33, 41, 0, 19, 32, 27],
    [31, 19, 8, 91, 34, 19, 0, 59, 30],
    [11, 33, 29, 10, 82, 32, 59, 0, 32],
    [27, 13, 15, 20, 22, 27, 30, 32, 0]
]

# Define os nomes das cidades
city_names = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]

# Define os parâmetros do algoritmo genético
POPULATION_SIZE = 50
ELITE_SIZE = 5
MUTATION_RATE = 0.01
GENERATIONS = 1000

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
            print(f"Geração {i+1}: Solução encontrada: {best_full_route}. Distância total: {best_distance}")
        quant_gerac = i + 1
    print(f'Quantidade de gerações: {quant_gerac}')
    best_full_route = " -> ".join(city_names[i] for i in best_solution.full_route)  # Transforma os números em nomes de cidades
    print(f"Melhor solução encontrada: {best_full_route}. Melhor distância total: {best_distance}")
    
        
best_solution = genetic_algorithm()