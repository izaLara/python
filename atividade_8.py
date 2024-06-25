preco = float(input("Digite o preço do produto: "))
desconto = int(input("Qual a porcentagem do desconto? "))

precoDesconto = preco*desconto
ValorFinal = precoDesconto / 100

print(f"O valor final d produto é: {ValorFinal}")