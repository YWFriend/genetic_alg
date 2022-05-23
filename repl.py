from typing import Callable, Generic, TypeVar
from population import Population
from individ import Individual
import numpy as np
from numpy import ndarray, mgrid, random


def gencoordinates() -> list[tuple[int, int]]:  # Функция создания массива уникальных координат
    xy = mgrid[:8, :8].reshape(2, -1).T
    sample: ndarray
    sample = xy.take(random.choice(xy.shape[0], 9, replace=False), axis=0)
    return list(map(lambda i: (i[0], i[1]), sample))


# def simple_coords() -> list[(int, int)]:
#     coords = [(random.randint(0, 7), random.randint(0, 7)) for _ in range(9)]
#
# def attack(genotype: ndarray) -> int:  # Функция атаки короля
#     board = np.zeros((8, 8))
#     for i in genotype:
#         for a in range(i[0] - 1, i[0] + 2):
#             for b in range(i[1] - 1, i[1] + 2):
#                 if 0 <= a < 8 and 0 <= b < 8:
#                     board[a][b] = 1
#     return board.sum()

arr = gencoordinates()

flag = 1
