# Stock Tracker

## Description
A stock analysis tool that calculates technical indicators and visualizes trends using mock data. Built to practice Python fundamentals: data structures, algorithms, web scraping, and Flask.

## Features
1. Mock stock data generator — Create realistic fake stock prices locally
2. Technical indicators — Calculate SMA, EMA, Bollinger Bands, RSI
3. Web dashboard — Flask app showing stock charts + indicators
4. Yahoo Finance scraper — Pull financial news headlines
5. CLI tool — Query stocks, run analysis from command line
6. Local JSON storage — Persist mock data and news

## Tech Stack
1. Flask

## Getting Started
### Prerequisites
1. Python 3.10+, pip
### Installation
1. Clone/download repo
2. pip install -r requirements.txt
3. [anything else?]
### Usage
1. run tests, lint, and coverage: `make verify`
2. Start web dashboard: python web/app.py
3. View at http://localhost:5000

### Project Structure
stock-analyzer/
├── requirements.txt
├── main.py

### Learning Goals
- Implement technical indicator algorithms (SMA, EMA, RSI, Bollinger Bands)
- Web scraping with BeautifulSoup
- Data persistence with JSON
- Flask web application basics
- CLI tool development

### Data Structures
- **List/Deque** — Store price history for sliding window calculations (SMA, EMA)
- **Dictionary** — Map stock symbols to price data and indicators
- **namedtuple/dataclass** — Represent OHLC (Open, High, Low, Close) candlesticks
- **defaultdict** — Group news headlines by stock symbol
- **heapq** — Find top performing stocks (max/min heap)
- **pandas DataFrame** — Efficient tabular data for analysis and calculations 

### Stock Market Knowledge
SMA (Simple Moving Average)
The SMA is the average price of a stock over a specific number of time periods. It is calculated by adding the closing prices for a set duration (e.g., 50 days) and dividing by that number. It smooths out price volatility to help identify the overall direction of a trend.

EMA (Exponential Moving Average)
The EMA is similar to the SMA but gives more weight to recent price data. Because it prioritizes what happened yesterday over what happened a month ago, it reacts much faster to price changes and trend reversals than the SMA.

Bollinger Bands
Bollinger Bands consist of three lines: a middle SMA and two outer bands calculated using standard deviation.

Volatility Indicator: The bands expand when the market is volatile and contract when it is quiet.

Overbought/Oversold: Prices touching the upper band may indicate the stock is "overbought," while touching the lower band may indicate it is "oversold".

RSI (Relative Strength Index)
The RSI is a momentum oscillator that measures the speed and change of price movements on a scale from 0 to 100.

Overbought: An RSI above 70 generally suggests a stock is becoming overvalued or overbought and may be due for a pullback.

Oversold: An RSI below 30 suggests it is undervalued or oversold and might be primed for a bounce.