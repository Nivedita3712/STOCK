import yfinance as yf
import pandas as pd

# -------------------------------
# Stock symbols
# -------------------------------
stocks = {
    "TCS": "TCS.NS",
    "RELIANCE": "RELIANCE.NS",
    "APPLE": "AAPL",
    "TESLA": "TSLA",
    "MICROSOFT": "MSFT"
}

# -------------------------------
# Date range
# -------------------------------
start_date = "2018-01-01"
end_date = "2024-12-31"

# -------------------------------
# Fetch data for each company
# -------------------------------
for company, symbol in stocks.items():
    print(f"Fetching data for {company} ({symbol})...")
    
    df = yf.download(symbol, start=start_date, end=end_date)
    
    # Reset index to make Date a column
    df.reset_index(inplace=True)
    
    # Save each stock data separately
    file_name = f"{company}_stock_data.csv"
    df.to_csv(file_name, index=False)
    
    print(f"{company} data saved as {file_name}")
    print("-" * 50)

print("✅ Data collection completed for all companies.")
