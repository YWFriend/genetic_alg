from population import Population
from numpy import mgrid, ndarray, zeros, random


def individuals() -> list[[int, int]]:  # Create a list of unique coordinates
    xy = mgrid[:8, :8].reshape(2, -1).T
    sample: ndarray
    sample = xy.take(random.choice(xy.shape[0], 9, replace=False), axis=0)
    return list(map(lambda a: list(a), sample))


def attack(genotype: list[tuple[int, int]]) -> int:  # King's attack function
    board = zeros((8, 8))
    for i in genotype:
        for a in range(i[0] - 1, i[0] + 2):
            for b in range(i[1] - 1, i[1] + 2):
                if 0 <= a < 8 and 0 <= b < 8:
                    board[a][b] = 1
    return board.sum()


def main():
    pop = Population.create_population(population_size=200, genotype_func=individuals, attack_function=attack)
    pop.breeding(iteration_count=150, limit=64)


if __name__ == '__main__':
    main()
