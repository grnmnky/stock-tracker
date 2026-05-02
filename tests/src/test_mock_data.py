import json
import runpy
import sys
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


def test_mock_data_module_cli_generate_path(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    # Avoid runpy warning by ensuring module is not already loaded.
    sys.modules.pop("src.mock_data", None)
    monkeypatch.setattr("sys.argv", ["mock_data.py", "--generate", "NVDA", "--days", "2"])

    runpy.run_module("src.mock_data", run_name="__main__")

    output_file = Path("data") / "NVDA.json"
    assert output_file.exists()

    payload = json.loads(output_file.read_text(encoding="utf-8"))
    assert payload["symbol"] == "NVDA"
    assert len(payload["history"]) == 2
