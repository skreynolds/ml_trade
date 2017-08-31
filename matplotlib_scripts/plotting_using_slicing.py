#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 10:18:37 2017

@author: shane
"""

"""Slice and plot"""

import os
import pandas as pd
import matplotlib.pyplot as plt


def plot_selected(df, columns, start_index, end_index):
    """Plot the desired columns over index values in the given range."""
    # TODO: Your code here
    # Note: DO NOT modify anything else!
    
    # Create the subsection of data that we want to plot
    df_plot = df.loc[start_index:end_index, columns]
    
    # Normalise data
    df_plot = normalise_data(df_plot)
    
    # Plot the data
    plot_data(df_plot)


def symbol_to_path(symbol, base_dir="../data"):
    """Return CSV file path given ticker symbol"""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def get_data(symbols, dates):
    """
    Read stock data (adjusted close) for given symbols
    from CSV files.
    """
    df = pd.DataFrame(index=dates)
    print(df)
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
            df = df.join(df_temp)
    #df = df.sort_index(ascending=True)    
    print(df)    
    return df

'''An alternative approach to implementing the get data function'''
'''
def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, 'SPY')

    for symbol in symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol), index_col='Date',
                parse_dates=True, usecols=['Date', 'Adj Close'], na_values=['nan'])
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df = df.join(df_temp)
        if symbol == 'SPY':  # drop dates SPY did not trade
            df = df.dropna(subset=["SPY"])

    return df
'''

def plot_data(df, title="Stock prices"):
    """Plot stock prices with a custom title and meaningful axis labels."""
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()

def normalise_data(df):
    return df / df.iloc[0,:]

def test_run():
    # Define a date range
    dates = pd.date_range('2016-04-16', '2017-04-13')

    # Choose stock symbols to read
    symbols = ['GOOG', 'IBM', 'GLD']  # SPY will be added in get_data()
    
    # Get stock data
    df = get_data(symbols, dates)
    
    # Slice and plot
    plot_selected(df, ['SPY', 'IBM'], '2017-03-01', '2017-04-01')


if __name__ == "__main__":
    test_run()