#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 17:57:49 2017

@author: shane
"""

import pandas as pd
import matplotlib.pyplot as plt

def test_run():
    df = pd.read_csv("~/Documents/ml_trade/data/AAPL.csv")
    print(df["Adj Close"])
    df['Adj Close'].plot()
    plt.show() # must be called to show plots
    
if __name__ == "__main__":
    test_run()