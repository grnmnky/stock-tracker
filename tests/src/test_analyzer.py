import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from src.analyzer import calculate_sma


def test_calculate_sma_returns_none_when_window_is_greater_than_prices():
    prices = [100, 200, 300]
    window = 4
    assert calculate_sma(prices, window) is None

def test_calculate_sma_raises_value_error_when_window_is_less_than_one():
    prices = [100, 200, 300]
    window = 0
    try:
        calculate_sma(prices, window)
        assert False, "Expected ValueError when window is less than one"
    except ValueError:
        pass

def test_calculate_sma_returns_empty_list_when_prices_is_empty():
    prices = []
    window = 3
    assert calculate_sma(prices, window) == []

def test_calculate_sma_returns_one_value_when_window_is_equal_to_prices():
    prices = [100, 200, 300]
    window = 3
    assert calculate_sma(prices, window) == [200]

def test_calculate_sma_returns_multiple_values_when_window_is_less_than_prices():
    prices = [100, 200, 300, 400, 500]
    window = 3
    assert calculate_sma(prices, window) == [200, 300, 400]