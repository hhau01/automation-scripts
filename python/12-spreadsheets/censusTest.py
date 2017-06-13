#!/usr/bin/env python3

# census2010 test

import os

# directory of census2010.py
os.chdir()

import census2010

census2010.allData['AK']['Anchorage']
anchoragePop = census2010.allData['AK']['Anchorage']['pop']
print('The 2010 population of Anchorage was ' + str(anchoragePop))
