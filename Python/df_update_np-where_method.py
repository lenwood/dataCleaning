# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 13:55:52 2018

@author: ChrisLeonard
"""

import numpy as np
import pandas as pd

data1 = '''\
UID    COMPANY    EML    MAI   TEL
273    7UP        nan    nan   TEL
273    7UP        nan    MAI   nan
906    WSJ        nan    nan   TEL
906    WSJ        EML    nan   nan
736    AIG        nan    MAI   nan
812    KIA        nan    MAI   nan'''

fileobj1 = pd.compat.StringIO(data1)
df1 = pd.read_csv(fileobj1, sep='\s+').replace('NaN', np.nan)

df = df1.copy()

data2 = '''\
UID    COMPNAME    EML    MAI    TEL
812    IBM        nan    nan    TEL'''

fileobj2 = pd.compat.StringIO(data2)
df2 = pd.read_csv(fileobj2, sep='\s+').replace('NaN', np.nan)

df1['COMPANY'] = np.where(df1['UID'].isin(df2['UID']), df2['COMPNAME'], df1['COMPANY'])

del data1, data2, fileobj1, fileobj2
