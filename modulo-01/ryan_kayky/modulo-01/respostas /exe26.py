from typing import Optional, Union, Dict, Any

def buscar_usuario(id_usuario: int, nome: Union[str, None] = None) -> Optional[Dict[str, Any]]:
    """
    Busca os dados de um usuário pelo ID e nome.

    Args:
        id_usuario (int): ID numérico do usuário.
        nome (Union[str, None], optional): Nome do usuário. Defaults to None.

    Returns:
        Optional[Dict[str, Any]]: Dicionário com os dados do usuário ou None se o id for negativo.
    """
    if id_usuario < 0:
        return None
    return {"id": id_usuario, "nome": nome, "status": "Ativo"}