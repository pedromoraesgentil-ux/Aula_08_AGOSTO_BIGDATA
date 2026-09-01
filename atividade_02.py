def hora_trabalhada (d,h):#definicação da função 
    r= (d/h)
    print(f'O valor da hora é de R${r}')


#corpo da função 

nome = input(f'Olá!Informe o seu nome: ')
horastotal=int(input(f'Informe quantas horas foram trabalhadas no dia:'))
diaria=int(input(f'Informe qual valor da sua diária:'))

hora_trabalhada (diaria,horastotal) #chamada da função







