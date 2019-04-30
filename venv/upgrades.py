# coding=utf-8

class Upgrade():

    def __init__(self, name, basecost, baserate, multiplier, owned):
        self.name = name
        self.basecost = basecost
        self.baserate = baserate
        self.multiplier = multiplier
        self.owned = owned
        self.price = basecost * (multiplier ** owned)
        self.speed = baserate * owned

    def buy(self, count):
        self.owned += count
        self.speed = self.baserate * self.owned
        self.price = self.basecost * (self.multiplier ** self.owned)

    def sell(self, count):
        buy(-min(count, self.owned))


upgrades = []
def build_upgrades():
    upg_names = [
        u'Пальчик',
        u'Сосед',
        u'Ролик для одежды',
        u'Личный робот',
        u'Магнитно-статическая камера',
        u'Машина времени',
        u'Генератор антиволос'
    ]
    upg_basecosts = [
        15,
        100,
        500,
        3000,
        10000,
        40000,
        200000
    ]
    upg_baserates = [
        0.1,
        0.5,
        4,
        10,
        40,
        100,
        400
    ]
    for i in range(7):
        upgrades.append(Upgrade(upg_names[i], upg_basecosts[i], upg_baserates[i], 1.15, 0))


class Score():

    def __init__(self):
        self.curscore = 0
        self.curspeed = 0

    def click(self):
        self.curscore += 1

