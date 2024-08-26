import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def getData(symbol, start_date, end_date) -> pd.DataFrame:
    data = yf.download(symbol, start = start_date, end = end_date)
    return data

data = getData("AAPL", "2015-01-01", "2020-01-01")
print(data)