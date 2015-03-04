__author__ = 'joanneyeh'
import pandas as pd

"""
This program will return subsets of each dataset and
concatenate corresponding subsets together.
Usage:

"""


def read_in_file(filename):
    data = pd.read_csv(filename)
    return data

"""
Methods to print out list of unique values in a column (for sanity check):

column_names = list(ca14)

agg_levels = pd.unique(ca14[column_names[0]])
names = pd.unique(ca14[column_names[2]])
disc_type = pd.unique(ca14[column_names[3]])
list_ethnic = pd.unique(ca14[column_names[4]])
year = pd.unique(ca14[column_names[5]])
"""


def subset_by_level(df):
    county_data = df[df.AggegateLevel == 'O']
    district_data = df[df.AggegateLevel == 'D']
    school_data = df[df.AggegateLevel == 'S']
    state_data = df[df.AggegateLevel == 'T']
    return county_data, district_data, school_data, state_data

""" MAIN METHOD HERE """

ca14 = read_in_file('CA_discip14.csv')
country_data14, district_data14, school_data14, state_data14 = subset_by_level(ca14)

ca13 = read_in_file('CA_discip13.csv')
country_data13, district_data13, school_data13, state_data13 = subset_by_level(ca13)

ca12 = read_in_file('CA_discip12.csv')
country_data12, district_data12, school_data12, state_data12 = subset_by_level(ca12)

