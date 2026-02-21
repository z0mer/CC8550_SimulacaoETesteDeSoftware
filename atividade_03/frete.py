"""Módulo de cálculo de frete."""


def _normalizar_destino(destino: str) -> str:
    """Normaliza destino para uma chave interna válida."""
    if not isinstance(destino, str):
        raise ValueError("Destino inválido")

    texto = destino.strip().lower()

    equivalencias = {
        "mesma_regiao": "mesma_regiao",
        "mesma regiao": "mesma_regiao",
        "mesma região": "mesma_regiao",
        "outra_regiao": "outra_regiao",
        "outra regiao": "outra_regiao",
        "outra região": "outra_regiao",
        "internacional": "internacional",
    }

    if texto not in equivalencias:
        raise ValueError("Destino inválido")

    return equivalencias[texto]


def calcular_frete(peso: float, destino: str, valor_pedido: float) -> float:
    """Calcula o valor do frete com base no peso, destino e valor do pedido."""
    if peso <= 0:
        raise ValueError("Peso deve ser maior que zero")

    if peso > 20:
        raise ValueError("Peso acima de 20 kg não é aceito")

    if valor_pedido < 0:
        raise ValueError("Valor do pedido não pode ser negativo")

    if valor_pedido > 200:
        return 0.0

    destino_normalizado = _normalizar_destino(destino)

    if peso <= 1:
        frete_base = 10.0
    elif peso <= 5:
        frete_base = 15.0
    else:
        frete_base = 25.0

    multiplicadores = {
        "mesma_regiao": 1.0,
        "outra_regiao": 1.5,
        "internacional": 2.0,
    }

    return frete_base * multiplicadores[destino_normalizado]
