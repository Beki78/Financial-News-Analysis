import yfinance as yf

def get_financials(data):
    ticker = yf.Ticker(data)
    financials = ticker.financials
    return financials

