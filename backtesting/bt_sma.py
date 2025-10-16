import time
import datetime
import pandas as pd
from backtesting import Strategy, Backtest
from backtesting.lib import crossover


def SMA(values, n):
    """
    Return simple moving average of `values`, at
    each step taking into account `n` previous values.
    """
    return pd.Series(values).rolling(n).mean()



class SmaCross(Strategy):
    n1 = 15 
    n2 = 91
    
    def init(self):
        # Precompute the two moving averages
        self.sma1 = self.I(SMA, self.data.df['Close'], self.n1)
        self.sma2 = self.I(SMA, self.data.df['Close'], self.n2)

    
    def next(self):
        # If sma1 crosses above sma2, close any existing
        # short trades, and buy the asset
        if crossover(self.sma1, self.sma2):
            self.position.close()
            self.buy(size=1)

        # Else, if sma1 crosses below sma2, close any existing
        # long trades, and sell the asset
        elif crossover(self.sma2, self.sma1):
            self.position.close()
            #self.sell() #size=1)


def my_commision(size: float, price: float):
    size = round(abs(size))
    rc = size * 10;  ## 10h зper share
    return rc
    

start = time.perf_counter()
dt = pd.read_csv("./SBER_M1.csv.zip", sep=";",  parse_dates=[["Date","Time"]], index_col=0)
dt.index.name = 'Date'

bt = Backtest(dt, SmaCross, cash=1_000_000, commission=(10,.0))  
stats = bt.run()

end = time.perf_counter()
print(f"Execution time for sum_list: {end - start:.4f} seconds\n\n")

print(stats)


