import sys
import pandas as pd
import numpy as np
from pathlib import Path

# Setup path to include src directory
ROOT_DIR = Path(__file__).resolve().parents[2]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from src.analyzer import calculate_sma, calculate_ema, calculate_bollinger_bands
import pytest


@pytest.mark.describe("calculate_sma")
class TestCalculateSMA:
    def test_returns_none_when_window_is_greater_than_prices(self):
        prices = [100, 200, 300]
        window = 4
        assert calculate_sma(prices, window) is None

    def test_raises_value_error_when_window_is_less_than_one(self):
        prices = [100, 200, 300]
        window = 0
        with pytest.raises(ValueError):
            calculate_sma(prices, window)

    def test_returns_empty_list_when_prices_is_empty(self):
        prices = []
        window = 3
        assert calculate_sma(prices, window) == []

    def test_returns_one_value_when_window_is_equal_to_prices(self):
        prices = [100, 200, 300]
        window = 3
        assert calculate_sma(prices, window) == [200.0]

    def test_returns_multiple_values_when_window_is_less_than_prices(self):
        prices = [100, 200, 300, 400, 500]
        window = 3
        assert calculate_sma(prices, window) == [200.0, 300.0, 400.0]

    def test_sma_handles_window_of_one(self):
            """SMA with window 1 should just return the price list itself."""
            prices = [10.0, 20.0, 30.0]
            window = 1
            assert calculate_sma(prices, window) == [10.0, 20.0, 30.0]

@pytest.mark.describe("calculate_ema")
class TestCalculateEMA:
    def test_returns_none_when_window_is_greater_than_prices(self):
        prices = [100, 200, 300]
        window = 4
        assert calculate_ema(prices, window) is None

    def test_raises_value_error_when_window_is_less_than_one(self):
        prices = [100, 200, 300]
        window = 0
        with pytest.raises(ValueError):
            calculate_ema(prices, window)

    def test_returns_empty_list_when_prices_is_empty(self):
        """Coverage: Tests the 'if not prices' branch in EMA"""
        assert calculate_ema([], 3) == []

    def test_correct_calculation_logic(self):
        """
        Test EMA with a known sequence.
        Window = 3, so k = 2 / (3 + 1) = 0.5
        Prices = [10, 20, 30, 40]
        1. First EMA (SMA of first 3): (10+20+30)/3 = 20.0
        2. Second EMA: (40 * 0.5) + (20.0 * (1 - 0.5)) = 20 + 10 = 30.0
        """
        prices = [10.0, 20.0, 30.0, 40.0]
        window = 3
        result = calculate_ema(prices, window)
        assert result == [20.0, 30.0]

    def test_ema_is_more_reactive_than_sma(self):
        prices = [10, 10, 10, 10, 10, 50]
        window = 5
        sma = calculate_sma(prices, window)
        ema = calculate_ema(prices, window) 
        assert ema[-1] > sma[-1]

    def test_returns_one_value_when_window_is_equal_to_prices(self):
        prices = [10, 20, 30]
        window = 3
        assert calculate_ema(prices, window) == [20.0]


    def test_ema_handles_window_of_one(self):
        """EMA with window 1 should just return the price list itself."""
        prices = [10.0, 20.0, 30.0]
        window = 1
        # k = 2/(1+1) = 1.0. 
        # EMA_1 = 10.0
        # EMA_2 = (20 * 1.0) + (10 * 0) = 20.0...
        assert calculate_ema(prices, window) == [10.0, 20.0, 30.0]

