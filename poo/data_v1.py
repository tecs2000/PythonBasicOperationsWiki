class Data:
    def to_str(self):
        return f'{self.dia}/{self.mes}/{self.ano}'

    # o metodo acima pode ser chamado de forma implicita
    # atraves de def __str__(self), pois cvt o dado p str


d1 = Data()
d1.dia = 5
d1.mes = 12
d1.ano = 2020
print(d1.to_str())

d2 = Data()
d2.dia = 7
d2.mes = 11
d2.ano = 2020
print(d2.to_str())
