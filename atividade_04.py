def dobro (x):
    r=x*2
    return r


def triplo (y):
    r=y*3
    return r


def quadrado (q):
    r=q*q
    return r


#Inicio fluxo do programa 
numero=int(input(f'Informe o número desejado:'))

resposta_dobro = dobro(numero)
respost_triplo = triplo(numero)


resposta_quadrado = quadrado (numero)

#final do fluxo
print(f'O dobro do numero é {resposta_dobro}')
print(f'O triplo do numero é {respost_triplo}')
print(f'O quadrado do numero é {resposta_quadrado}')
