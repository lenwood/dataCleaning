#!/usr/bin/env python 3.6

import numpy as np
import pandas as pd

def typeChanger(s):
    if isinstance(s, (bytes, bytearray)):
        try:
            newS = s.decode('utf-8')
        except AttributeError:
            newS = s
    elif isinstance(s, str):
        try:
            newS = s.encode('utf-8')
        except AttributeError:
            newS = s
    else:
        newS = s
    return newS

def categorizeDF(df, searchColName, searchList, catList, newColName="Category", undefinedValue="Undefined"):
    # create copy of df to avoid altering the orginal
    myDF = df.copy()

    # Add default category to all rows to begin with
    # this will be the value for unmatched rows
    myDF.loc[:, newColName] = undefinedValue

    # Add ID so that original sequence can be restored
    myDF.loc[:, 'ID'] = list(range(1, myDF.shape[0]+1)) # +1 to account for header row

    # create empty dataframe to work with.
    tempDF = pd.DataFrame(columns=list(myDF.columns.values), index=np.arange(2))

    # iterate through the strings
    for ind, val in enumerate(searchList):
        x = myDF[myDF[searchColName].str.match(val, case=False, na=False)]
        y = x.copy()
        y.loc[:, newColName] = catList[ind]
        tempDF = tempDF.append(y)

    # remove NAs that were induced when empty dataframe was created
    clean = tempDF.dropna(axis=0, how='all')

    # merge the orginal and newly categorized dataframes
    final = myDF.append(clean)

    retry = final[final[newColName] == undefinedValue]

    invertedSearchList = [typeChanger(x) for x in searchList]

    for ind, val in enumerate(invertedSearchList):
        x = retry[retry[searchColName].str.contains(val, case=False, regex=False) == True]
        final.at[x.index, newColName] = catList[ind]

    # remove duplicate rows
    final = final.drop_duplicates(subset='ID', keep='last')

    # restore the original order and remove the ID
    final = final.sort_values(by='ID')
    final = final.drop('ID', axis=1)
    return final
