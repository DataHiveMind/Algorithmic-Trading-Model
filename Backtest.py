import talib

def __init__(self):
     pass

def sma(self, period):
        return talib.SMA(self.data, timeperiod=period)

def ema(self, period):
    return talib.EMA(self.data, timeperiod=period)

def rsi(self, period):
    return talib.RSI(self.data, timeperiod=period)
