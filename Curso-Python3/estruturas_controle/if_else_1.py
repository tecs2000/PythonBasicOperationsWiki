class TerminalColor:
    ERRO = '\033[91m'
    NORMAL = '\033[0m'


def nota_conceito(valor):
    nota = valor

    if nota > 10 or nota < 0:
        return(TerminalColor.ERRO + "Nota invalida!" + TerminalColor.NORMAL)

    elif nota >= 9.1:
        return "Conceito: A"

    elif nota >= 8.1:
        return "Conceito: A-"

    elif nota >= 7.1:
        return "Conceito: B"

    elif nota >= 6.1:
        return "Conceito: B-"

    elif nota >= 5.1:
        return "Conceito: C"

    elif nota >= 4.1:
        return "Conceito: C-"

    elif nota >= 3.1:
        return "Conceito: D"

    elif nota >= 2.1:
        return "Conceito: D-"

    elif nota >= 1.1:
        return "Conceito: E"

    else:
        return "Conceito: E-"


if __name__ == "__main__":
    nota = float(input("Digite a sua nota: "))
    print(nota_conceito(nota))
