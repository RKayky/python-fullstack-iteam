capacidade_caminhao = 850
peso_caixa = 32

quantiCai = capacidade_caminhao // peso_caixa
peso_restante = capacidade_caminhao % peso_caixa

print(f"O caminhão comporta {quantiCai} caixas completas.")
print(f"O peso que sobra e não completa uma caixa é de {peso_restante} kg.")