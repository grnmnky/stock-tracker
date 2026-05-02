import argparse
from src.mock_data import generate_mock_data


def main():
    parser = argparse.ArgumentParser(...)
    parser.add_argument("--generate", type=str, help="Symbol to generate data for")
    parser.add_argument("--days", type=int, default=365, help="Number of days to generate")
    args = parser.parse_args()

    if not args.generate:
        parser.print_help()
        raise SystemExit(1)

    symbol = args.generate.strip().upper()
    generate_mock_data(symbol, args.days)

if __name__ == "__main__":
    main()