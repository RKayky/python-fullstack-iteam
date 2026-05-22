import json
from typing import List, Dict, Any

def carregar_dados(caminho: str) -> List[Dict[str, Any]]:
    with open(caminho, "r") as f:
        return json.load(f)

def normalizar_dados(dados: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    for d in dados:
        d["nome"] = str(d.get("nome", "")).title().strip()
        d["email"] = str(d.get("email", "")).lower().strip()
    return dados

def enriquecer_dados(dados: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    for d in dados:
        d["status"] = "Ativo"
    return dados

def exportar_resultado(dados: List[Dict[str, Any]], caminho: str) -> None:
    with open(caminho, "w") as f:
        json.dump(dados, f, indent=4)