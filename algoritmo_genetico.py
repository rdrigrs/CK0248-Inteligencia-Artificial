import random
import numpy as np

# distâncias entre as cidades
# coluna é cidade de origem e linha é cidade de destino
d = [
    [0, 10, 15, 45, 5, 45, 50, 44, 30, 100, 67, 33, 90, 17, 50],
    [15, 0, 100, 30, 20, 25, 80, 45, 41, 5, 45, 10, 90, 10, 35],
    [40, 80, 0, 90, 70, 33, 100, 70, 30, 23, 80, 60, 47, 33, 25],
    [100, 8, 5, 0, 5, 40, 21, 20, 35, 14, 55, 35, 21, 5, 40],
    [17, 10, 33, 45, 0, 14, 50, 27, 33, 60, 17, 10, 20, 13, 71],
    [15, 70, 90, 20, 11, 0, 15, 35, 30, 15, 18, 35, 15, 90, 23],
    [25, 19, 18, 30, 100, 55, 0, 70, 55, 41, 55, 100, 18, 14, 18],
    [40, 15, 60, 45, 70, 33, 25, 0, 27, 60, 80, 35, 30, 41, 35],
    [21, 34, 17, 10, 11, 40, 8, 32, 0, 47, 76, 40, 21, 90, 21],
    [35, 100, 5, 18, 43, 25, 14, 30, 39, 0, 17, 35, 15, 13, 40],
    [38, 20, 23, 30, 5, 55, 50, 33, 70, 14, 0, 60, 30, 35, 21],
    [15, 14, 45, 21, 100, 10, 8, 20, 35, 43, 8, 0, 15, 100, 23],
    [80, 10, 5, 20, 35, 8, 90, 5, 44, 10, 80, 14, 0, 25, 80],
    [33, 90, 40, 18, 70, 45, 25, 23, 90, 44, 43, 70, 5, 0, 25],
    [25, 70, 45, 50, 5, 45, 20, 100, 25, 50, 35, 10, 90, 5, 0]
]


def calcula_distancia(caminho):
    distancia = 0
    for i in range(len(caminho) - 1):
        distancia += d[caminho[i]][caminho[i + 1]]
    distancia += d[caminho[-1]][caminho[0]]
    return distancia


# Algortimo Genético:
def fitness(indivual, chromosomes_size):
    metrica = 0
    caminho = 0
    for i in range(chromosomes_size - 1):
        caminho += d[indivual[i]][indivual[i + 1]]
    caminho += d[indivual[chromosomes_size - 1]][indivual[0]]
    metrica = 1 / caminho
    return metrica


def crossover(individual_1, individual_2, chromosomes_size):
    kid = list()
    for i in range(chromosomes_size):
        kid.append(-1)

    for i in range(chromosomes_size):
        if individual_1[i] == individual_2[i]:
            kid[i] = individual_1[i]

    for i in range(chromosomes_size):
        if kid[i] == -1:
            if i % 2 == 0:
                for j in range(chromosomes_size):
                    if individual_1[j] not in kid:
                        kid[i] = individual_1[j]
                        break
            else:
                for j in range(chromosomes_size):
                    if individual_2[j] not in kid:
                        kid[i] = individual_2[j]
                        break
    return kid


def mutation(ind, crom_size):
    i = random.randint(0, crom_size - 1)
    j = random.randint(0, crom_size - 1)
    ind[i], ind[j] = ind[j], ind[i]
    return ind


def next_generation(population, pop_size, chromosomes_size, mutation_rate):
    for i in range(int(pop_size / 2)):
        population.pop()

    for i in range(int(pop_size / 2)):
        ind1 = random.choice(population)
        ind2 = random.choice(population)
        kid = crossover(ind1, ind2, chromosomes_size)

        if random.random() < mutation_rate:
            kid = mutation(kid, chromosomes_size)

        population.append(kid)

    population.sort(key=lambda x: fitness(x, chromosomes_size), reverse=True)
    return population


def genetic_algorithm(pop_size, chromosomes_size, generations, mutation_rate):
    population = list()
    for i in range(pop_size):
        ind = list(range(chromosomes_size))
        random.shuffle(ind)
        population.append(ind)

    for g in range(generations):
        population = next_generation(population, pop_size, chromosomes_size, mutation_rate)
    return population


def analytics_genetic_algorithm(pop_size, chromosomes_size, generations, mutation_rate):
    population = list()
    for i in range(pop_size):
        ind = list(range(chromosomes_size))
        random.shuffle(ind)
        population.append(ind)

    for g in range(generations):
        population = next_generation(population, pop_size, chromosomes_size, mutation_rate)
        print("Geração: ", g)
        print("Melhor indivíduo: ", population[0])
        print("Fitness: ", fitness(population[0], chromosomes_size))
        print("Distância: ", calcula_distancia(population[0]))
        print("===========================================")
    return population