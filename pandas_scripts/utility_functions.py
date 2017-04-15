#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 23:04:26 2017

@author: shane
"""

"""
Utility functions which can be used to be more
productive more quickly
"""
import os
import pandas as pd

def symbol_to_path(symbol, base_dir="~/Documents/ml_trade/data"):
    """Return CSV file path given ticker symbol"""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))


def get_data(symbols, dates):
    """
    Read stock data (adjusted close) for given symbols
    from CSV files.
    """
    df = pd.DataFrame(index=dates)
    
    if 'SPY' not in symbols: #add SPY for reference
        symbols.insert(0,'SPY')
        
    # This for loop will loop through all the desired
    # symbols in the symbol list and create a dataframe
    # containing all the required data
    for symbol in symbols:
        # Get path for .csv file for symbol
        sym_path = symbol_to_path(symbol)
        # Load data from csv and create dataframe
        if symbol == 'SPY':
            dfSPY = pd.read_csv(sym_path,
                                index_col="Date",
                                parse_dates=True,
                                usecols=["Date","Adj Close"],
                                na_values=['nan'])
            
            dfSPY = dfSPY.rename(columns={"Adj Close": str(symbol)})
            df = df.join(dfSPY,how='inner')
        else:
            df_temp = pd.read_csv(sym_path,
                                  index_col="Date",
                                  parse_dates=True,
                                  usecols=["Date","Adj Close"],
                                  na_values=['nan'])
            df_temp = df_temp.rename(columns={"Adj Close": str(symbol)})
            df = df.join(df_temp)
        
    return df

def test_run():
    # Define a date range
    start_date = "2016-04-16"
    end_date = "2017-04-13"
    dates = pd.date_range(start_date,end_date)
    
    # Choose stock symbols to read
    symbols = ["GOOG", "IBM", "GLD"]
    
    # Get stock data
    df = get_data(symbols,dates)
    print(df)
    
if __name__ == "__main__":
    test_run()