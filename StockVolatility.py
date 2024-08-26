
def calculate_returns(self):
        self.returns = np.log(self.price_data['Close']).diff().dropna()

def fit_garch_model(self):
        self.model = arch.arch_model(self.returns, vol='Garch', p=1, q=1)
        self.model_fit = self.model.fit()

def forecast_volatility(self):
        self.volatility_forecast = self.model_fit.forecast(horizon=1)

def compare_volatility(self):
        self.realized_volatility = self.returns.std()
        self.predicted_volatility = self.volatility_forecast.variance.values[-1, 0] ** 0.5

def perform_sensitivity_analysis(self):
        self.parameter_sensitivity = self.model_fit.conditional_volatility.diff().dropna()

if "__main__" == __name__:
    data = yf.download('AAPL', start='2020-01-01', end='2021-01-01')
    stock = StockVolatility(data)
    stock.calculate_returns()
    stock.fit_garch_model()
    stock.forecast_volatility()
    stock.compare_volatility()
    stock.perform_sensitivity_analysis()