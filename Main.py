import random
from copy import copy

import numpy as np

size_of_pop = 200


def sorting(mas):  # Функция сортировки массива координат
    dt = [('col1', mas.dtype), ('col2', mas.dtype)]
    assert mas.flags['C_CONTIGUOUS']
    b = mas.ravel().view(dt)
    b.sort(order=['col1', 'col2'])
    return mas


def gencoordinates():  # Функция создания массива уникальных координат
    nx, ny = 8, 8
    xy = np.mgrid[:nx, :ny].reshape(2, -1).T
    sample = xy.take(np.random.choice(xy.shape[0], 9, replace=False), axis=0)
    return sample


def attack(mas, i, j):  # Функция атаки короля
    for a in (i - 1, i, i + 1):
        for b in (j - 1, j, j + 1):
            if (a >= 0) and (a < 8) and (b >= 0) and (b < 8):
                mas[a][b] = 1
    return mas


class Individ:  # Класс, описывающий индивида
    def __init__(self):
        self.indiv = gencoordinates()  # Объявляем генотипа нашего индивида
        self.hp = 0

    def health(
            self):  # Вычисление фенотипа (сумма всех клеток, бьщихся королями, включая клетки, на которых стоят короли)
        self.hp = 0
        board = np.zeros((8, 8))
        indiv_sort = sorting(copy(self.indiv))
        n = 0
        for i in range(8):  # Расстановка фигур на доске и вычисление бьющихся клеток
            for j in range(8):
                if (i == indiv_sort[n][0]) and (j == indiv_sort[n][1]):
                    if n < 8:
                        n += 1
                    attack(board, i, j)

        for i in range(8):  # Вычисление фенотипа
            for j in range(8):
                self.hp += board[i][j]
        return board

    def info(self):  # Вывод на экран индивида (не используется)
        print(self.indiv)
        self.health()
        print(self.hp)


class Population:  # Класс, описывающий популяцию
    def __init__(self):
        self.pop = []
        for i in range(size_of_pop):
            c = Individ()
            self.pop.append(c)
        self.sr = 0

    def info(self):
        mas_hp = np.arange(size_of_pop)
        for i in range(size_of_pop):
            for j in range(9):
                print(self.pop[i].indiv[j], end=" ")
            print("=", end=" ")
            self.pop[i].health()
            print(self.pop[i].hp)
            mas_hp[i] = self.pop[i].hp
            self.sr = np.mean(mas_hp)
        print("Средний фенотип по поколению =", self.sr)


def main():
    pop1 = Population()  # Создаём экземпляр класса. Т.е. создаём нашу популяцию
    pop1.info()  # Выводим её на экран нашей клёвой функцией вывода.
    result = Individ()

    temp_ar = Population()

    print("\n")  # Отступаем две строчки после вывода нашей стартовой популяции. И да начнётся.. ЕСТЕСТВЕННЫЙ ОТБОР!!!11

    for p in range(150):  # Это наш основной цикл.

        for s in range(0, size_of_pop // 2, 2):  # Цикл. От 0 до размера популяции с шагом 2.

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

        glob_flag = 0

        for h in range(size_of_pop):

            # Создаем мутацию
            ran_mut = random.random()
            ran_gen = random.randint(0, 8)
            if ran_mut < 0.3:
                x_mut = random.randint(0, 7)
                y_mut = random.randint(0, 7)
                temp_ar.pop[h].indiv[ran_gen] = [x_mut, y_mut]

            # Исключаем повторяющиеся гены
            flag = 1
            while flag != 0:
                flag = 0
                for i in range(8):
                    for j in range(i + 1, 9):
                        if temp_ar.pop[h].indiv[i][0] == temp_ar.pop[h].indiv[j][0] and temp_ar.pop[h].indiv[i][1] == \
                                temp_ar.pop[h].indiv[j][1]:
                            x = random.randint(0, 7)
                            y = random.randint(0, 7)
                            temp_ar.pop[h].indiv[j] = [x, y]
                            flag = 1
            temp_ar.pop[h].health()
            if temp_ar.pop[h].hp == 64:
                result.indiv = copy(temp_ar.pop[h].indiv)
                glob_flag = 1
                break

        # Обрываем итерации при нахождении резултьтата
        if glob_flag == 1:

            res_mas = np.array(range(64), str)
            res_mas = res_mas.reshape((8, 8))
            for i in range(8):
                for j in range(8):
                    res_mas[i][j] = "*"

            print("<-------------RESULT------------->")
            print(result.info())

            for t in range(9):
                x = result.indiv[t][0]
                y = result.indiv[t][1]
                res_mas[x][y] = '0'

            print(res_mas)

            break

        for i in range(size_of_pop):
            temp_ar.pop[i].health()

        for m in range(size_of_pop - 1, 0, -1):  # Ранжирование (методом пузырька).
            for b in range(m):
                if temp_ar.pop[b].hp > temp_ar.pop[b + 1].hp:
                    temp_ar.pop[b], temp_ar.pop[b + 1] = temp_ar.pop[b + 1], temp_ar.pop[b]

        for i in range(size_of_pop):
            pop1.pop[i].indiv = copy(temp_ar.pop[i].indiv)

        pop1.info()
        random.shuffle(pop1.pop)
        print(p)


if __name__ == '__main__':
    main()
