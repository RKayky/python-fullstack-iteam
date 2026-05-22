from typing import TypedDict, List
import json

class ItemPedido(TypedDict):
    produto: str
    quantidade: int
    preco_unitario: float

class Pedido(TypedDict):
    id_pedido: int
    cliente: str
    itens: List[ItemPedido]
    status: str

meu_pedido: Pedido = {
    "id_pedido": 9982,
    "cliente": "João Silva",
    "itens": [
        {"produto": "Mousepad", "quantidade": 2, "preco_unitario": 25.50},
        {"produto": "Teclado Mecânico", "quantidade": 1, "preco_unitario": 250.00}
    ],
    "status": "Processando"
}

print(json.dumps(meu_pedido, indent=4))
