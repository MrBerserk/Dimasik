import random
import time
from multiprocessing import Pool


def func():
    array = []
    for i in range(10**6):
        array.append(random.randint(-100, 100))
    print(sum(array)%2)


if __name__ == '__main__':
    print('В одном потоке:')

    t1 = time.time()
    for _ in range(4):
        func()
    print(time.time()-t1, 'секунд')

    print('В 4 потоках:')
    t1 = time.time()
    with Pool(4) as p:
        r = []
        for _ in range(4):
            r.append(p.apply_async(func))
        for a in r:
            a.wait()
    print(time.time()-t1, 'секунд')