import pandas as pd
import numpy as np

search = ["chicken", "pepperoni", "egg", "cheeseburger", "blt", "omlette"]

category = ["Chicken", "Beef", "Egg", "Beef", "Pork", "Egg"]

food = pd.DataFrame(
    {'dish' : ["chicken cordon bleu", "Pepperoni Pizza", "egg salad", "bagel", "GOULASH", "Fried Chicken", "Chili Relleno", "cheeseburger", "BLT", "omlette"],
     'meal' : ["dinner", "dinner", "lunch", "breakfast", "dinner", "lunch", "dinner", "lunch", "lunch", "breakfast"] 
    })


def categorizeDF(df, searchColName, searchList, catList, newColName="Category"):
    # Add default category to all rows to begin with
    # this will be the value for unmatched rows
    oList = ['Undefined'] * df.shape[0]
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
    clean = tempDF.dropna(axis=0)

    # merge the orginal and newly categorized dataframes
    final = df.append(clean)

    # remove duplicate rows
    final = final.drop_duplicates(subset='ID', keep='last')

    # restore the original order and remove the ID
    final = final.sort_values(by='ID')
    final = final.drop('ID', axis=1)
    return final

print categroizeDF(food, 'dish', search, category)

