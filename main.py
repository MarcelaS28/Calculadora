
def somar(valor1, valor2):
    return valor1 + valor2


def subtracao(valor1, valor2):
    return valor1 - valor2


def divisao(valor1, valor2):
    return valor1 / valor2


def multiplicacao(valor1, valor2):
    return valor1 * valor2

def definir_opcao(opcao):
    if opcao == 1:
        return somar(primeiro_valor, segundo_valor)
    elif opcao == 2:
        return subtracao(primeiro_valor, segundo_valor)
    elif opcao == 3:
        return divisao(primeiro_valor, segundo_valor)
    elif opcao == 4:
        return multiplicacao(primeiro_valor, segundo_valor)
    else:
        print('Opcção inexistente')


texto_pergunta = 'Digite o {} valor: '


primeiro_valor = float(input(texto_pergunta.format('primeiro')))
segundo_valor = float(input(texto_pergunta.format('segundo')))


print('[1] Soma')
print('[2] Subtração')
print('[3] Divisão')
print('[4] Multiplicação')
opcao = int(input('Escolha uma opção: '))

resultado = definir_opcao(opcao)

print('Resultado: {}'.format(resultado))