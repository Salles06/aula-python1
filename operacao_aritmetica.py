a = 5
b = 3
c = 10
# Adição (+)
resultado = a + b
print(f'soma: {resultado}')

#Subtração

resultado = a - b
print(f'subtracao: {resultado}')

#multiplicação

resultado = a * b
print(f'multiplicacao: {resultado}')

#Divisão Inteira

resultado = a // b
print(f'divisao Inteira: {resultado}')

#Resto de Divisao

resultado = a % b
print(f'resto da divisao: {resultado}')

#Exponencial(**)

resultado = a ** b
print(f'exponencial: {resultado}')

##José foi ao mercado com R$ 50,00. Ele comprou:
# - 2 refrigerantes R$ 8,00/cada
# - 3 pães R$ 4,00
# - 300g de mortadela ( Valor do quilo da mortadela R$ 39,90)
# - Após as compras, José deseka saber quanto
# - Sobrou de seu dinheiro e se há algum valor
# - Exato que ele poderia gastar com os trocados restantes

# Declarando Variavel

saldoinicial = 50
custoRefrigerante = 8
custoPao = 4
custoMortadela = 39.90

valorcompra = (custoRefrigerante * 2) + custoPao + ((custoMortadela / 1000) * 300)

saldofinal = saldoinicial - valorcompra
print(f'Jose chegou com R$ {saldoinicial} e saiu com R$ {saldofinal}')