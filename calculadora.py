def somar(a, b):
    """Soma dois números."""
    return a + b


def subtrair(a, b):
    """Subtrai o segundo número do primeiro."""
    return a - b


def multiplicar(a, b):
    """Multiplica dois números."""
    return a * b


def dividir(a, b):
    """Divide dois números e evita divisão por zero."""
    if b == 0:
        return None

    return a / b


# Testa as funções apenas quando este arquivo for executado diretamente
if __name__ == "__main__":
    print(somar(10, 5))
    print(subtrair(10, 5))
    print(multiplicar(10, 5))
    print(dividir(10, 5))
    print(dividir(10, 0))