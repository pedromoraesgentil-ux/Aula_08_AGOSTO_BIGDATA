def calcula_preco (q,p):
    r=q*p
    print (f'\nO valor da compra do cliente {Cliente} é de R${r:.2f} ')

for i in range (5):
    Cliente= input(f'\nDigite o nome do Cliente: ')
    quantidade= int(input('Quantidade de itens ?'))
    preco= float(input('Informe o valor da compra R$'))
    calcula_preco(quantidade,preco)

print('Programa Encerrado')



    






