import json
from datetime import datetime
from typing import List, Dict, Any

def registrar_evento(arquivo: str, nivel: str, mensagem: str) -> None:
    """Registra um evento em formato JSON no arquivo de log especificado."""
    try:
        with open(arquivo, "r") as f:
            logs = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        logs = []
        
    novo_log = {
        "timestamp": datetime.now().isoformat(),
        "nivel": nivel,
        "mensagem": mensagem
    }
    logs.append(novo_log)
    
    with open(arquivo, "w") as f:
        json.dump(logs, f, indent=2)

def ler_logs(arquivo: str) -> List[Dict[str, Any]]:
    """Lê todos os logs de um arquivo JSON."""
    try:
        with open(arquivo, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def filtrar_por_nivel(logs: List[Dict[str, Any]], nivel: str) -> List[Dict[str, Any]]:
    """Filtra uma lista de logs por nível de severidade."""
    return [log for log in logs if log["nivel"] == nivel]

registrar_evento("sistema.log", "INFO", "Sistema iniciado")
registrar_evento("sistema.log", "INFO", "Usuário logado")
registrar_evento("sistema.log", "WARNING", "Memória alta")
registrar_evento("sistema.log", "ERROR", "Falha no banco")
registrar_evento("sistema.log", "INFO", "Job concluído")

logs_gerais = ler_logs("sistema.log")
erros = filtrar_por_nivel(logs_gerais, "ERROR")
print(erros)
