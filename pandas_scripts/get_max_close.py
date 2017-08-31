#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 17:15:58 2017

@author: shane
"""

import pandas as pd

def get_max_close(symbol):
    """
    Return the maximum closing value for stock indicated
    by symbol. Note: data for a stock is stored in the
    file: data/<symbol>.csv
    """
    df = pd.read_csv("../data/{}.csv".format(symbol)) #read in the data
    return df['Close'].max() #computer and return max

def test_run():
    """Function called by Test Run"""
    for symbol in ['AAPL','IBM']:
        print("Max close")
        print(symbol, get_max_close(symbol))
        
if __name__ == "__main__":
    test_run()