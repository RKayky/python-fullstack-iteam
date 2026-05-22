import json
from typing import List, Dict, Any, Optional

ARQUIVO_ALUNOS = "alunos.json"

def _carregar_alunos() -> List[Dict[str, Any]]:
    try:
        with open(ARQUIVO_ALUNOS, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def _salvar_alunos(dados: List[Dict[str, Any]]) -> None:
    with open(ARQUIVO_ALUNOS, "w") as f:
        json.dump(dados, f, indent=4)

def cadastrar_aluno(nome: str, email: str, idade: int, notas: List[float]) -> Dict[str, Any]:
    """
    Cadastra um novo aluno e persiste no arquivo JSON.

    Args:
        nome (str): Nome completo do aluno.
        email (str): Email de contato.
        idade (int): Idade em anos.
        notas (List[float]): Lista de notas obtidas pelo aluno.

    Returns:
        Dict[str, Any]: O dicionário com os dados do aluno recém cadastrado.
    """
    alunos = _carregar_alunos()
    novo_id = max([a["id"] for a in alunos], default=0) + 1
    aluno = {
        "id": novo_id,
        "nome": nome,
        "email": email,
        "idade": idade,
        "notas": notas,
        "ativo": True
    }
    alunos.append(aluno)
    _salvar_alunos(alunos)
    return aluno

def listar_alunos() -> List[Dict[str, Any]]:
    """
    Retorna a lista completa de alunos cadastrados.

    Returns:
        List[Dict[str, Any]]: Lista de dicionários, onde cada um representa um aluno.
    """
    return _carregar_alunos()

def buscar_por_nome(nome: str) -> Optional[Dict[str, Any]]:
    """
    Busca um aluno pelo nome exato.

    Args:
        nome (str): Nome exato a ser buscado.

    Returns:
        Optional[Dict[str, Any]]: Dicionário com os dados do aluno, ou None se não encontrado.
    """
    for aluno in _carregar_alunos():
        if aluno["nome"].lower() == nome.lower():
            return aluno
    return None

def calcular_media_turma() -> float:
    """
    Calcula a média geral agrupando todas as notas de todos os alunos.

    Returns:
        float: Média global da turma.
    """
    todas_notas = [nota for aluno in _carregar_alunos() for nota in aluno["notas"]]
    if not todas_notas:
        return 0.0
    return sum(todas_notas) / len(todas_notas)

def exportar_relatorio() -> None:
    """
    Gera um relatório consolidado da turma e salva em 'relatorio_turma.json'.
    """
    alunos = _carregar_alunos()
    if not alunos:
        return

    medias_alunos = []
    for a in alunos:
        media_aluno = sum(a["notas"]) / len(a["notas"]) if a["notas"] else 0
        medias_alunos.append((a["nome"], media_aluno))

    maior = max(medias_alunos, key=lambda x: x[1])
    menor = min(medias_alunos, key=lambda x: x[1])

    relatorio = {
        "total_alunos": len(alunos),
        "media_geral": calcular_media_turma(),
        "maior_media": {"aluno": maior[0], "media": maior[1]},
        "menor_media": {"aluno": menor[0], "media": menor[1]}
    }
    with open("relatorio_turma.json", "w") as f:
        json.dump(relatorio, f, indent=4)

cadastrar_aluno("João", "joao@email.com", 20, [8.0, 7.5])
cadastrar_aluno("Maria", "maria@email.com", 22, [9.0, 9.5])
cadastrar_aluno("Ana", "ana@email.com", 19, [6.0, 7.0])
cadastrar_aluno("Pedro", "pedro@email.com", 21, [5.5, 6.0])

print(listar_alunos())
print(buscar_por_nome("Maria"))
print(calcular_media_turma())
exportar_relatorio()