import json
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


def test_generate_mock_data_respects_requested_days(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    symbol = "MSFT"
    days = 3
    generate_mock_data(symbol, days=days)

    output_file = Path("data") / f"{symbol}.json"
    assert output_file.exists()

    payload = json.loads(output_file.read_text(encoding="utf-8"))
    assert payload["symbol"] == symbol
    assert len(payload["history"]) == days
