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
1. Start web dashboard: python web/app.py
2. View at http://localhost:5000
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