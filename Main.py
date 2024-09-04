# Libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf


# Python File Functions
import FinancialDerivativePricer as FDP
import Backtest as back
import FinancialTimeSeriesAnalyzer as FTSA
import HestonModel as HM
import HighFrequencyTrader as HFT
import LoanPricePredictor as LPP
import MachineLearning as ML
import SABRModel as SM
import StatisticalDataMining as SDM
import StockVolatility as SV
import QuantitativeFinance as QF



# Getting Financial Data
import Trader as tr

stocks = ["AAPL", "MSFT", "AMZN", "GOOG", "IBM", "FB"]
data = tr.getData(stocks, "2015-01-01", "2020-01-01")

pred = tr.predict_price()

Call = tr.BS_CALL()

Put = tr.BS_PUT()

MCS = tr.monte_carlo_sim()


# EDA and Display the Data 
import FinancialIndictator as FIR
# import pygwalker as pyg

df = pd.read_csv('./bike_sharing_dc.csv')
#walker = pyg.walk(df)

# Use of Financial MatheMatics
import FinancialMathematics as FM

FM.Stock_Valuation()
FM.Bond_Valuation()
FM.Portfolio_Valuation()


if __name__ == "__main__":
    stock = yf.download("AAPl", start_date = "2015-01-01", end_date = "2020-01-01")
    test = back.sma(stock['Close', 14])
    print(test)

    loan_data = {'borrower_income': 50000, 'debt_to_income': 0.5, 
             'credit_score': 700, 'loan_amount': 10000, 'loan_term': 36, 
             'property_value': 200000, 'purpose': 'debt_consolidation'}
    #predicted_price = predictor.predict_price(loan_data)
    #print(predicted_price)


    #call_price = price_call_option(strike_price=100, time_to_maturity=0.5)
    #put_price = price_put_option(strike_price=100, time_to_maturity=0.5)
    #forward_price = price_forward_contract(strike_price=100, time_to_maturity=0.5)
    #futures_price = price_futures_contract(strike_price=100, time_to_maturity=0.5)