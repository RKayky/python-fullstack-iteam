valor_compra = float(input("Valor da compra: "))
desconto = valor_compra * 0.10
valor_final = valor_compra - desconto

print(f"Desconto: R$ {desconto:.2f}")
print(f"Valor final: R$ {valor_final:.2f}")