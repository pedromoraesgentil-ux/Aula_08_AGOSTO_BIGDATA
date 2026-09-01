def cal_multa(quantidade_pescada):
    # O limite permitido é 100 kg
    limite = 100
    
    if quantidade_pescada > limite:
        valor_excedente = quantidade_pescada - limite
        multa = 4 * valor_excedente
        print(f"Peso excedido em: {valor_excedente} kg.")
        print(f"Valor da multa a pagar: R$ {multa:.2f}")
    else:
        print("Peso dentro do limite. Não há multa a pagar.")

# Entrada de dados do usuário
quantidade = int(input('Informe a quantidade em kg pescados: '))

# Chamada da função passando o valor digitado
cal_multa(quantidade


                    