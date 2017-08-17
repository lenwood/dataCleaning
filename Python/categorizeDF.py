#!/usr/bin/env python 3.6

import pandas as pd
import numpy as np

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

search = ["chicken", "pepperoni", "egg", "cheeseburger", "blt", "omlette"]

category = ["Chicken", "Beef", "Egg", "Beef", "Pork", "Egg"]

food = pd.DataFrame(
    {'dish' : ["chicken cordon bleu", b"Pepperoni Pizza", "", b"egg salad", "kaese spaetzle", "bagel", "GOULASH", b"Fried Chicken", "Chili Relleno", "cheeseburger", np.nan, "BLT", "omlette"],
     'meal' : ["dinner", "dinner", "", "lunch", np.nan, "breakfast", "dinner", "lunch", "dinner", "lunch", np.nan, "lunch", "breakfast"] 
    })

def categorizeDF(df, searchColName, searchList, catList, newColName="Category", undefined="Undefined"):
    # Add default category to all rows to begin with
    # this will be the value for unmatched rows
    oList = [undefined] * df.shape[0]
    df.loc[:, newColName] = oList

    # Add ID so that original sequence can be restored
    df.loc[:, 'ID'] = list(range(1, df.shape[0]+1)) # +1 to account for header row

    # create empty dataframe to work with.
    tempDF = pd.DataFrame(columns=list(df.columns.values), index=np.arange(2))

    # iterate through the strings
    for ind, val in enumerate(searchList):
        x = df[df[searchColName].str.contains(val, case=False) == True]
        categoryColumn = [catList[ind]] * x.shape[0]
        x.loc[:, newColName] = categoryColumn
        tempDF = tempDF.append(x)

    # remove NAs that were induced when empty dataframe was created
    clean = tempDF.dropna(axis=0, how='all')

    # merge the orginal and newly categorized dataframes
    final = df.append(clean)

    retry = final[final[newColName] == undefined]

    invertedSearchList = [typeChanger(x) for x in searchList]

    for ind, val in enumerate(invertedSearchList):
        x = retry[retry[searchColName].str.contains(val, case=False) == True]
        final.set_value(x.index, newColName, catList[ind])

    # remove duplicate rows
    final = final.drop_duplicates(subset='ID', keep='last')

    # restore the original order and remove the ID
    final = final.sort_values(by='ID')
    final = final.drop('ID', axis=1)
    return final

catTest = categorizeDF(food, 'dish', search, category)
