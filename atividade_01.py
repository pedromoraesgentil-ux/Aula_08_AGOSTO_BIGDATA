#DEFINIR A FUNÇÃO 
def calcule_preco(x,y): #x,y são parametros da função 
    resultado = x*y
    print(f'O valor do resultado é {resultado}') #corpo da função 


#inicio do programa 
#entrada
quantidade= int(input('Quantidade:'))
preco= float(input('Informe o preço:'))

#chamada da função
calcule_preco(quantidade,preco)





    