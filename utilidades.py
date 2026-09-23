def converter_temperatura(temperatura, escala):
    """Converte uma temperatura entre Celsius e Fahrenheit."""
    if escala.upper() == "C":
        return (temperatura * 9 / 5) + 32

    if escala.upper() == "F":
        return (temperatura - 32) * 5 / 9

    return None


def validar_senha(senha):
    """Verifica se a senha possui pelo menos 8 caracteres."""
    return len(senha) >= 8


def caixa(*precos):
    """Soma todos os preços recebidos."""
    return sum(precos)


def ficha_aluno(**dados):
    """Mostra os dados recebidos de um aluno."""
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")


def adicionar_item(lista, item):
    """Adiciona um item sem alterar a lista original."""
    nova_lista = lista.copy()
    nova_lista.append(item)

    return nova_lista


# Testa as funções apenas quando este arquivo for executado diretamente
if __name__ == "__main__":
    print(converter_temperatura(30, "C"))
    print(validar_senha("lunanda123"))
    print(caixa(10, 20, 30))

    ficha_aluno(
        nome="Lunanda",
        idade=19,
        curso="Engenharia da Computação"
    )

    lista_original = ["Python", "Java"]
    nova_lista = adicionar_item(lista_original, "Portugol")

    print("Lista original:", lista_original)
    print("Nova lista:", nova_lista)