
def somar(valor1, valor2):
    return valor1 + valor2


def subtracao(valor1, valor2):
    return valor1 - valor2


def divisao(valor1, valor2):
    return valor1 / valor2


def multiplicacao(valor1, valor2):
    return valor1 * valor2


texto_pergunta = 'Digite o {} valor: '


primeiro_valor = float(input(texto_pergunta.format('primeiro')))
segundo_valor = float(input(texto_pergunta.format('segundo')))

resultado_soma = somar(primeiro_valor, segundo_valor)
resultado_subtracao = subtracao(primeiro_valor, segundo_valor)
resultado_divisao= divisao(primeiro_valor, segundo_valor)
resultado_multiplicacao= multiplicacao(primeiro_valor, segundo_valor)

print(30 * '-')

texto_resultado = 'O resultado da {} é: {} '

print (texto_resultado.format('soma', resultado_soma))
print (texto_resultado.format('subtração', resultado_subtracao))
print (texto_resultado.format('divisão', resultado_divisao))
print (texto_resultado.format('multiplicação', resultado_multiplicacao))