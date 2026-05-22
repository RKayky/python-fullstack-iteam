descricao = input("Descrição: ")
qtd = int(input("Quantidade: "))
preco = float(input("Preço Unitário: "))

subtotal = qtd * preco
imposto = subtotal * 0.12
total = subtotal + imposto

print("===== NOTA FISCAL =====")
print(f"Produto   : {descricao}")
print(f"Quantidade: {qtd} unidade(s)")
print(f"Preço Unit: R$ {preco:.2f}")
print(f"Subtotal  : R$ {subtotal:.2f}")
print(f"Imposto   : R$ {imposto:.2f}")
print(f"Total     : R$ {total:.2f}")
print("=======================")