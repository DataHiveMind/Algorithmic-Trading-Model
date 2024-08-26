# Libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf
import pygwalker as pyg



# Python File Functions
import FinancialDerivativePricer as FDP
import FinancialIndictator as FIR
import FinancialMathematics as FM
import FinancialTimeSeriesAnalyzer as FTSA
import HestonModel as HM
import HighFrequencyTrader as HFT
import LoanPricePredictor as LPP
import MachineLearning as ML
import SABRModel as SM
import StatisticalDataMining as SDM
import StockVolatility as SV
import QuantitativeFinance as QF
import Trader as tr


# Getting Financial Data
stocks = ["AAPL", "MSFT", "AMZN", "GOOG", "IBM"]
d1 = tr.getData(stocks, "2015-01-01", "2020-01-01")

# EDA and Display the Data 
df = pd.read_csv('./bike_sharing_dc.csv')
walker = pyg.walk(df)

# Use of Financial MatheMatics 
FM.Stock_Valuation()
FM.Bond_Valuation()
FM.Portfolio_Valuation()



loan_data = {'borrower_income': 50000, 'debt_to_income': 0.5, 'credit_score': 700, 'loan_amount': 10000, 'loan_term': 36, 'property_value': 200000, 'purpose': 'debt_consolidation'}
#predicted_price = predictor.predict_price(loan_data)
#print(predicted_price)


#call_price = price_call_option(strike_price=100, time_to_maturity=0.5)
#put_price = price_put_option(strike_price=100, time_to_maturity=0.5)
#forward_price = price_forward_contract(strike_price=100, time_to_maturity=0.5)
#futures_price = price_futures_contract(strike_price=100, time_to_maturity=0.5)