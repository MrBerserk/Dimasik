from queue import Queue


class Projectile:
    """ Класс снаряда """
    G_CONST = 9.78  # ускорение свободного падения

    def __init__(self, caliber, mass):
        self.caliber = caliber
        self.mass = mass
        self.power = caliber * mass * Projectile.G_CONST


class Clip:
    """ Класс обоймы """
    def __init__(self):
        self.storage = Queue()

    def add(self, item):
        self.storage.append(item)

    def save(self):
        file = open('1.txt', 'w', encoding='utf8')
        file.write(f'В обойме {self.storage.length} снарядов:\n')

        i = 0
        while True:
            i += 1
            item = self.storage.enqueue()
            if item is None:
                break
            file.write(f'Снаряд {i}: {item.caliber}, {item.mass}, {item.power}\n')


c = Clip()
c.add(Projectile(1, 10))
c.add(Projectile(1, 10))
c.add(Projectile(2, 20))
c.save()