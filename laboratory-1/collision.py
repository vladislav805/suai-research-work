import numpy as np;
from matplotlib import pyplot as plt;
import random;

# Рамки вероятностей, которые будем моделировать
ranges = (.01, .30);

# Шаг моделирования
step = 0.01;

rangesScale = 1 / step;

# количество слотов для моделирования
slots = 1000;

# примеры графиков по количеству абонентов
examples = [2, 3, 5, 15, 50];

# Генерация лямбд
lambdas = [i / rangesScale for i in range(int(ranges[0] * rangesScale), int(ranges[1] * rangesScale), int(step * rangesScale))];

# Генерация вектора отправки сообщений абонентами размерностью `count` с вероятностью `p`
def generateVectorMessages(p, count):
    res = [];
    for i in range(count):
        res.append(1 if random.random() <= p else 0);
    return res;

# Функция для моделирования процесса с "глупыми" абонентами
def solve(slots, clients):
    graph = [];
    for curLambda in range(len(lambdas)):
        lost = 0;

        for slot in range(1, slots):
            clientsInterFlow = generateVectorMessages(lambdas[curLambda], clients);

            if (sum(clientsInterFlow) > 1):
                lost += 1;

        graph.append(lost / slots);

    return graph;

# Вывод графика
plt.figure();
for i in range(len(examples)):
    plt.plot(lambdas, solve(slots, clients = examples[i]), label = 'Clients = {}'.format(examples[i]));

plt.legend();
plt.xlabel('Вероятность отправки');
plt.ylabel('Вероятность наложения/коллизии');
plt.grid();
plt.show();
