from abc import ABCMeta, abstractmethod


class Humano(metaclass=ABCMeta):
    # atributo de classe
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome
        self._idade = None

    @abstractmethod
    def inteligente(self):
        pass

    # Os @s abaixo permitem que o atributo idade seja
    # setado e printado no main 'como se fosse' um atributo
    # publico, mas respeitando as exigencias
    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        if idade < 0:
            raise ValueError('Idade deve ser um numero positivo')
        self._idade = idade

    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'
        return self

    @staticmethod
    def especies():
        adjetivos = ('Habilis', 'Erectus', 'Neanderthalensis', 'Sapiens')
        return ('Australopiteco',) + tuple(f'Homo {adj}' for adj in adjetivos)

    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1]


class Neanderthal(Humano):
    especie = Humano.especies()[-2]

    @property
    def inteligente(self):
        return False


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]

    @property
    def inteligente(self):
        return True


if __name__ == '__main__':
    # Agora apenas as classes concretas poderao ser instaciadas
    try:
        anonimo = Humano('John Doe')

    except TypeError:
        print('Humano eh uma classe abstrata.')

    jose = HomoSapiens('Jose')
    grogn = Neanderthal('Grogn')

    print('{} da classe {}, inteligente: {}'.format(
        jose.nome, jose.__class__.__name__, jose.inteligente))

    print('{} da classe {}, inteligente: {}'.format(
        grogn.nome, grogn.__class__.__name__, grogn.inteligente))
