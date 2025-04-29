soma = 0
contador = 0

print("Digite as notas para calcular a média. Digite 'n' para finalizar.")

while True:
    entrada = input("Digite uma nota: ")
    
    if entrada.lower() == 'n':  # Verifica se o usuário quer encerrar
        break
    
    try:
        numero = float(entrada)  # Converte a entrada para número
        soma += numero           # Soma o número
        contador += 1            # Incrementa o contador
    except ValueError:
        print("Por favor, insira um número válido ou 'n' para finalizar.")

# Calcula e exibe a média
if contador > 0:
    media = soma / contador
    print(f"A média dos números digitados é: {media:.2f}")
else:
    print("Nenhum número válido foi digitado.")