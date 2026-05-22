from typing import TypeVar, List, Callable, Dict, Any

T = TypeVar('T')
R = TypeVar('R')

def aplicar_transformacao(dados: List[T], funcao: Callable[[T], R]) -> List[R]:
    return [funcao(item) for item in dados]

res_str = aplicar_transformacao(["ola", "mundo"], str.upper)
res_float = aplicar_transformacao([1.123, 4.567], lambda x: round(x, 2))
dicts = [{"v": 10}, {"v": 20}]
res_dict = aplicar_transformacao(dicts, lambda d: d["v"])