Python Data Cleaning Scripts
============================

#### categorizeDF
This is a script to categorize otherwise messy data in a Pandas data frame. It contains a function that looks at a column of messy character data, and produces a new column of categorized data. The inputs are the ugly data frame, the name of the column containing messy data, a list of search strings and a list of category names (these have to be correlated). You have the option of naming the name of the new column that's added to your data frame, and specifying how unmatched search terms are listed in the resulting data frame.

Usage:

    cleanDF = categorizeDF(uglyDataFrame, 'Column Name To Search', list_of_search_strings, list_of_category_strings)

The three notes about this are:

1. The searches & categories must be correlated. In other words, the search string in the 4th position of your list will be assigned the category in the 4th position of your category list.
2. If a field contains both of your search strings, the one category assigned will be the last one in your list.
3. The script is compatible with Python versions 2.7 and 3.6.

The benefit of this method of categorization is that it's fast and requires very little setup. For the cases where I have a lot of search strings and/or categories, I add them as I work with a particular data set. If the list becomes unwieldy I switch to storing them in a CSV.

    search_category_lists = pd.read_csv("search_and_category_lists.csv", header=None)

    searchStrings = search_category_lists.ix[:, 0].tolist()
    categoryStrings = search_category_lists.ix[:, 1].tolist()

#### notInBoth
Script to identify rows not present in 2 similar data frames. Sample usage included in the script.