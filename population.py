import random
import numpy as np
from individ import Individual
from typing import Callable


class Population:  # Класс, описывающий популяцию
    def __init__(
            self,
            population: list[Individual],
            phenotype: float
    ):
        self.population: list[Individual] = population
        self.phenotype: float = phenotype

    def check_health(self):
        self.phenotype = float(np.mean(list(map(lambda x: x.phenotype, self.population))))

    def info(self):
        for individual in self.population:
            individual.info()
        print("Средний фенотип по поколению =", self.phenotype)

    def sort(self):
        self.population.sort(key=lambda i: i.phenotype)

    def crossover(self):
        for s in range(0, len(self.population) // 2, 2):  # Цикл. От 0 до половины размера популяции с шагом 2.
            # Кроссенговер
            # Берутся пары соседних индивидов, меняются местами часть их генотипа от начала до n
            for i in range(random.randint(1, len(self.population[0].genotype) - 1)):
                self.population[s].genotype[i], self.population[s + 1].genotype[i] = self.population[s + 1].genotype[i], self.population[s].genotype[i]

                self.population[s].check_health()
                self.population[s + 1].check_health()

    @staticmethod
    def create_population(
            population_size: int,
            genotype_func: Callable[[], list],
            attack_function: Callable[[list], int]
    ):
        assert population_size // 2 != 0, 'Size must be even'

        pop = [Individual.create_individual(genotype_func(), attack_function) for _ in range(population_size)]

        return Population(
            population=pop,
            phenotype=float(np.mean(list(map(lambda x: x.phenotype, pop)))),
        )
