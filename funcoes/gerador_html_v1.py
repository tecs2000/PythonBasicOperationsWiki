#!/usr/local/lib/python3.6


def tag_bloco(texto, classe='success'):   # classe = opcional
    return f'<div class="{classe}">{texto}</div>'


if __name__ == '__main__':
    # Testes (assertions) : se for false, gera erro
    assert tag_bloco('Incluido com sucesso!') == \
        '<div class="success">Incluido com sucesso!</div>'

    assert tag_bloco('Impossivel excluir!', 'error') == \
        '<div class="error">Impossivel excluir!</div>'

    print(tag_bloco('bloco'))
