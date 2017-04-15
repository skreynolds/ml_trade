#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 17:03:06 2017

@author: shane
"""

import pandas as pd

def test_run():
    df = pd.read_csv("data/AAPL.csv")
    print(df[10:21]) #rows between index 10 and 20
    
if __name__ == "__main__":
    test_run()