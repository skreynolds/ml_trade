#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 17:41:34 2017

@author: shane
"""

import pandas as pd

def get_mean_volume(symbol):
    """
    Return the mean volume for stock indicated by
    symbol. Note: Data for a stock is stored in file:
    data/<symbol.csv>
    """
    df = pd.read_csv("~/Documents/ml_trade/data/{}.csv".format(symbol)) #read in data
    # TODO: Compute and return the mean volume for this stock
    #return df["Close"].mean() will also work
    length =  len(df["Close"])
    return df["Close"].sum()/length

def test_run():
    """
    Function called be Test Run.
    """
    for symbol in ['AAPL','IBM']:
        print("Mean Volume")
        print(symbol, get_mean_volume(symbol))
        
if __name__ == "__main__":
    test_run()