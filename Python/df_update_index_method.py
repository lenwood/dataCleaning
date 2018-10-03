# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 10:05:01 2018

@author: ChrisLeonard
"""

import pandas as pd

original = pd.DataFrame(
        {'Company' : ['Xerox', 'Amazon', 'Whole Foods', '3M', 'Gibson', 'Fender'],
         'Product_ID' : ['8B8386', 'FF3E96', 'EE3A8C', 'CD3278', '8B2252', 'FF69B4'],
         'Value' : [9654, 2468, 5743, 3451, 8862, 1497]},
         columns=['Company', 'Product_ID', 'Value'])

replacement_data = pd.DataFrame(
        {'Product_ID' : ['EE3A8C', 'CD3278', 'FF69B4'],
         'Value' : [1119, 1113, 1117]},
         columns=['Product_ID', 'Value'])

updated = original.copy()

updated.set_index('Product_ID', drop=False, inplace=True)
updated.update(replacement_data.set_index('Product_ID'))
updated.reset_index(drop=True, inplace=True)
