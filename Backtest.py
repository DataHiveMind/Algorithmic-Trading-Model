import talib

def __init__(self):
     pass

def sma(self, period: int):
    """AI is creating summary for sma

    Args:
        period (int): Time period being used

    Returns:
        [type]: [description]
    """
    return talib.SMA(self.data, timeperiod=period)

def ema(self, period: int):
    """AI is creating summary for ema

    Args:
        period (int): [description]

    Returns:
        [type]: [description]
    """
    return talib.EMA(self.data, timeperiod=period)

def rsi(self, period: int):
    """AI is creating summary for ema

    Args:
        period (int): [description]

    Returns:
        [type]: [description]
    """
    return talib.RSI(self.data, timeperiod=period)

def mom(self, period: int):
    """AI is creating summary for ema

    Args:
        period (int): [description]

    Returns:
        [type]: [description]
    """
    return talib.MOM(self.data, timeperiod=period)

def stocrsi(self, period: int):
    """AI is creating summary for ema

    Args:
        period (int): [description]

    Returns:
        [type]: [description]
    """
    return talib.STOCHRSI(self.data, timeperiod=period)

def bbands(self, period: int):
    """AI is creating summary for ema

    Args:
        period (int): [description]

    Returns:
        [type]: [description]
    """
    return talib.BBands(self.data, timeperiod=period)
