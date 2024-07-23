class FinancialTimeSeriesAnalyzer:
    def __init__(self, data):
        self.data = data

    def calculate_returns(self):
        self.returns = self.data.pct_change().dropna()

    def calculate_volatility(self):
        self.volatility = self.returns.std()

    def calculate_autocorrelation(self):
        self.autocorrelation = self.returns.autocorr()

    def calculate_moving_average(self, window_size):
        self.moving_average = self.data.rolling(window=window_size).mean()

    def calculate_exponential_smoothing(self, alpha):
        self.exponential_smoothing = self.data.ewm(alpha=alpha).mean()

    def perform_unit_root_test(self):
        from statsmodels.tsa.stattools import adfuller
        self.unit_root_test_result = adfuller(self.data)

    def perform_granger_causality_test(self, other_data):
        from statsmodels.tsa.stattools import grangercausalitytests
        self.granger_causality_test_result = grangercausalitytests(self.data, other_data)

    def plot_time_series(self):
        plt.plot(self.data)
        plt.show()

    def plot_returns(self):
        plt.plot(self.returns)
        plt.show()

    def plot_volatility(self):
        plt.plot(self.volatility)
        plt.show()

    def plot_autocorrelation(self):
        plt.plot(self.autocorrelation)
        plt.show()

    def plot_moving_average(self):
        plt.plot(self.moving_average)
        plt.show()

    def plot_exponential_smoothing(self):
        plt.plot(self.exponential_smoothing)
        plt.show()

if "__main__" == __name__:
    data = yf.download('AAPL', start='2020-01-01', end='2021-01-01')
    analyzer = FinancialTimeSeriesAnalyzer(data['Close'])
    analyzer.calculate_returns()
    analyzer.calculate_volatility()
    analyzer.calculate_autocorrelation()
    analyzer.calculate_moving_average(window_size=20)
    analyzer.calculate_exponential_smoothing(alpha=0.5)
    analyzer.perform_unit_root_test()
    analyzer.perform_granger_causality_test(data['Volume'])
    analyzer.plot_time_series()
    analyzer.plot_returns()
    analyzer.plot_volatility()
    analyzer.plot_autocorrelation()
    analyzer.plot_moving_average()
    analyzer.plot_exponential_smoothing()