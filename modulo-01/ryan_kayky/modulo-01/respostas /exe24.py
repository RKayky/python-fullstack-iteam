from typing import Tuple

def converter_moeda(valor_brl: float) -> Tuple[float, float]:
    """
    Converte um valor em Reais (BRL) para Dólar (USD) e Euro (EUR).

    Args:
        valor_brl (float): Valor em reais a ser convertido.

    Returns:
        Tuple[float, float]: Uma tupla contendo o valor em USD e o valor em EUR.

    Example:
        >>> converter_moeda(10.0)
        (1.9417475728155338, 1.7921146953405017)
    """
    usd = valor_brl / 5.15
    eur = valor_brl / 5.58
    return usd, eur