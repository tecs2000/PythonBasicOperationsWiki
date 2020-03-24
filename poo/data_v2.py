class Data:
    def __init__(self, dia, mes, ano):  # no python so pode ter 1 const
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'

    # o metodo acima pode ser chamado de forma implicita
    # atraves de def __str__(self), pois cvt o dado p str


d1 = Data(5, 12, 2020)
print(d1)

d2 = Data(7, 11, 2020)
print(d2)
