file_name = '2.csv'


class Sim:
    def __init__(self, name):
        self.name = name

    def eat_smithing(self, product_name, count):
        f = open(file_name, 'a', encoding='utf8')
        f.write(f'{self.name},{product_name},{count}\n')
        f.close()

    def get_eats(self):
        data = []
        for line in open(file_name, 'r', encoding='utf8').readlines():
            res = line[:-1].split(',')
            res = (res[0], res[1], int(res[2]))
            print(res)
            data.append(res)

s = Sim('Dima')
s.eat_smithing('milk', 1)
s.eat_smithing('apple', 2)
s.eat_smithing('chocolate', 10)
s.get_eats()