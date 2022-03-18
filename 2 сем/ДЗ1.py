from random import randint

class Human:
    """Класс человек"""

    def __init__(self, name, age, sostoyanie):
        self.name = name
        self.age = age
        self.sostoyanie = sostoyanie

    def speek(self):
        return f'Меня зовут: {self.name} , мне {self.age}, я {self.sostoyanie}'

    def __repr__(self):
        return self.name


class Queue:
    """Класс очереди"""

    def __init__(self):
        self.line = []

    def nalichie(self):
        return self.line == []

    def length_Queue(self):
        return len(self.line)

    def remove_human(self, human):
        if len(self.line) < 1:
            return None
        return self.line.remove(human)

    def add_human(self, human):
        self.line.insert(0, human)

    def pronoknovenie(self, name, age, sostoyanie):
        if len(self.line) == 0:
            self.add_human(Human(name, age, sostoyanie))
        else:
            self.line.insert(randint(1, len(self.line)), Human(name, age, sostoyanie))

    def chek(self):
        print(f'очередь: {self.line}')

N1 = Human("Школьник", 0 , "Сдал ЕГЭ на 30 баллов")
N2 = Human("Наталья-Морская пехота", 22, "Джип в Москве")
N3 = Human("Калик", 50, "ЭАОы")
N4 = Human("Димасик", 18, "Алкоголик")

Pyaterochka = Queue()
print(Pyaterochka.nalichie())

Pyaterochka.add_human(N1)
Pyaterochka.add_human(N2)
Pyaterochka.add_human(N3)
Pyaterochka.add_human(N4)

Pyaterochka.chek()

Pyaterochka.remove_human(N3)
print(Pyaterochka.length_Queue())

Pyaterochka.chek()

Pyaterochka.pronoknovenie("Нияз", 23, "Люблю пивасик")
Pyaterochka.chek()

