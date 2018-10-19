from functools import reduce
import numpy as np
from pandas import Series
import pandas as pd


class optimizer:
    """a class that can calculate the technical indicators given the stock indices
    these technical indicators include williams_r, rolling standard deviation, absolute
    price oscillators, relative strength index"""

    def __init__(self, stock_data, keys=['williams_r', 'rsi', 'mom', 'trix']):
        """@stock_data: list of dataframes for S&P 500 Companies - this could be either intra-day, 
        daily, weekly or monthly data"""
        self._stock_data = stock_data
        for i in range(len(self._stock_data)):
            for key in keys:
                self._stock_data[i][key] = \
                        Series(np.random.randn(len(self._stock_data[i]['open'].values)), index=self._stock_data[i].index)

    
    def compute_williams_r(self, company_index, pad_value=0):
        c = 0
        company = self._stock_data[company_index]
        for index, row in self._stock_data[company_index].iterrows():
            if c > 14:
                self._stock_data[company_index].set_value(index, 'williams_r', ((max(company['high'][c - 14: c]) - row['close']) / (max(company['high'][c - 14: c]) - min(company['low'][c - 14 : c]))))
            else: 
                self._stock_data[company_index].set_value(index, 'williams_r', pad_value)
            c = c + 1

    def compute_trix(self, company_index, span=15):
        ewm = pd.DataFrame.ewm(self._stock_data[company_index]['close'], span, adjusted=True)
        ewm = pd.DataFrame.ewm(ewm.mean(), span)
        ewm = pd.DataFrame.ewm(ewm.mean(), span)
        ewm = ewm.mean()
        ewm = ((ewm.values[1:] - ewm.values[:-1])/((10**-16) + ewm.values[:-1]))
        self._stock_data[company_index]['trix'][1:] = ewm


    def compute_rsi(self, company_index, span=14):
        delta = self._stock_data[company_index]['close'].diff()[1:]
        up_movement, down_movement = delta.copy(), delta.copy()
        up_movement[up_movement < 0] = 0
        down_movement[down_movement > 0] = 0
        roll_up = pd.DataFrame.ewm(up_movement, span=span)
        roll_down = pd.DataFrame.ewm(down_movement.abs(), span=span)
        relative_strength_index = roll_up.mean()/roll_down.mean()
        relative_strength_index = 100 - (100/(1.0 + relative_strength_index))
        self._stock_data[company_index]['rsi'][1:] = relative_strength_index


    def compute_rolling_std(self, company_index, span=7):
       self._stock_data[company_index]['std_dev'] = self._stock_data[company_index]['close'].rolling(span).std()


    def calculate_moving_average(self, company_index, period=2):
        moving_average = []
        for j in range(period-1):
            moving_average.append(self._stock_data[company_index]['close'].values[j])
        for j in range(period-1, len(self._stock_data[company_index]['close'].values) - 1):
            moving_average.append(np.mean(self._stock_data[company_index]['close'].values[j - (period - 1) : j + 1]))
        val = 0
        for j in range(1, period+1):
            val = val + self._stock_data[company_index]['close'].values[-1 * j]
        moving_average.append(float(val)/period)
        self._stock_data[company_index][str(period) + '-val'] = moving_average


    def compute_absolute_price_oscillator(self, company_index, slow='28-val', fast='7-val'):
        company = self._stock_data[company_index]
        self._stock_data[company_index]['delta'] = np.array(company[fast].values) - np.array(company[slow].values)
        #self._stock_data[company_index]['volume'] = self._stock_data[company_index]['volume'] * self._stock_data[company_index]['close']

    
    def drop_data(self, company_index, keys=['close', 'low']):
        """used to drop any of features from the dataset"""
        for key in keys:
            self._stock_data[company_index] = self._stock_data[company_index].drop(key, axis=1)
    
    def momentum(self, company_index):
        self._stock_data[company_index]['mom'][3:] = self._stock_data[company_index]['close'].values[3:] - self._stock_data[company_index]['mom'][:-3]
    
    def compute_commodity_channel_index(self, company_index, n=14):
        PP = (self._stock_data[company_index]['high'] + self._stock_data[company_index]['low'] + self._stock_data[company_index]['close']) / 3     
        CCI = pd.Series((PP - PP.rolling(n, min_periods=n).mean()) / PP.rolling(n, min_periods=n).std(),                     name='CCI_' + str(n))     
        self._stock_data[company_index]['cci'] = CCI



    def calculate_money_flow_index(self, company_index):
        typical_price = (self._stock_data[company_index]['high'].values + self._stock_data[company_index]['low'].values + self._stock_data[company_index]['close'].values)/3
        self._stock_data[company_index]['mfi'] = typical_price * self._stock_data[company_index]['volume'].values

    
    def average_directional_movement_index(self, company_index, n=4):
        """Calculate the Average Directional Movement Index for given data.      
        :param df: pandas.DataFrame     
        :param n:     
        :param n_ADX:     
        :return: pandas.DataFrame     
        """     
        i = 0     
        UpI = []
        DoI = []     
        while i < len(self._stock_data[company_index]['open'].values) - 1:         
            UpMove = self._stock_data[company_index]['high'].values[i+1] - self._stock_data[company_index]['high'].values[i] 
            DoMove = self._stock_data[company_index]['low'].values[i+1] - self._stock_data[company_index]['low'].values[i]        
            if UpMove > DoMove and UpMove > 0:
                UpD = UpMove         
            else:             
                UpD = 0         
            UpI.append(UpD)         
            if DoMove > UpMove and DoMove > 0:
                DoD = DoMove         
            else:             
                DoD = 0         
            DoI.append(DoD)
            i = i + 1     
        i = 0     
        TR_l = [0]     
        while i < len(self._stock_data[company_index]['open'].values) - 1:
            TR = max(self._stock_data[company_index]['high'].values[i+1], self._stock_data[company_index]['close'].values[i]) - \
            min(self._stock_data[company_index]['low'].values[i+1], self._stock_data[company_index]['close'].values[i])
            TR_l.append(TR)
            i = i + 1     
        TR_S = pd.Series(TR_l)     
        ETA = pd.DataFrame.ewm(TR_S, span=n, min_periods=n)
        ATR = pd.Series(ETA.mean())     
        UpI = pd.Series(UpI)
        DoI = pd.Series(DoI)
        ETA_UpI = pd.DataFrame.ewm(UpI, span=n)
        ETA_DownI = pd.DataFrame.ewm(DoI, span=n)
        PosDI = pd.Series(ETA_UpI.mean() / ATR)     
        NegDI = pd.Series(ETA_DownI.mean() / ATR)
        Sum = pd.DataFrame.ewm(PosDI + NegDI, span=7, min_periods=7)
        ADX = pd.Series((abs(PosDI - NegDI) / (Sum.mean())))
        ADX = ADX.fillna(0)
        print(ADX)
        self._stock_data[company_index]['adx'] = ADX
        #self._stock_data[company_index] = self._stock_data[company_index].dropna()

    def compute_high_low(self, company_index):
        """compute the difference between high and low closing indices of company with index company_index"""
        self._stock_data[company_index]['high'] = self._stock_data[company_index]['high'].values - self._stock_data[company_index]['low'].values

    
    def compute_open_close(self, company_index):
        self._stock_data[company_index]['open'] = self._stock_data[company_index]['close'].values - self._stock_data[company_index]['close'].values

    def merge(self):
        stocks = reduce(lambda left, right: pd.merge(left, right, on='dt'), self._stock_data)
        stocks = stocks.fillna(method='bfill')
        return stocks
