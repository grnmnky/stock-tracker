import pandas as pd

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

def calculate_ema(prices: list[float], window: int) -> list[float] | None:
    """
    Calculates the Exponential Moving Average.
    Formula: EMA = (Price * k) + (Previous EMA * (1 - k))
    where k = 2 / (window + 1)
    """
    if window <= 0:
        raise ValueError("window must be greater than 0")
    if not prices:
        return []
    if len(prices) < window:
        return None

    # 1. Smoothing factor (multiplier)
    k = 2 / (window + 1)

    # 2. Seed the EMA with the SMA of the first window
    first_ema = sum(prices[:window]) / window
    ema_values = [first_ema]

    # 3. Calculate subsequent values recursively
    # We start at the first price AFTER the initial window
    for i in range(window, len(prices)):
        current_price = prices[i]
        previous_ema = ema_values[-1]
        
        ema_now = (current_price * k) + (previous_ema * (1 - k))
        ema_values.append(ema_now)

    return ema_values

def calculate_bollinger_bands(prices: pd.Series, window: int) -> tuple[pd.Series, pd.Series, pd.Series]:
    if not isinstance(prices, pd.Series):
        raise TypeError("must be a pandas series")

    middle_band = prices.rolling(window=window).mean()
    std_dev = prices.rolling(window=window).std()
    
    upper_band = middle_band + (std_dev * 2)
    lower_band = middle_band - (std_dev * 2)

    return upper_band, middle_band, lower_band