capital = float(input("Capital inicial: "))
taxa_mensal = float(input("Taxa de juros ao mês (%): ")) / 100
meses = int(input("Período (meses): "))

montante = capital * (1 + taxa_mensal * meses)
juros_totais = montante - capital

print(f"Capital: R$ {capital:.2f}")
print(f"Taxa: {taxa_mensal * 100:.2f}% ao mês")
print(f"Período: {meses} meses")
print(f"Juros Totais: R$ {juros_totais:.2f}")
print(f"Montante Final: R$ {montante:.2f}")