import json
from typing import Any, Dict

config_dados = {
    "app": {"versao": "1.0.0", "modo": "producao"},
    "banco": {"host": "localhost", "porta": 5432},
    "email": {"servidor": "smtp.mail.com"}
}
with open("config.json", "w") as f:
    json.dump(config_dados, f, indent=4)

def carregar_config(caminho: str) -> Dict[str, Any]:
    with open(caminho, "r") as f:
        return json.load(f)

def obter_valor(config: Dict[str, Any], chave: str, padrao: Any = None) -> Any:
    chaves = chave.split('.')
    atual = config
    for c in chaves:
        if isinstance(atual, dict) and c in atual:
            atual = atual[c]
        else:
            return padrao
    return atual

config = carregar_config("config.json")
print(obter_valor(config, "app.versao"))
print(obter_valor(config, "banco.porta"))
print(obter_valor(config, "email.servidor"))
print(obter_valor(config, "app.modo"))
print(obter_valor(config, "inexistente.chave", "N/A"))