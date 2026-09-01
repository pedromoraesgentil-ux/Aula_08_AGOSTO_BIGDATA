def calcula_anterio_sucessor (n):
    a= n-1
    s= n+1
    return a,s


numero= int(input("Informe um numero"))
anterior, sucessor = calcula_anterio_sucessor(numero)


#final do fluxo 
print(f'O valor do numero escolhido é {numero}')
print(f'O valor do sucessor é {sucessor}')
print(f'O valor do anterior é {anterior}')


