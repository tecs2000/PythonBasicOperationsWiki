def fatorial(n):
    return n * (fatorial(n-1) if (n-1) > 1 else 1)


if __name__ == '__main__':
    print(fatorial(10))

    # 10 fat == qtd seg. em 6 semanas
    print(6 * 7 * 24 * 60 * 60)
