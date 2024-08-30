import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import norm
from scipy.stats import lognorm as log
import pylab as pl

def __init__(self):
    pass


def getData(symbol, start_date, end_date) -> pd.DataFrame:
    data = yf.download(symbol, start = start_date, end = end_date)
    return data

def Options(k: int, s: int)-> any:
    # Options payoff modelling
    optype = input("Rnter the option type (C/P): ")

    if optype == "C":
        payoff = max(0, (s-k)) # Make Money when Stock goes Up
    elif optype == "P":
        payoff = max(0, (k-s)) # Make Money when Stock goes Down
    print("Payoff is: ", payoff)

def predict_price():
    raise NotImplementedError

def BS_CALL(S: float, K: float, T: float, R: float, sigma:float):
    """
    Calculate the Black-Scholes price.

    Parameters
    ----------
    S (float)
        Current stock price
    K (float)
        Strike price
    T (float)
        Time to maturity (in years)
    R (float)
        Risk-free interest rate (annual)
    Sigma (float)
        Volatility of the stock (annual)

    Returns
    -------
    float
        Price of the European put option
    """
    N = norm.cdf
    d1 = np.log(S/K) + (R + sigma**2/2)*T / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return S-N(d1) - K * np.exp(-R * T)* N(d2)

def BS_PUT(S, K, T, R, sigma) -> float:
    """
    Calculate the Black-Scholes price.

    Parameters
    ----------
    S (float)
        Current stock price
    K (float)
        Strike price
    T (float)
        Time to maturity (in years)
    R (float)
        Risk-free interest rate (annual)
    Sigma (float)
        Volatility of the stock (annual)

    Returns
    -------
    float
        Price of the European put option
    """
    N = norm.cdf
    d1 = np.log(S/K) + (R + sigma**2/2)*T / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return K * np.exp(-R * T)* N(-d2) - S * N(-d1)

def black_scholes_model(k: int, r: float, t: int, sigma: float):
    """
    Calculate the Black-Scholes price.

    Parameters
    ----------
    S (float)
        Current stock price
    K (float)
        Strike price
    T (float)
        Time to maturity (in years)
    R (float)
        Risk-free interest rate (annual)
    Sigma (float)
        Volatility of the stock (annual)

    Returns
    -------
    float
        Price of the European put option
    """
    s = np.arange(60,140,0.1) # array range

    calls = [BS_CALL(s, k, t, r, sigma) for s in s] # array of series of option value
    puts = [BS_PUT(s, k, t, r, sigma) for s in s]

    plt.plot(s, calls, label = "Call value")
    plt.plot(s, puts, label = "Put value")
    plt.xlabel("Stock Price")
    plt.ylabel("Option Value")
    plt.title("Impact of BSM of S")
    plt.legend()

def monte_carlo_sim():
    raise NotImplementedError