@pytest.mark.describe("bollinger_bands")
class TestBollingerBands:
    def test_bb_insufficient_data_returns_nulls(self):
        short_series = pd.Series([10, 12, 11, 13,12])
        upper, middle, lower = calculate_bollinger_bands(short_series, window=20)

        assert upper.isnull().all()
        assert middle.isnull().all()
        assert lower.isnull().all()

    def test_bb_invalid_input_data(self):
        with pytest.raises(TypeError, match="must be a pandas series"):
            calculate_bollinger_bands([1, 2, 3], window=20)

    def test_bb_invalid_window_zero(self):
        prices = pd.Series([10, 20, 30, 40, 50])
        with pytest.raises(ValueError, match="window must be greater than 0"):
            calculate_bollinger_bands(prices, window=0)

    def test_bb_invalid_window_negative(self):
        prices = pd.Series([10, 20, 30, 40, 50])
        with pytest.raises(ValueError, match="window must be greater than 0"):
            calculate_bollinger_bands(prices, window=-5)

    def test_bb_empty_list_data(self):
        prices = pd.Series([], dtype=float)
        window = 20

        upper, middle, lower = calculate_bollinger_bands(prices, window)

        assert upper.isnull().all()
        assert middle.isnull().all()
        assert lower.isnull().all()

    def test_bb_invalid_window_type_float(self):
        prices = pd.Series([10, 20, 30, 40, 50])
        with pytest.raises(TypeError, match="window must be an integer"):
            calculate_bollinger_bands(prices, window=5.5)

    def test_bb_invalid_window_type_string(self):
        prices = pd.Series([10, 20, 30, 40, 50])
        with pytest.raises(TypeError, match="window must be an integer"):
            calculate_bollinger_bands(prices, window="10")

    def test_bb_invalid_window_type_boolean(self):
        prices = pd.Series([10, 20, 30, 40, 50])
        with pytest.raises(TypeError, match="window must be an integer"):
            calculate_bollinger_bands(prices, window=True)

    def test_bb_non_numeric_series_elements(self):
        non_numeric_prices = pd.Series(["10", "20", "30", "40", "50"])

        with pytest.raises(TypeError, match="prices series must contain numeric data"):
            calculate_bollinger_bands(non_numeric_prices, window=3)

    def test_bb_simple_window(self):
        prices = pd.Series([10.0, 20.0, 30.0])
        window = 3
        
        upper, middle, lower = calculate_bollinger_bands(prices, window)
        
        assert pd.isna(middle.iloc[0])
        assert pd.isna(middle.iloc[1])
        
        assert middle.iloc[2] == 20.0
        assert upper.iloc[2] == 40.0
        assert lower.iloc[2] == 0.0

    def test_bb_zero_volatility(self):
        """Tests that flat lines (no volatility) have converging bands without issues."""
        prices = pd.Series([15.0, 15.0, 15.0, 15.0, 15.0])
        window = 3
        
        upper, middle, lower = calculate_bollinger_bands(prices, window)

        for i in range(2, 5):
            assert middle.iloc[i] == 15.0
            assert upper.iloc[i] == 15.0
            assert lower.iloc[i] == 15.0

    def test_bb_index_preservation(self):
        """Tests that the dates/indices of the input Series are fully preserved in the output."""
        dates = pd.date_range(start="2026-05-01", periods=5)
        prices = pd.Series([10, 12, 11, 13, 12], index=dates)
        window = 3
        
        upper, middle, lower = calculate_bollinger_bands(prices, window)

        assert (upper.index == dates).all()
        assert (middle.index == dates).all()
        assert (lower.index == dates).all()

    def test_bb_exact_window_length(self):
        """Tests when the series length is precisely equal to the rolling window."""
        prices = pd.Series([10.0, 20.0, 30.0, 40.0])
        window = 4
        
        upper, middle, lower = calculate_bollinger_bands(prices, window)
        
        assert upper.iloc[:3].isnull().all()
        
        assert not pd.isna(upper.iloc[3])
        assert middle.iloc[3] == 25.0

    def test_bb_handles_nan_in_prices(self):
        """Tests that input gaps (NaNs) are handled gracefully and standard Pandas NaN propagation happens."""
        # Index 2 has an explicit NaN value
        prices = pd.Series([10.0, 20.0, np.nan, 40.0, 50.0])
        window = 3
        
        upper, middle, lower = calculate_bollinger_bands(prices, window)
        
        # Rolling calculations containing a NaN in their window will output NaN
        assert pd.isna(middle.iloc[2])  # Window [10, 20, NaN]
        assert pd.isna(middle.iloc[3])  # Window [20, NaN, 40]
        assert pd.isna(middle.iloc[4])  # Window [NaN, 40, 50]

