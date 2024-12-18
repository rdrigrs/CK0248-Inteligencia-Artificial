"""
    Projeto Computacional 1
    Disciplina: CK0248 - Inteligência Artificial
    Professor: Dr. João Paulo do Vale Madeiro
    Aluno: Rodrigo Rodrigues Santos
    Matrícula: 539105

    Descrição: Implementação do algoritmo genético e do algoritmo colônia de formigas para resolver o problema do caixeiro viajante com 15 cidades.

    O problema do caixeiro viajante (PCV) é um problema de otimização
    que consiste em encontrar o menor caminho que passa por todas as cidades de um conjunto,
    visitando cada cidade uma única vez e retornando à cidade de origem.

    O algoritmo genético é um método de otimização que simula a evolução natural,
    onde a população é composta por indivíduos que representam soluções para o problema.
    A cada geração, os indivíduos são avaliados, selecionados, cruzados e mutados,
    gerando uma nova população de indivíduos.

    O algoritmo colônia de formigas é um método de otimização baseado no comportamento
    de formigas reais, onde as formigas artificiais constroem soluções para o problema
    através de um processo de busca local e global.
"""
from algoritmo_colonia_formigas import colonia_formigas_analitico
from algoritmo_genetico import analytics_genetic_algorithm


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

def executar_algoritmo_genetico():
    pop_size = 100
    crom_size = len(d)
    generations = 1000
    mutation_rate = 0.2
    print("Algoritmo Genético")
    analytics_genetic_algorithm(pop_size, crom_size, generations, mutation_rate)
    print("===========================================")

def executar_algoritmo_colonia_formigas():
    n_ants = 100
    n_cities = len(d)
    alpha = 1
    beta = 2
    evap_rate = 0.1
    n_iterations = 1000
    print("Algoritmo Colônia de Formigas")
    colonia_formigas_analitico(n_ants, n_cities, alpha, beta, evap_rate, n_iterations)
    print("===========================================")


def main():
    while(True):
        choice = input("Digite 1 para executar o Algoritmo Genético e 2 para executar o Algoritmo Colônia de Formigas: ")
        if choice == '1':
            executar_algoritmo_genetico()
        elif choice == '2':
            executar_algoritmo_colonia_formigas()
        else:
            print("Opção inválida. Tente novamente.")
            continue


if __name__ == '__main__':
    main()