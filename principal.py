import calculadora
import utilidades


# Usa as funções do módulo calculadora
print("=== CALCULADORA ===")
print(f"Soma: {calculadora.somar(10, 5)}")
print(f"Subtração: {calculadora.subtrair(10, 5)}")
print(f"Multiplicação: {calculadora.multiplicar(10, 5)}")
print(f"Divisão: {calculadora.dividir(10, 5)}")

# testa a divisão por zero
resultado = calculadora.dividir(10, 0)

if resultado is None:
    print("Não é possível dividir por zero.")


# Usa as funções do módulo utilidades
print("\n=== UTILIDADES ===")

temperatura = utilidades.converter_temperatura(30, "C")
print(f"30°C em Fahrenheit: {temperatura:.2f}°F")

senha_valida = utilidades.validar_senha("lunanda123")
print(f"Senha válida: {senha_valida}")

total = utilidades.caixa(10, 25.50, 30)
print(f"Total da caixa: R$ {total:.2f}")


# Mostra os dados do aluno usando **kwargs
print("\n=== FICHA DO ALUNO ===")

utilidades.ficha_aluno(
    nome="Lunanda",
    idade=19,
    curso="Engenharia da Computação"
)


# Cria uma nova lista sem modificar a original
print("\n=== LISTA SEGURA ===")

lista_original = ["Python", "Java"]
nova_lista = utilidades.adicionar_item(lista_original, "Portugol")

print(f"Lista original: {lista_original}")
print(f"Nova lista: {nova_lista}")