
def somar(valor1, valor2):
    resultado = valor1 + valor2
    print('O resultado da soma é {}'.format(resultado))


def subtracao(valor1, valor2):
    resultado = valor1 - valor2
    print('O resultado da subtração é {}'.format(resultado))


def divisao(valor1, valor2):
    resultado = valor1 / valor2
    print('O resultado da divisão é {}'.format(resultado))


def multiplicacao(valor1, valor2):
    resultado = valor1 * valor2
    print('O resultado da multiplicação é {}'.format(resultado))


texto_pergunta = 'Digite o {} valor: '


primeiro_valor = float(input(texto_pergunta.format('primeiro')))
segundo_valor = float(input(texto_pergunta.format('segundo')))

somar(primeiro_valor, segundo_valor)
subtracao(primeiro_valor, segundo_valor)
divisao(primeiro_valor, segundo_valor)
multiplicacao(primeiro_valor, segundo_valor)






