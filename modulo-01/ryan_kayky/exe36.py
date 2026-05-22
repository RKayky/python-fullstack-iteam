import json
from typing import List, Dict, Optional

ARQUIVO = "contatos.json"

def _salvar(dados: List[Dict[str, str]]) -> None:
    with open(ARQUIVO, "w") as f:
        json.dump(dados, f, indent=4)

def listar_contatos() -> List[Dict[str, str]]:
    try:
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def adicionar_contato(nome: str, telefone: str, email: str) -> None:
    contatos = listar_contatos()
    contatos.append({"nome": nome, "telefone": telefone, "email": email})
    _salvar(contatos)

def buscar_contato(nome: str) -> Optional[Dict[str, str]]:
    for c in listar_contatos():
        if c["nome"] == nome:
            return c
    return None

def remover_contato(nome: str) -> bool:
    contatos = listar_contatos()
    contatos_novos = [c for c in contatos if c["nome"] != nome]
    if len(contatos) != len(contatos_novos):
        _salvar(contatos_novos)
        return True
    return False

adicionar_contato("Lucas", "111", "l@email.com")
adicionar_contato("Mari", "222", "m@email.com")
adicionar_contato("Beto", "333", "b@email.com")
print(listar_contatos())
print(buscar_contato("Mari"))
remover_contato("Beto")
