# classe = opcional
def tag_bloco(conteudo, classe='success', inlane=False):
    tag = 'span' if inlane else 'div'
    return f'<{tag} class="{classe}">{conteudo}</{tag}>'


def tag_lista(*itens):
    Lista = ''.join(f'<li>{item}</li>' for item in itens)
    return f'<ul>{Lista}</ul>'


if __name__ == '__main__':
    print(tag_bloco('bloco'))
    print(tag_bloco('inline e classe', 'info', True))

    # qdo os parametros estao em ordem, n precisa nomear!
    print(tag_bloco('inline', inlane=True))
    print(tag_bloco(inlane=True, conteudo='inline'))

    print(tag_bloco('falhou', classe='error'))

    # packing
    print(tag_bloco(tag_lista('Item 1', 'Item 2'), classe='info'))
