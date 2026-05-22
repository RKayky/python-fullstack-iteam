from typing import Dict, List, Any

def validar_cadastro(dados: Dict[str, Any]) -> Dict[str, List[str]]:
    """
    Valida dados de cadastro de um usuário.

    Args:
        dados (Dict[str, Any]): Dicionário contendo os dados do usuário.

    Returns:
        Dict[str, List[str]]: Dicionário com chaves 'valido' (lista de campos aprovados) 
        e 'erros' (lista de mensagens de erro).
    """
    resultado: Dict[str, List[str]] = {"valido": [], "erros": []}
    
    if len(dados.get("nome", "")) >= 3:
        resultado["valido"].append("nome")
    else:
        resultado["erros"].append("Nome menor que 3 caracteres.")
        
    email = dados.get("email", "")
    if "@" in email and "." in email:
        resultado["valido"].append("email")
    else:
        resultado["erros"].append("Email inválido.")
        
    idade = dados.get("idade", 0)
    if 18 <= idade <= 120:
        resultado["valido"].append("idade")
    else:
        resultado["erros"].append("Idade fora do intervalo 18-120.")
        
    cpf = dados.get("cpf", "")
    if len(cpf) == 11 and cpf.isdigit():
        resultado["valido"].append("cpf")
    else:
        resultado["erros"].append("CPF deve ter exatamente 11 dígitos numéricos.")
        
    return resultado