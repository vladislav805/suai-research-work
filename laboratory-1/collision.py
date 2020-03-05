import numpy as np;
from matplotlib import pyplot as plt;
import random;
import decimal

def drange(x, y, jump):
  while x < y:
    yield float(x)
    x += decimal.Decimal(jump)

# Рамки Лямбды Пуассона
ranges = (.01, .30);

# Шаг моделирования
step = 0.01;

rangesScale = 1 / step;

# Генерация лямбд
lambdas = [i / rangesScale for i in range(int(ranges[0] * rangesScale), int(ranges[1] * rangesScale), int(step * rangesScale))];

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


slots = 1000; # количество слотов для моделирования

examples = [2, 3, 5, 15, 50]; # количество абонентов, варианты для моделирования

plt.figure();
for i in range(len(examples)):
    plt.plot(lambdas, solve(slots, clients = examples[i]), label = 'Clients = {}'.format(examples[i]));

plt.legend();
plt.xlabel('Вероятность отправки');
plt.ylabel('Вероятность наложения/коллизии');
plt.grid();
plt.show();
