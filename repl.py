from population import Population
import numpy as np
from numpy import ndarray, mgrid, random


def gencoordinates() -> list[tuple[int, int]]:  # Функция создания массива уникальных координат
    xy = mgrid[:8, :8].reshape(2, -1).T
    sample: ndarray
    sample = xy.take(random.choice(xy.shape[0], 9, replace=False), axis=0)
    return list(map(lambda i: (i[0], i[1]), sample))


def attack(genotype: list[tuple[int, int]]) -> int:  # Функция атаки короля
    board = np.zeros((8, 8))
    for i in genotype:
        for a in range(i[0] - 1, i[0] + 2):
            for b in range(i[1] - 1, i[1] + 2):
                if 0 <= a < 8 and 0 <= b < 8:
                    board[a][b] = 1
    return board.sum()


pop = Population.create_population(10, gencoordinates, attack)


flag = 1
