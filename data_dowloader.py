from typing import Dict
import pandas as pd


from alpha_vantage.timeseries import TimeSeries
from pandas.core.frame import DataFrame

class data_dowload(): 
    def __init__(self,key,ticker,intervalo):  
        #atributos
        self.API_key  =        key
        self.symbol   =     ticker
        self.interval =  intervalo

        self.outputsize= 'compact'
        
        self.data = []

    def get_data(self):
        
        
        time_series = TimeSeries(key = self.API_key, output_format = "pandas")
        
        lista_de_intervalos = ['1min','5min', '15min', '30min', '60min']

        if  self.interval in lista_de_intervalos :
            
            self.data = time_series.get_intraday(self.symbol, interval = self.interval, outputsize=self.outputsize)[0]
            return self.data
            
        else:
            print("wrong entry")




        
    