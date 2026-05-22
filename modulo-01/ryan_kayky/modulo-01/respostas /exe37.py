import json
from datetime import datetime
from typing import Dict, Any

class Produto:
    def __init__(self, nome: str, preco: float, criado_em: datetime):
        self.nome = nome
        self.preco = preco
        self.criado_em = criado_em

def produto_para_dict(produto: 'Produto') -> Dict[str, Any]:
    return {
        "nome": produto.nome,
        "preco": produto.preco,
        "criado_em": produto.criado_em.isoformat()
    }

def dict_para_produto(dados: Dict[str, Any]) -> 'Produto':
    return Produto(
        nome=dados["nome"],
        preco=dados["preco"],
        criado_em=datetime.fromisoformat(dados["criado_em"])
    )

lista_produtos = [
    Produto("A", 10.0, datetime.now()),
    Produto("B", 20.0, datetime.now()),
    Produto("C", 30.0, datetime.now())
]

json_str = json.dumps([produto_para_dict(p) for p in lista_produtos])
lista_desserializada = [dict_para_produto(d) for d in json.loads(json_str)]