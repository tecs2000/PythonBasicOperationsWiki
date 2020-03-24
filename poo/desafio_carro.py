class Carro:
    def __init__(self, vel_max):
        self.vel_atual = 0
        self.vel_max = vel_max

    def acelerar(self, val=5):
        self.vel_atual = self.vel_atual + val if self.vel_atual + \
            val <= self.vel_max else self.vel_max

        return self.vel_atual

    def frear(self, val=5):
        self.vel_atual = self.vel_atual - val if self.vel_atual - \
            val >= 0 else 0

        return self.vel_atual


if __name__ == '__main__':
    c1 = Carro(180)  # vel max, min = 0

    for _ in range(25):
        print(c1.acelerar(8))  # defaut = 5

    for _ in range(10):
        print(c1.frear(val=20))
