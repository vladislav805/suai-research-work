import numpy as np;
from matplotlib import pyplot as plt;
import random;

# N, кол-во абонентов
clients = 100;

# количество слотов для моделирования
slots = 50000;

# наблюдаемый клиент
client = 3;

# Рамки вероятностей, которые будем моделировать
ranges = (.001, .025);

# Шаг моделирования
step = 0.001;

rangesScale = 1 / step;

# Генерация лямбд
lambdas = [i / rangesScale for i in range(int(ranges[0] * rangesScale), int(ranges[1] * rangesScale), int(step * rangesScale))];

# Генерация вектора с `n` сообщений с вероятностью `p`
def getInterflow(p, n):
    res = [];
    for i in range(n):
        res.append(1 if random.random() <= p else 0);
    return res;

# Добавление сообщения в буфер
def pushBuffers(buffer, interflow, i):
    buffer.append(buffer[i - 1] + interflow[i]);

# Удаление сообщения из буфера
def popMessage(buffer, interflow, i):
    if (buffer[i - 1] > 0):
        buffer[i] -= 1;

# Решалка с параметрами слотов и клиентов
def solve(slots, clients):
    graph = []; # данные для графика
    print(len(graph));
    for i in range(len(lambdas)):
        curLambda = lambdas[i];

        # генерация сообщений
        interflow = getInterflow(curLambda, slots);

        # buffer - количество сообщений в буфере в определённом слоте
        buffer = [interflow[0]];

        for slot in range(1, slots):
            pushBuffers(buffer, interflow, slot);
            if slot % clients == client:
                popMessage(buffer, interflow, slot);

        graph.append(clients * sum(buffer) / slots);
        del buffer;

    return graph;

plt.figure();
plt.xlabel('Вероятность успешной отправки');
plt.ylabel('Среднее число сообщений в слоте');

examples = [10, 70, 100];
for i in range(len(examples)):
    plt.plot(lambdas, solve(slots, examples[i]), label = '{} clients'.format(examples[i]));
plt.legend();
plt.grid();
plt.show();
