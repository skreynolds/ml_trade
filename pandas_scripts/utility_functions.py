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
import matplotlib.pyplot as plt

def symbol_to_path(symbol, base_dir="../data"):
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
            df = df.join(dfSPY,how='inner') # inner joins and drops NaN
        else:
            df_temp = pd.read_csv(sym_path,
                                  index_col="Date",
                                  parse_dates=True,
                                  usecols=["Date","Adj Close"],
                                  na_values=['nan'])
            df_temp = df_temp.rename(columns={"Adj Close": str(symbol)})
            df = df.join(df_temp,how='inner')
    df = df.sort_index(ascending=True)
    return df

def plot_data(df,title='Stock prices'):
    '''Plot stock prices'''
    ax = df.plot(title=title,fontsize=8)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show() # must be called to show plots in some envs

def test_run():
    # Define a date range
    start_date = "2016-04-16"
    end_date = "2017-04-13"
    dates = pd.date_range(start_date,end_date)
    
    # Choose stock symbols to read
    symbols = ["GOOG", "IBM", "GLD"]
    
    # Get stock data
    df = get_data(symbols,dates)
    #print(df)
    
    # Slice a by row (daterange)
    #print(df.loc['2017-04-11':'2017-04-13'])
    
    # Slicing by column
    #print(df['GOOG']) # A single label selects a single column
    #print(df[['IBM','GOOG']]) # a list of labels selects multiple columns
    
    # Slicing by row and column
    #print(df.loc['2017-04-11':'2017-04-13', ['SPY','IBM']])
    
    # Slicing by numerical index location is done using the .iloc[]
    #print(df.iloc[0,:]) # note you have to use numbers
    print(df)
    plot_data(df)
          
if __name__ == "__main__":
    test_run()