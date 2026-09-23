// Funções de utilidade para reutilizar em outros programas

funcao real converter_temperatura(real temperatura, texto escala) inicio

    // converte Celsius para Fahrenheit
    se (escala = "C") entao
        retorne (temperatura * 9 / 5) + 32
    fimse

    // converte Fahrenheit para Celsius
    se (escala = "F") entao
        retorne (temperatura - 32) * 5 / 9
    fimse

    retorne 0
fimfuncao


funcao logico validar_senha(texto senha) inicio

    // verifica se a senha possui pelo menos 8 caracteres
    se (tamanho(senha) >= 8) entao
        retorne verdadeiro
    fimse

    retorne falso
fimfuncao


funcao real caixa(real precos[]) inicio

    real total
    inteiro contador

    total <- 0

    // soma todos os preços da lista
    para contador de 0 ate tamanho(precos) - 1 faca
        total <- total + precos[contador]
    fimpara

    retorne total
fimfuncao


funcao adicionar_item(texto lista[], texto item) inicio

    texto nova_lista[]
    inteiro contador

    // cria uma nova lista para não alterar a original
    para contador de 0 ate tamanho(lista) - 1 faca
        nova_lista[contador] <- lista[contador]
    fimpara

    nova_lista[tamanho(lista)] <- item

    escreva("Nova lista: ")

    para contador de 0 ate tamanho(nova_lista) - 1 faca
        escreva(nova_lista[contador])
    fimpara

fimfuncao