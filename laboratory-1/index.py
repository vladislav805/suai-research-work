import numpy as np;
from matplotlib import pyplot as plt;
import random;

clients = 100; # N, кол-во абонентов
slots = 5000; # количество слотов для моделирования
client = 3; # наблюдаемый клиент

lambdas = [i / 10000 for i in range(1, 150)];

def getInterflow(p, n):
    res = [];
    for i in range(n):
        res.append(1 if random.random() <= p else 0);
    return res;

def pushBuffers(buffer, interflow, i):
    buffer.append(buffer[i - 1] + interflow[i]);

def popMessage(buffer, interflow, i):
    if (buffer[i - 1] > 0):
        buffer[i] -= 1;

def solve(slots, clients):
    graph = []; # данные для графика
    print(len(graph));
    for i in range(len(lambdas)):
        curLambda = lambdas[i];

        interflow = getInterflow(curLambda, slots); # генерация сообщений

        buffer = [interflow[0]]; # размер буфера в определённом слоте

        for slot in range(1, slots):
            pushBuffers(buffer, interflow, slot);
            if slot % clients == client:
                popMessage(buffer, interflow, slot);

        graph.append(clients * sum(buffer) / slots);
        del buffer;

    return graph;

plt.xlabel('Вероятность успешной отправки');
plt.ylabel('Среднее число сообщений в слоте');
plt.plot(lambdas, solve(slots, 50));
plt.grid();
plt.show();
