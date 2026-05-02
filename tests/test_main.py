import main as main_module


def test_main_calls_generate_mock_data(monkeypatch):
    captured = {}

    def fake_generate(symbol, days):
        captured["symbol"] = symbol
        captured["days"] = days

    monkeypatch.setattr(main_module, "generate_mock_data", fake_generate)
    monkeypatch.setattr(
        "sys.argv", ["main.py", "--generate", "msft", "--days", "10"]
    )

    main_module.main()

    assert captured == {"symbol": "MSFT", "days": 10}


def test_main_exits_when_symbol_missing(monkeypatch):
    monkeypatch.setattr("sys.argv", ["main.py"])

    try:
        main_module.main()
        assert False, "Expected SystemExit when --generate is missing"
    except SystemExit as exc_info:
        assert exc_info.code == 1

