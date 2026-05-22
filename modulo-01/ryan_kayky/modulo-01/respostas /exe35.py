import json
from typing import List, Dict, Any

vendas_json = """
[
    {"mes": "Janeiro",  "produto": "Notebook", "quantidade": 45, "valor_unit": 3200.00},
    {"mes": "Janeiro",  "produto": "Mouse",    "quantidade": 120, "valor_unit": 89.90},
    {"mes": "Fevereiro","produto": "Notebook", "quantidade": 38, "valor_unit": 3200.00},
    {"mes": "Fevereiro","produto": "Teclado",  "quantidade": 75, "valor_unit": 149.90},
    {"mes": "Março",    "produto": "Monitor",  "quantidade": 30, "valor_unit": 1200.00},
    {"mes": "Março",    "produto": "Mouse",    "quantidade": 200,"valor_unit": 89.90}
]
"""
vendas = json.loads(vendas_json)

def calcular_total_mes(vendas: List[Dict[str, Any]], mes: str) -> float:
    return sum(v["quantidade"] * v["valor_unit"] for v in vendas if v["mes"] == mes)

def produto_mais_vendido(vendas: List[Dict[str, Any]]) -> str:
    contagem: Dict[str, int] = {}
    for v in vendas:
        contagem[v["produto"]] = contagem.get(v["produto"], 0) + v["quantidade"]
    return max(contagem, key=contagem.get)

def receita_total(vendas: List[Dict[str, Any]]) -> float:
    return sum(v["quantidade"] * v["valor_unit"] for v in vendas)