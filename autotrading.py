import pandas as pd
import yfinance as yf

# Load price data from Yahoo Finance
def load_price_data(symbol, start_date, end_date):
    # Fetch historical price data from Yahoo Finance
    price_data = yf.download(symbol, start=start_date, end=end_date)
     # Calculate Heikin-Ashi candles
    ha_close = (price_data['Open'] + price_data['High'] + price_data['Low'] + price_data['Close']) / 4
    ha_open = (price_data['Open'].shift(1) + price_data['Close'].shift(1)) / 2
    ha_high = price_data[['High', 'Open', 'Close']].max(axis=1)
    ha_low = price_data[['Low', 'Open', 'Close']].min(axis=1)
    
    # Create a DataFrame for Heikin-Ashi candles
    ha_data = pd.DataFrame({'Open': ha_open, 'High': ha_high, 'Low': ha_low, 'Close': ha_close}, index=price_data.index)
    
    return ha_data

# Calculate 0.5% price change
def calculate_price_change(close):
    price_change = close.pct_change()
    return price_change

# Implement trading strategy
def run_trading_strategy(price_data):
    # Calculate 0.5% price change
    price_change = calculate_price_change(price_data['Close'])
    
    # Buy and Sell Signals
    buyp = price_change >= 0.005
    sellp = price_change <= -0.005
    
    # Initialize position and track the current position
    position = None
    
    # Strategy entry conditions
    buy_condition = buyp & (position is None or position == -1)
    sell_condition = sellp & (position is None or position == 1)
    
    # Stop loss calculation
    stop = price_data['Low'].shift(1).rolling(window=2).min()
    
    # Initialize signals DataFrame
    signals = pd.DataFrame(index=price_data.index)
    signals['Buy'] = buy_condition
    signals['Sell'] = sell_condition | (price_data['Close'] < stop)
    
    # Backtesting
    trades = []
    for index, row in signals.iterrows():
        if row['Buy']:
            if position != 1:
                position = 1
                trades.append((index, 'Buy'))
        elif row['Sell']:
            if position != -1:
                position = -1
                trades.append((index, 'Sell'))
    
    # Print trading signals
    for trade in trades:
        print(f"{trade[1]} signal at: {trade[0]}")
    
    # Plotting signals
    # You can use your preferred plotting library to visualize the buy and sell signals.

# Main function
def main():
    # Define parameters
    symbol = 'BTC-USD'  # Stock symbol (e.g., AAPL for Apple Inc.)
    start_date = '2024-01-01'  # Start date for historical data
    end_date = '2024-03-29'    # End date for historical data
    
    # Load price data
    price_data = load_price_data(symbol, start_date, end_date)
    
    # Run trading strategy
    run_trading_strategy(price_data)

if __name__ == "__main__":
    main()
