#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 22:33:00 2017

@author: shane
"""

import pandas as pd

def test_run():
    
    # Create a date range specifying start and end dates
    start_date = '2016-04-18'
    end_date = '2017-04-13'
    dates = pd.date_range(start_date,end_date)
    
    # Create a temp dataframe which contains dates
    df1 = pd.DataFrame(index=dates)
    
    # Read in the SPY data
    dfSPY = pd.read_csv('~/Documents/ml_trade/data/SPY.csv',
                        index_col='Date',
                        parse_dates=True,
                        usecols=["Date","Adj Close"],
                        na_values=['nan'])
    
    # Rename the column to prevent overlap
    dfSPY = dfSPY.rename(columns={'Adj Close': 'SPY'})
    
    # Join the read in SPY data to the temp date range
    df1 = df1.join(dfSPY,how='inner')
    
    # Specify the list of symbols that we want to
    # append to the dataframe
    symbols = ['GOOG','IBM','GLD']
    
    # For loop reads in more stocks
    for symbol in symbols:
        df_temp = pd.read_csv("~/Documents/ml_trade/data/{}.csv".format(symbol),
                              index_col='Date',
                              parse_dates=True,
                              usecols=['Date','Adj Close'],
                              na_values=['nan'])
        
        # Rename the columns to prevent overlap
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df1 = df1.join(df_temp)
    
    print(df1)

if __name__ == '__main__':
    test_run()