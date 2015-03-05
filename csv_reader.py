__author__ = 'joanneyeh'
import pandas as pd

"""
This program will return subsets of each dataset and
concatenate corresponding subsets together.

Methods written in here : read_in_file, get_unique_values, subset_by_level,
export_df_to_csv, subset_cols_dataframe, append_dataframes

Dependency: csv_parser must be run first!
"""


def read_in_file(filename):
    data = pd.read_csv(filename)
    return data


#  prints out the unique categorical values found in specified columns
def get_unique_values(df, verbose=False):
    column_names = list(df)
    agg_levels = pd.unique(df[column_names[0]])
    names = pd.unique(df[column_names[2]])
    discip_type = pd.unique(df[column_names[3]])
    ethnic_groups = pd.unique(df[column_names[4]])
    year = pd.unique(df[column_names[5]])
    if verbose:
        print("Aggregate Levels are: %s" % agg_levels)
        print("Names of schools are: %s" % names)
        print("Discipline types are: %s" % discip_type)
        print("Ethnic groups are: %s" % ethnic_groups)
        print("Years are: %s" % year)
    return


#  subset the data by AGGREGATION LEVEL
#  D=Local educational agency totals (includes districts and direct funded charter schools)
#  O=County totals
#  S=SchoolTotals
#  T=State totals
def subset_by_agg_level(df):
    column_names = list(df)
    county_data = df[df.AggegateLevel == 'O']
    district_data = df[df.AggegateLevel == 'D']
    school_data = df[df.AggegateLevel == 'S']
    state_data = df[df.AggegateLevel == 'T']
    # label columns in subset:
    county_data.columns = column_names
    district_data.columns = column_names
    school_data.columns = column_names
    state_data.columns = column_names
    return county_data, district_data, school_data, state_data


#  export a specified dataframe to csv
def export_df_to_csv(df, output_filename):
    df.to_csv(output_filename, index=False, header=False)
    return


def subset_cols_dataframe(df, col_indexes):
    subset = df.iloc[:, col_indexes]
    return subset


def append_dataframes(array_df):
    temp = array_df[0]
    for i in range(1, len(array_df)):
        temp = temp.append(array_df[i])
    return temp

""" MAIN METHOD BEGINS HERE """

#  this chunk of code just takes the input csv and subsets it
ca14 = read_in_file('CA_discip14.csv')  # 2014 California Data saved in ca14
county_data14, district_data14, school_data14, state_data14 = subset_by_agg_level(ca14)
ca13 = read_in_file('CA_discip13.csv')  # 2013 California Data saved in ca13
county_data13, district_data13, school_data13, state_data13 = subset_by_agg_level(ca13)
ca12 = read_in_file('CA_discip12.csv')  # 2012 California Data saved in ca12
county_data12, district_data12, school_data12, state_data12 = subset_by_agg_level(ca12)

#  print out unique categorical values found in certain columns (sanity check)
get_unique_values(ca13, verbose=False)

indices_ethnicity = [4, 6, 12]
ethn14 = subset_cols_dataframe(county_data14, indices_ethnicity)
ethn13 = subset_cols_dataframe(county_data13, indices_ethnicity)
ethn12 = subset_cols_dataframe(county_data12, indices_ethnicity)

total_ethnic_discip = append_dataframes([ethn14, ethn13, ethn12])
export_df_to_csv(total_ethnic_discip, 'total_ethnic_discip.csv')