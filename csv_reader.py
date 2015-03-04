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
# list of all headings: ['AggegateLevel', 'Cds', 'Name', 'DisciplineType', 'Ethnicity',
# 'Weapons', 'Drugs', 'ViolenceWithInjury', 'ViolenceWithoutInjury', 'OtherNonDefiance',
# 'OtherDefiance', 'Total', 'Year']
# note that aggregate level is not spelling correctly!




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


def export_df_to_csv(df, output_filename):
    df.to_csv(output_filename, index=False, header=False)
    return


""" MAIN METHOD HERE """

ca14 = read_in_file('CA_discip14.csv')
county_data14, district_data14, school_data14, state_data14 = subset_by_level(ca14)

ca13 = read_in_file('CA_discip13.csv')
county_data13, district_data13, school_data13, state_data13 = subset_by_level(ca13)

ca12 = read_in_file('CA_discip12.csv')
county_data12, district_data12, school_data12, state_data12 = subset_by_level(ca12)


# incorrect merge(is adding by column, not by row)
# need to figure out how ot do
# county_total = pd.merge(county_data13, county_data12)

# export subsetted data to csv for Siyang
export_df_to_csv(county_data12, "county_data12.csv")
export_df_to_csv(county_data13, "county_data13.csv")
export_df_to_csv(county_data14, "county_data14.csv")

export_df_to_csv(district_data12, "district_data12.csv")
export_df_to_csv(district_data13, "district_data13.csv")
export_df_to_csv(district_data14, "district_data14.csv")

export_df_to_csv(school_data12, "school_data12.csv")
export_df_to_csv(school_data13, "school_data13.csv")
export_df_to_csv(school_data14, "school_data14.csv")

export_df_to_csv(state_data12, "state_data12.csv")
export_df_to_csv(state_data13, "state_data13.csv")
export_df_to_csv(state_data14, "state_data14.csv")



# exploring the data
list(county_data14)