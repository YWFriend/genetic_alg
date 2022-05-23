import numpy as np
from typing import Callable
from numpy import ndarray


class Individual:  # Класс, описывающий индивида
    genotype: list[tuple[int, int]]
    phenotype: int

    def __init__(
            self,
            genotype: list[tuple[int, int]],
            attack_function: Callable[[ndarray], int]
    ) -> None:
        self.genotype: list[tuple[int, int]] = genotype
        self.attack_function: Callable[[ndarray], int] = attack_function
        self.phenotype: int = attack_function(self.genotype)

    def info(self):  # Вывод на экран индивида
        np.set_printoptions(linewidth=np.inf)
        print(self.genotype.tolist(), ' = ', self.phenotype)

def create_individual(genotype_array: list[tuple[int, int]]) -> Individual:
    return Individual(
        genotype= genotype_array
    )
