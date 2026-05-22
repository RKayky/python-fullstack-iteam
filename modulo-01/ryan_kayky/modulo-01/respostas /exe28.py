def calcular_juros_compostos(capital: float, taxa: float, periodo: int) -> float:
    """
    Calcula o montante final usando juros compostos.

    Args:
        capital (float): Valor inicial do investimento.
        taxa (float): Taxa de juros em porcentagem.
        periodo (int): Número de períodos.

    Returns:
        float: O montante final após os juros.

    Raises:
        ValueError: Se o capital ou a taxa forem valores negativos.

    Example:
        >>> calcular_juros_compostos(1000.0, 10.0, 2)
        1210.0
    """
    if capital < 0 or taxa < 0:
        raise ValueError("Capital e taxa não podem ser negativos.")
    return capital * (1 + taxa / 100) ** periodo