import pandas as pd

DF1 = pd.DataFrame(
    {'AA' : [3, 4, 5, 6, 7, 11, 12],
     'BB' : ['C', 'D', 'E', 'F', 'G', 'K', 'L']
    })

DF2 = pd.DataFrame(
    {'AA' : [4, 5, 8, 9, 10, 11, 12],
     'BB' : ['D', 'E', 'H', 'I', 'J', 'K', 'L']
    })

# method 1 uses the pandas isin function
not_in_DF1_method1 = DF2[~DF2['AA'].isin(DF1['AA'])]
print(not_in_DF1_method1)


not_in_DF2_method1 = DF1[~DF1['AA'].isin(DF2['AA'])]
print(not_in_DF2_method1)

# method 2 is more generic but produces the same results
DF1list = [True] * DF1.shape[0]
DF2list = [True] * DF2.shape[0]

DF1.loc[:, 'inDF1'] = DF1list
DF2.loc[:, 'inDF2'] = DF2list

bigDF = pd.merge(DF1, DF2, how="outer")

not_in_DF1_method2 = bigDF.drop('inDF2', axis=1)
not_in_DF1_method2 = not_in_DF1_method2[pd.isnull(not_in_DF1_method2).any(axis=1)]
not_in_DF1_method2 = not_in_DF1_method2.drop('inDF1', axis=1)

print(not_in_DF1_method2)

not_in_DF2_method2 = bigDF.drop('inDF1', axis=1)
not_in_DF2_method2 = not_in_DF2_method2[pd.isnull(not_in_DF2_method2).any(axis=1)]
not_in_DF2_method2 = not_in_DF2_method2.drop('inDF2', axis=1)

print(not_in_DF2_method2)
