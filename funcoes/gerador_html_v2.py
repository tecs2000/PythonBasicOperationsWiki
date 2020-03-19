def tag_bloco(texto, classe='success', inlane=False):   # classe = opcional
    tag = 'span' if inlane else 'div'
    return f'<{tag} class="{classe}">{texto}</{tag}>'


if __name__ == '__main__':
    print(tag_bloco('bloco'))
    print(tag_bloco('inline e classe', 'info', True))

    # qdo os parametros estao em ordem, n precisa nomear!
    print(tag_bloco('inline', inlane=True))
    print(tag_bloco(inlane=True, texto='inline'))

    print(tag_bloco('falhou', classe='error'))
