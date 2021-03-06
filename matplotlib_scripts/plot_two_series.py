#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 21:24:12 2017

@author: shane
"""

import pandas as pd
import matplotlib.pyplot as plt

def test_run():
    df = pd.read_csv("../data/AAPL.csv")
    df[['Close','High']].plot()
    plt.show()

if __name__ == "__main__":
    test_run()