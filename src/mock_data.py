
import argparse
import json
import os
import random
from datetime import datetime, timedelta


def generate_mock_data(symbol, days=365):
    # Starting parameters
    price = random.uniform(50.0, 500.0)
    data = []
    start_date = datetime.now() - timedelta(days=days)

    for i in range(days):
        # Calculate a small random change (-2% to +2%)
        change_percent = random.uniform(-0.02, 0.02)
        price = price * (1 + change_percent)

        current_date = start_date + timedelta(days=i)
        data.append(
            {
                "date": current_date.strftime("%Y-%m-%d"),
                "price": round(price, 2),
                "volume": random.randint(1000, 10000),
            }
        )

    # Save to data directory
    os.makedirs("data", exist_ok=True)
    file_path = f"data/{symbol}.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump({"symbol": symbol, "history": data}, f, indent=4)

    print(f"Successfully generated {days} days of mock data for {symbol} at {file_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--generate", type=str, help="Symbol to generate data for")
    parser.add_argument("--days", type=int, default=365, help="Number of days to generate")
    args = parser.parse_args()

    if args.generate:
        generate_mock_data(args.generate, args.days)
