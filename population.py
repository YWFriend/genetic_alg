import numpy as np
from numpy import ndarray
from individ import Individual
from typing import Callable


class Population:  # Класс, описывающий популяцию
    def __init__(
            self,
            population: list[Individual],
            phenotype_of_population: float = 0.0
    ):
        self.population: list[Individual] = population
        self.phenotype_of_population: float = phenotype_of_population

    def info(self):
        for individual in self.population:
            individual.info()
        print("Средний фенотип по поколению =", self.phenotype_of_population)

    def crossover(self, double_cross: bool):
        for s in range(0, len(self.population) // 2, 2):  # Цикл. От 0 до размера популяции с шагом 2.

            # # Кроссенговер
            # ran = random.randint(1, 5)
            #
            # for n in range(ran):
            #     temp_ar.pop[s].indiv[n] = pop1.pop[s].indiv[n]
            #     temp_ar.pop[s + 1].indiv[n] = pop1.pop[s + 1].indiv[n]
            # for n in range(ran, 9):
            #     temp_ar.pop[s].indiv[n] = pop1.pop[s + 1].indiv[n]
            #     temp_ar.pop[s + 1].indiv[n] = pop1.pop[s].indiv[n]

            # Двойной Кроссенговер
            for m in range(3):
                temp_ar.pop[s].indiv[m] = pop1.pop[s].indiv[m]
                temp_ar.pop[s + 1].indiv[m] = pop1.pop[s + 1].indiv[m]

                temp_ar.pop[s].indiv[m + 3] = pop1.pop[s + 1].indiv[m + 3]
                temp_ar.pop[s + 1].indiv[m + 3] = pop1.pop[s].indiv[m + 3]

                temp_ar.pop[s].indiv[m + 6] = pop1.pop[s].indiv[m + 6]
                temp_ar.pop[s + 1].indiv[m + 6] = pop1.pop[s + 1].indiv[m + 6]

    @staticmethod
    def create_population(population_size: int, genotype_array: list, attac_function: Callable):
        pop = [Individual.create_individual(genotype_array, attac_function) for _ in range(population_size)]

        return Population(
            pop,
            float(np.mean(list(map(lambda x: x.phenotype, pop))))
        )
