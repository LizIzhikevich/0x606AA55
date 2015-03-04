__author__ = 'joanneyeh'
import pandas as pd


def read_in_file(filename):
    data = pd.read_csv(filename)
    return data


""" MAIN METHOD """

ca14 = read_in_file('CA_discip14.csv')
ca15 = read_in_file('')
# save column titles to list
column_names = list(ca14)
print(column_names)

# list unique values in column 0
agg_levels = pd.unique(ca14[column_names[0]])
names = pd.unique(ca14[column_names[2]])
disc_type = pd.unique(ca14[column_names[3]])
list_ethnic = pd.unique(ca14[column_names[4]])
year = pd.unique(ca14[column_names[5]])

# print(ca14)


def subset_by_level(dataframe):
    county_data = dataframe[dataframe.AggregateLevel == 'O']
    district_data = dataframe[dataframe.AggregateLevel == 'D']
    school_data = dataframe[dataframe.AggregateLevel == 'S']
    state_data = dataframe[dataframe.AggregateLevel == 'T']
    return county_data, district_data, school_data, state_data

