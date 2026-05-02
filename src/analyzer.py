def calculate_sma(prices: list[float], window: int) -> list[float | None]:
    if window <= 0:
        raise ValueError("window must be greater than 0")

    if not prices:
        return []

    if len(prices) < window:
        return None

    sma_values = []
    for index in range(len(prices) - window + 1):
        window_slice = prices[index : index + window]
        sma_values.append(sum(window_slice) / window)

    return sma_values