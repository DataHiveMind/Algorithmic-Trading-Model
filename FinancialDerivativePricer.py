class FinancialDerivativePricer:
    def __init__(self, model, data):
        self.model = model
        self.data = data

    def price_call_option(self, strike_price, time_to_maturity):
        # Implement the pricing logic for a call option using the chosen model
        pass

    def price_put_option(self, strike_price, time_to_maturity):
        # Implement the pricing logic for a put option using the chosen model
        pass

    def price_forward_contract(self, strike_price, time_to_maturity):
        # Implement the pricing logic for a forward contract using the chosen model
        pass

    def price_futures_contract(self, strike_price, time_to_maturity):
        # Implement the pricing logic for a futures contract using the chosen model
        pass

if "__main__" == __name__:
    model = HestonModel(mean_reversion=0.05, correlation=0.5)
    data = yf.download('AAPL', start='2020-01-01', end='2021-01-01')
    pricer = FinancialDerivativePricer(model, data)
    call_price = pricer.price_call_option(strike_price=100, time_to_maturity=0.5)
    put_price = pricer.price_put_option(strike_price=100, time_to_maturity=0.5)
    forward_price = pricer.price_forward_contract(strike_price=100, time_to_maturity=0.5)
    futures_price = pricer.price_futures_contract(strike_price=100, time_to_maturity=0.5)