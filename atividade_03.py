def calculadora (x):
    r=x*2
    return r

#inicio do fluxo do programa
numero=int(input(f'Informe o número desejado:'))
resposta = calculadora(numero)

#final do fluxo

print(f'O dobro do numero é {resposta}')

