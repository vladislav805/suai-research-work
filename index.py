import numpy as np;
from matplotlib import pyplot as plt;
import random;

clients = 5; # N, кол-во абонентов

p = .2; # вероятность появления сообщения у каждого абонента

slots = 1000; # количество слотов для моделирования

queue = [[] for i in range(clients)];

def generate_client_messages(slot):
    for client in range(clients):
        rnd = random.random();
        if (rnd <= p):
            queue[client].append(slot);

def count_queue_lengths():
    res = [0 for i in range(clients)];
    for i in range(clients):
        res[i] = len(queue[i]);
    return res;

def common_queue_length():
    return np.sum(count_queue_lengths())


# class struct(object):
#     def __init__(self, **kwargs):
#         self.__dict__.update(kwargs)

history = [];

for slot in range(slots):
    generate_client_messages(slot);

    clientId = slot % clients;

    if (clientId in queue and len(queue[clientId]) > 0):
        del queue[clientId][0];

    # history.append(struct(items = count_queue_lengths()));
    history.append(common_queue_length());


# plt.title('test');
# plt.xlabel('x');
# plt.ylabel('y');
# plt.plot(np.arange(0, clients), history);
# plt.show();
