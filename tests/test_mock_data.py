import json
import os
import tempfile
import unittest
from pathlib import Path

from src.mock_data import generate_mock_data


def test_generate_mock_data_creates_expected_json(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    symbol = "AAPL"
    days = 5
    generate_mock_data(symbol, days=days)

    output_file = Path("data") / f"{symbol}.json"
    assert output_file.exists()

    payload = json.loads(output_file.read_text(encoding="utf-8"))
    assert payload["symbol"] == symbol
    assert len(payload["history"]) == days

    for entry in payload["history"]:
        assert set(entry) == {"date", "price", "volume"}
        assert isinstance(entry["date"], str)
        assert isinstance(entry["price"], float)
        assert isinstance(entry["volume"], int)


class TestMockDataGeneration(unittest.TestCase):
    def test_generate_mock_data_creates_expected_json(self):
        previous_cwd = os.getcwd()
        try:
            with tempfile.TemporaryDirectory() as tmpdir:
                os.chdir(tmpdir)
                symbol = "MSFT"
                days = 3
                generate_mock_data(symbol, days=days)

                output_file = Path("data") / f"{symbol}.json"
                self.assertTrue(output_file.exists())

                payload = json.loads(output_file.read_text(encoding="utf-8"))
                self.assertEqual(payload["symbol"], symbol)
                self.assertEqual(len(payload["history"]), days)
        finally:
            os.chdir(previous_cwd)
