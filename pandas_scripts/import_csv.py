#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 13:23:32 2017

@author: shane
"""

import pandas as pd

def test_run():
    df = pd.read_csv("data/AAPL.csv")
    print(df.head())
    print(df.tail())
    
if __name__ == "__main__":
    test_run()