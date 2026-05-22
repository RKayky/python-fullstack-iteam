import json

produto = {
    "id": 1,
    "nome": "Notebook",
    "preco": 3500.00,
    "estoque": 15,
    "disponivel": True,
    "categorias": ["Eletrônicos", "Informática"]
}

with open("produto.json", "w") as f:
    json.dump(produto, f, indent=4)

with open("produto.json", "r") as f:
    dados_lidos = json.load(f)

for chave, valor in dados_lidos.items():
    print(f"{chave.capitalize()}: {valor}")