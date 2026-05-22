dados = input("Qual é o seu PESO e ALTURA? ")
peso, altura = map(float, dados.split())

imc = peso / (altura * altura)

print(f"O imc é {imc:.2f}")

