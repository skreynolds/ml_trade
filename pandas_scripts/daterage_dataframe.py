#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 21:33:37 2017

@author: shane
"""

import pandas as pd

def test_run():
    start_date = '2016-04-18'
    end_date = '2017-04-13'
    dates = pd.date_range(start_date,end_date)
    
    # Create an empty dataframe
    df1 = pd.DataFrame(index=dates)
    
    # Read SPY data into temporary dataframe
    dfSPY = pd.read_csv("../data/SPY.csv",
                        index_col="Date",
                        parse_dates=True,
                        usecols=['Date','Adj Close'],
                        na_values=['nan'])

    # Join the two dataframes using DataFrame.join()
    df1 = df1.join(dfSPY)
    
    # Drop NaN values
    df1 = df1.dropna()
    
    # Print the dataframe
    print(df1.head())

if __name__ == "__main__":
    test_run()