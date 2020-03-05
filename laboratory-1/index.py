import numpy as np;
from matplotlib import pyplot as plt;
import random;

clients = 100; # N, кол-во абонентов
slots = 1000; # количество слотов для моделирования
messages = [];
neededClient = 0;

lambdas = [1] #[i / 100 for i in range(5, 100)];

neededClient = 1;

data = [
    1 for i in range(len(lambdas))
];

def getInterflow(_lambda, n):
    return np.random.poisson(_lambda, n);

def pushBuffers(buffers, interflow):
    for i in range(buffers):
        buffers[i] += interflow[i];
    return buffers;

def popMessage(buffers, client):
    if (buffers[client] > 0):
        buffers[client] -= 1;
    return buffers;

def solve(slots, clients):
    graph = []; # данные для графика
    for curLambda in range(len(lambdas)):
        buffers = [0 for i in range(clients)]; # буферы всех абонентов

        for slot in range(slots):
            interflow = getInterflow(curLambda, clients); # генерация сообщений у каждого клиента
            print(interflow);
            break;
            popMessage(buffers, slot % clients);

        break;
        graph.append(clients * sum(buffers) / slots);

    return graph;

plt.title('test');
plt.xlabel('p');
plt.ylabel('Messages');
plt.plot(lambdas, solve(slots, 50));
plt.grid();
plt.show();
