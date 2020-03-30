class RGB:
    def __init__(self):
        self.cores = ['red', 'green', 'blue'][::-1]

    def __next__(self):
        try:
            return self.cores.pop()
        except IndexError:
            raise StopIteration()

    def __iter__(self):
        return self.cores.__iter__()


if __name__ == '__main__':
    cores = RGB()

    for cor in cores:
        print(cor)

    # Printa e da pop() na lista
    print(next(cores))
    print(next(cores))
    print(next(cores))

    try:
        print(next(cores))

    except StopIteration:
        print('Acabou!')
