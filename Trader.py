pip install yfinance
import yfinance as yf
import pandas as pd
import numpy as np


class Trader:
    def __init__(self, trader, position, budget) -> None:
        self.trader = trader
        self.position = position
        self.budget = budget

    def getData(symbol, start_date, end_date) -> any:
        data = yf.download(symbol, start = start_date, end = end_date)
        return data

    def predict_price():
        raise NotImplementedError

    def black_scholes_model():
        raise NotImplementedError

    def monte_carlo_sim():
        raise NotImplementedError

if "__main__" == __name__:
    trader = Trader()
    trader.getData()
    trader.predict_price()
    trader.black_scholes_model()
    trader.monte_carlo_sim()