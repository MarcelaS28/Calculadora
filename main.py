
def somar(valor1, valor2):
    return valor1 + valor2


def subtracao(valor1, valor2):
    return valor1 - valor2


def divisao(valor1, valor2):
    return valor1 / valor2


def multiplicacao(valor1, valor2):
    return valor1 * valor2

def definir_opcao():
    opcoes = ['[1] Soma', '[2] Subtração', '[3] Divisão', '[4] Multiplicação']
    for opcao in opcoes:
        print(opcao)

    opcao_escolhida = int(input('Escolha uma opção: '))
    if opcao_escolhida == 1:
        return somar(primeiro_valor, segundo_valor)
    elif opcao_escolhida == 2:
        return subtracao(primeiro_valor, segundo_valor)
    elif opcao_escolhida == 3:
        return divisao(primeiro_valor, segundo_valor)
    elif opcao_escolhida == 4:
        return multiplicacao(primeiro_valor, segundo_valor)
    else:
        print('Opcção inexistente')


texto_pergunta = 'Digite o {} valor: '


primeiro_valor = float(input(texto_pergunta.format('primeiro')))
segundo_valor = float(input(texto_pergunta.format('segundo')))

resultado = definir_opcao()

print('Resultado: {}'.format(resultado))