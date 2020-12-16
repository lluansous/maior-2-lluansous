"""Arquivo principal que será interpretado pelo interpretador."""


def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""
    # COLOQUE SEU CÓDIGO AQUI
    a = float(input('Digite o primeiro número:'))
    b = float(input('digite o segundo número:'))

    m = max(a,b)
    print(f'{m}')
    

if __name__ == '__main__':
    main()
