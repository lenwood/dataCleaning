import pandas as pd

DF1 = pd.DataFrame(
    {'AA' : [3, 4, 5, 6, 7, 11, 12],
     'BB' : ['C', 'D', 'E', 'F', 'G', 'K', 'L']
    })

DF2 = pd.DataFrame(
    {'AA' : [4, 5, 8, 9, 10, 11, 12],
     'BB' : ['D', 'E', 'H', 'I', 'J', 'K', 'L']
    })

DF1list = [True] * DF1.shape[0]
DF2list = [True] * DF2.shape[0]

DF1.loc[:, 'inDF1'] = DF1list
DF2.loc[:, 'inDF2'] = DF2list

bigDF = pd.merge(DF1, DF2, how="outer")

not_in_DF1 = bigDF.drop('inDF2', axis=1)
not_in_DF1 = not_in_DF1[pd.isnull(not_in_DF1).any(axis=1)]
not_in_DF1 = not_in_DF1.drop('inDF1', axis=1)

print not_in_DF1

not_in_DF2 = bigDF.drop('inDF1', axis=1)
not_in_DF2 = not_in_DF2[pd.isnull(not_in_DF2).any(axis=1)]
not_in_DF2 = not_in_DF2.drop('inDF2', axis=1)

print not_in_DF2