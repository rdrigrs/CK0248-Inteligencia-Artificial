import random
import numpy as np

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

def calcula_probabilidade(feromonio, visibilidade, alpha, beta):
    probabilidade = np.multiply(np.power(feromonio, alpha), np.power(visibilidade, beta))
    probabilidade_sum = np.sum(probabilidade)
    if probabilidade_sum == 0:
        probabilidade = np.zeros_like(probabilidade)
    else:
        probabilidade = np.divide(probabilidade, probabilidade_sum)
    return probabilidade

def atualiza_feromonio(feromonio, caminhos, custos, evap_rate):
    for i in range(len(feromonio)):
        for j in range(len(feromonio[i])):
            feromonio[i][j] = (1 - evap_rate) * feromonio[i][j]
    for i in range(len(caminhos)):
        for j in range(len(caminhos[i]) - 1):
            feromonio[caminhos[i][j]][caminhos[i][j + 1]] += 1 / custos[i]
        feromonio[caminhos[i][-1]][caminhos[i][0]] += 1 / custos[i]
    return feromonio

def iteration(feromonio, visibilidade, alpha, beta, n_cities, n_ants):
    caminhos = []
    custos = []
    for j in range(n_ants):
        cidade_atual = random.randint(0, n_cities - 1)
        caminho = [cidade_atual]
        custo = 0
        for k in range(n_cities - 1):
            probabilidade = calcula_probabilidade(feromonio[cidade_atual], visibilidade[cidade_atual], alpha, beta)
            probabilidade[cidade_atual] = 0  # Evita escolher a mesma cidade
            probabilidade_sum = np.sum(probabilidade)
            if probabilidade_sum == 0:
                probabilidade = np.ones(n_cities) / (n_cities - 1)
                probabilidade[cidade_atual] = 0
            else:
                probabilidade = probabilidade / probabilidade_sum  # Re-normaliza as probabilidades
            cidade_atual = np.random.choice(n_cities, 1, p=probabilidade)[0]
            caminho.append(cidade_atual)
            custo += d[caminho[-2]][caminho[-1]]
        custo += d[caminho[-1]][caminho[0]]
        caminhos.append(caminho)
        custos.append(custo)
    return caminhos, custos

def colonia_formigas(n_ants, n_cities, alpha, beta, evap_rate, n_iterations):
    feromonio = np.ones((n_cities, n_cities))
    visibilidade = np.divide(1, d, where=d!=0)
    np.fill_diagonal(visibilidade, 0)  # Define a visibilidade para a própria cidade como zero
    caminhos = []
    custos = []
    for i in range(n_iterations):
        caminhos, custos = iteration(feromonio, visibilidade, alpha, beta, n_cities, n_ants)
        feromonio = atualiza_feromonio(feromonio, caminhos, custos, evap_rate)

    return caminhos, custos

def colonia_formigas_analitico(n_ants, n_cities, alpha, beta, evap_rate, n_iterations):
    feromonio = np.ones((n_cities, n_cities))
    visibilidade = np.divide(1, d, where=d!=0)
    np.fill_diagonal(visibilidade, 0)  # Define a visibilidade para a própria cidade como zero
    caminhos = []
    custos = []
    for i in range(n_iterations):
        print(f"Iteração {i}")
        caminhos, custos = iteration(feromonio, visibilidade, alpha, beta, n_cities, n_ants)
        print(f"Melhor caminho: {caminhos[np.argmin(custos)]}")
        print(f"Custo do melhor caminho: {custos[np.argmin(custos)]}")
        print("===========================================")
        feromonio = atualiza_feromonio(feromonio, caminhos, custos, evap_rate)

    return caminhos, custos